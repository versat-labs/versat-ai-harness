#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
failures=0
validation_python="${PYTHON:-python3}"
sdd_args=(--phase planning)
quality_base="${VERSAT_QUALITY_BASE:-}"
while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --quality-base)
      if [[ "$#" -lt 2 || -z "$2" || "$2" == --* ]]; then
        echo "--quality-base requires a Git comparison revision" >&2
        exit 1
      fi
      quality_base="$2"
      shift 2
      ;;
    --baseline)
      if [[ "$#" -lt 2 || -z "$2" || "$2" == --* ]]; then
        echo "--baseline requires a trusted Git revision" >&2
        exit 1
      fi
      sdd_args+=(--baseline "$2")
      if [[ -z "$quality_base" ]]; then
        quality_base="$2"
      fi
      shift 2
      ;;
    --require-archive)
      sdd_args+=(--require-archive)
      shift
      ;;
    *)
      echo "Usage: $0 [--quality-base git-revision] [--baseline trusted-git-revision] [--require-archive]" >&2
      exit 1
      ;;
  esac
done

if [[ "${VERSAT_STRUCTURAL_ONLY:-}" != "1" ]]; then
  if [[ -z "$quality_base" ]]; then
    echo "FAIL quality comparison needs --quality-base (for example, origin/main)." >&2
    failures=$((failures + 1))
  elif ! bash "${repo_root}/scripts/validate/quality.sh" --root "$repo_root" --base "$quality_base"; then
    failures=$((failures + 1))
  fi
fi

required_files=(
  "AGENTS.md"
  "README.md"
  "VERSION"
  "plugin.json"
  ".codex-plugin/plugin.json"
  ".agents/plugins/marketplace.json"
  "standards/index.yaml"
  "sdd/process.md"
  "schemas/project.schema.yaml"
  "docs/architecture/overview.md"
  "docs/decisions/README.md"
  "docs/decisions/0011-root-portable-plugin-package.md"
  "validators/plugin/validate.py"
  "sdd/README.md"
  "sdd/metadata.md"
  "sdd/workflows/new-change.md"
  "sdd/workflows/implement-change.md"
  "sdd/workflows/validate-change.md"
  "sdd/workflows/archive-change.md"
  "validators/sdd/validate.py"
  "requirements-validation.txt"
  "tests/validators/test_sdd.py"
)

for relative_path in "${required_files[@]}"; do
  if [[ ! -s "${repo_root}/${relative_path}" ]]; then
    echo "FAIL missing or empty: ${relative_path}"
    failures=$((failures + 1))
  fi
done

skill_names=(
  "project-bootstrap"
  "versat-sdd"
  "project-audit"
  "architecture-review"
  "project-maintenance"
  "sifen-electronic-documentation"
)

for skill_name in "${skill_names[@]}"; do
  skill_file="skills/${skill_name}/SKILL.md"
  if [[ ! -s "${repo_root}/${skill_file}" ]]; then
    echo "FAIL missing or empty: ${skill_file}"
    failures=$((failures + 1))
  fi
done

if ! grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+([.-][0-9A-Za-z.-]+)?$' "${repo_root}/VERSION"; then
  echo "FAIL VERSION is not semantic"
  failures=$((failures + 1))
fi

if command -v "${validation_python}" >/dev/null 2>&1; then
  if ! "${validation_python}" "${repo_root}/validators/plugin/validate.py"; then
    failures=$((failures + 1))
  fi
  if "${validation_python}" -c 'import yaml, jsonschema' >/dev/null 2>&1; then
    if ! PYTHONDONTWRITEBYTECODE=1 "${validation_python}" "${repo_root}/validators/security/validate.py" --check-policy; then
      failures=$((failures + 1))
    fi
    if ! PYTHONDONTWRITEBYTECODE=1 "${validation_python}" "${repo_root}/validators/sdd/validate.py" --root "${repo_root}" "${sdd_args[@]}"; then
      failures=$((failures + 1))
    fi
    if ! PYTHONDONTWRITEBYTECODE=1 "${validation_python}" -m unittest discover -s "${repo_root}/tests/validators" -p 'test_*.py'; then
      failures=$((failures + 1))
    fi
    if ! PYTHONDONTWRITEBYTECODE=1 "${validation_python}" -m unittest discover -s "${repo_root}/tests/execution" -p 'test_*.py'; then
      failures=$((failures + 1))
    fi
    if ! PYTHONDONTWRITEBYTECODE=1 "${validation_python}" -m unittest discover -s "${repo_root}/tests/skills" -p 'test_sifen_documentation.py'; then
      failures=$((failures + 1))
    fi
  else
    echo "FAIL install validation dependencies in a virtual environment: python -m pip install -r requirements-validation.txt"
    echo "Then activate that environment or set PYTHON to its interpreter path."
    failures=$((failures + 1))
  fi
else
  echo "FAIL Python is required; activate a virtual environment or set PYTHON to its interpreter path."
  failures=$((failures + 1))
fi

if [[ "${failures}" -gt 0 ]]; then
  echo "Validation failed with ${failures} error(s)."
  exit 1
fi

echo "Versat AI Harness package, SDD contract and validator tests passed."
