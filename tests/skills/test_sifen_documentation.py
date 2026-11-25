"""Behavioral and integrity regression tests for the portable SIFEN capability."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / 'skills/sifen-electronic-documentation'


class SifenDocumentationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)

    def run_script(self, script, *args, skill=SKILL):
        return subprocess.run([sys.executable, str(skill / 'scripts' / script), *map(str, args)],
                              cwd=self.work, capture_output=True, text=True, timeout=30)

    def query(self, *args, skill=SKILL):
        return self.run_script('query_rules.py', *args, skill=skill)

    def test_discovery_preserves_existing_skills(self):
        for name in ['architecture-review', 'project-audit', 'project-bootstrap',
                     'project-maintenance', 'versat-sdd', 'sifen-electronic-documentation']:
            self.assertIn(f'name: {name}', (ROOT/'skills'/name/'SKILL.md').read_text())
        result = subprocess.run([sys.executable, str(ROOT/'validators/plugin/validate.py')],
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_source_and_target_integrity(self):
        inventory = json.loads((SKILL/'references/import-inventory.json').read_text())
        for row in inventory['files']:
            if row['target'] is None:
                self.assertEqual(row['disposition'], 'excluded-os-metadata')
                continue
            target = SKILL / row['target']
            self.assertTrue(target.is_file(), row['target'])
            if row['disposition'] == 'preserved-source-bytes':
                self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(), row['source_sha256'])
        integrity = json.loads((SKILL/'references/target-integrity.json').read_text())
        actual = {str(f.relative_to(SKILL)) for f in SKILL.rglob('*') if f.is_file()
                  and '__pycache__' not in f.parts and f.name != 'target-integrity.json'}
        self.assertEqual(set(integrity['files']), actual)
        for path, digest in integrity['files'].items():
            self.assertEqual(hashlib.sha256((SKILL/path).read_bytes()).hexdigest(), digest, path)
        self.assertFalse(list(SKILL.rglob('.DS_Store')))

    def test_markdown_links_resolve(self):
        for file in [*SKILL.rglob('*.md'), *ROOT.glob('docs/user-docs/guides/sifen-electronic-documentation*.md')]:
            for target in re.findall(r'\]\(([^)]+)\)', file.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                path = unquote(target.split('#',1)[0].strip('<>'))
                self.assertTrue((file.parent/path).exists(), f'{file}: {target}')

    def test_known_note_match_is_source_backed(self):
        result = self.query('GENFE010', '--include', 'notes', '--max', '100', '--context', '1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('NT_E_KUATIA_027_MT_V150.txt', result.stdout)
        self.assertIn('GENFE010', result.stdout)

    def test_no_match_is_successful_empty_result(self):
        result = self.query('SYNTHETIC_ABSENT_TOKEN_56cdab')
        self.assertEqual(result.returncode, 0)
        self.assertIn('No matches found', result.stdout)

    def test_literal_regex_case_context_and_limit(self):
        fixture = self.work/'skill'
        (fixture/'scripts').mkdir(parents=True)
        shutil.copyfile(SKILL/'scripts/query_rules.py', fixture/'scripts/query_rules.py')
        corpus = fixture/'references/extracted-text'
        corpus.mkdir(parents=True)
        (corpus/'sample.txt').write_text('before\nA.B\na.b\nAxB\nafter\n')
        literal = self.query('A.B', '--case-sensitive', '--context', '1', skill=fixture)
        self.assertEqual(literal.returncode, 0)
        self.assertIn('1 match(es)', literal.stdout)
        self.assertIn('before', literal.stdout)
        regex = self.query('A.B', '--regex', '--max', '2', '--context', '0', skill=fixture)
        self.assertEqual(regex.stdout.count('### '), 2)
        self.assertIn('Result limit 2 reached', regex.stdout)

    def test_invalid_query_arguments(self):
        for args in [('[', '--regex'), ('x','--max','0'), ('x','--context','-1'), ('',)]:
            with self.subTest(args=args):
                result = self.query(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('error:', result.stderr)

    def test_missing_corpus_is_not_no_match(self):
        fixture = self.work/'skill'
        (fixture/'scripts').mkdir(parents=True)
        shutil.copyfile(SKILL/'scripts/query_rules.py',fixture/'scripts/query_rules.py')
        result = self.query('GENFE010', skill=fixture)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Missing or empty', result.stderr)
        self.assertNotIn('No matches found', result.stdout)

    def test_missing_selection_is_explicit(self):
        result = self.query('GENFE010','--include','nonexistent-sources')
        self.assertNotEqual(result.returncode,0)
        self.assertIn('No searchable sources',result.stderr)

    def test_relocated_package_lookup_and_export(self):
        fixture = self.work/'relocated-harness'
        # Copy the full provider, excluding repository metadata and transient outputs.
        shutil.copytree(ROOT, fixture, ignore=shutil.ignore_patterns('.git','__pycache__','.venv','tmp'))
        skill = fixture/'skills/sifen-electronic-documentation'
        result = self.query('GENFE010','--include','notes',skill=skill)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertIn('GENFE010',result.stdout)
        result = self.run_script('export_agent.py','generic','--destination',self.work/'consumer',skill=skill)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertTrue((self.work/'consumer/AGENTS.md').is_file())
        self.assertTrue((skill/'../../standards/index.yaml').exists())

    def test_all_platform_exports(self):
        outputs = {'claude':['.claude/agents/sifen-electronic-documentation.md'],
                   'gemini':['.gemini/sifen-core.md','GEMINI.md'],
                   'copilot':['.github/sifen-core.md','.github/copilot-instructions.md'],
                   'cursor':['.cursor/rules/sifen-electronic-documentation.mdc'],
                   'generic':['AGENTS.md']}
        for platform, paths in outputs.items():
            with self.subTest(platform=platform):
                destination = self.work/platform
                result = self.run_script('export_agent.py',platform,'--destination',destination)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertEqual({str(f.relative_to(destination)) for f in destination.rglob('*') if f.is_file()},set(paths))
                all_text = '\n'.join((destination/p).read_text() for p in paths)
                self.assertIn('SIFEN_SKILL_ROOT',all_text)
                self.assertIn('query_rules.py',all_text)
                self.assertNotIn('/Users/',all_text)

    def test_later_collision_creates_no_partial_output(self):
        for platform, collision, early in [('gemini','GEMINI.md','.gemini/sifen-core.md'),
                                           ('copilot','.github/copilot-instructions.md','.github/sifen-core.md')]:
            with self.subTest(platform=platform):
                destination=self.work/platform
                path=destination/collision; path.parent.mkdir(parents=True); path.write_text('KEEP\n')
                result=self.run_script('export_agent.py',platform,'--destination',destination)
                self.assertNotEqual(result.returncode,0)
                self.assertEqual(path.read_text(),'KEEP\n')
                self.assertFalse((destination/early).exists())

    def test_explicit_force_replaces_output(self):
        destination=self.work/'consumer'; destination.mkdir()
        path=destination/'AGENTS.md'; path.write_text('OLD\n')
        result=self.run_script('export_agent.py','generic','--destination',destination,'--force')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertNotEqual(path.read_text(),'OLD\n')
        self.assertIn('SIFEN_SKILL_ROOT',path.read_text())

    def test_symlink_output_is_rejected_even_with_force(self):
        destination=self.work/'consumer'; destination.mkdir()
        outside=self.work/'outside'; outside.write_text('KEEP\n')
        (destination/'AGENTS.md').symlink_to(outside)
        result=self.run_script('export_agent.py','generic','--destination',destination,'--force')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(outside.read_text(),'KEEP\n')

    def test_invalid_export_platform_and_missing_guidance(self):
        result=self.run_script('export_agent.py','unknown','--destination',self.work/'consumer')
        self.assertNotEqual(result.returncode,0)
        self.assertFalse((self.work/'consumer').exists())
        fixture=self.work/'skill'; (fixture/'scripts').mkdir(parents=True)
        shutil.copyfile(SKILL/'scripts/export_agent.py',fixture/'scripts/export_agent.py')
        result=self.run_script('export_agent.py','generic','--destination',self.work/'consumer',skill=fixture)
        self.assertNotEqual(result.returncode,0)
        self.assertFalse((self.work/'consumer').exists())


if __name__ == '__main__':
    unittest.main()
