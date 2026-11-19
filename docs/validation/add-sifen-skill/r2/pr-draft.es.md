# Añadir skill de documentación electrónica SIFEN

## Resultado

Añade una skill portable para consultar el Manual v150, las Notas Técnicas 1–27 y las guías suministradas, con trazabilidad a las fuentes, búsqueda local y exportación opcional de instrucciones para cinco plataformas. Incluye documentación EN/PT/ES y Apache-2.0 para el material de autoría; los documentos oficiales quedan excluidos de esa licencia.

**Borrador de trabajo incompleto:** la implementación técnica está disponible, pero FIND-001 sigue abierto por la evidencia pendiente de permiso/base revisada para redistribuir el corpus oficial. El origen y acceso público en la DNIT están verificados. El expediente permanece activo y no está listo para merge.

## Cambio SDD

- Change ID: `add-sifen-skill`.
- Expediente: `specs/changes/add-sifen-skill/`.
- `closure: active`; archivo documental pendiente.
- Proposal/Requirements, Design y Tasks revisión 2 aprobados.
- TASK-001 a TASK-004 completados; TASK-005 y TASK-006 bloqueados por FIND-001.
- REQ-001 y REQ-004 verificados; REQ-002/REQ-003 conservan las limitaciones de CHECK-002 registradas en las evaluaciones.

## Trazabilidad

Sin Story de Shortcut asociada. Rama: `codex/add-sifen-skill`. Commit y eventual squash: `feat: add SIFEN electronic documentation skill`.

## Riesgo y operación

La integración añade instrucciones, corpus y utilitarios; no introduce un servicio desplegado. Se preservan los bytes y hashes de las fuentes oficiales. El exportador comprueba todas las colisiones antes de escribir y requiere `--force` para sustituir archivos existentes. Rollback: revertir la nueva skill, sus pruebas, entradas del validador y enlaces de las guías juntos.

El repositorio de destino fue observado como **público** el 2026-11-18. Subir esta rama expondría también las copias del corpus. La publicación del PR queda pendiente hasta resolver la disposición de esos documentos; este archivo es una preparación local, no una publicación ni una autorización de redistribución.

## Validación

- [x] 194 pruebas técnicas: 131 de validadores, 48 de ejecución y 15 específicas de SIFEN.
- [x] Dos escenarios supervisados de revisión 2, con consultas reproducidas y fixtures sin cambios.
- [x] 74 archivos preservados y 35 entradas del manifiesto verificados; texto Apache-2.0 íntegro.
- [x] Aprobaciones SDD revisión 2 y evidencias vinculadas a los inputs actuales.
- [x] Standards resueltos, instrucciones y documentación alineadas; sin cambio arquitectónico que requiera ADR.
- [ ] `./scripts/validate/run.sh` completamente aprobado: las suites pasan, pero el contrato SDD falla por los escenarios/evidencias pendientes de FIND-001.
- [ ] Resolver CHECK-002/FIND-001 y completar TASK-005.
- [ ] Preparar archivo documental y ejecutar `--phase delivery --require-archive` antes de marcar listo para revisión.

Evidencia: `docs/validation/add-sifen-skill/r2/summary.md`, `review.md`, `official-source-verification.md`, `full-validation.txt` y `final-dossier-validation.txt`.

## Aprobaciones

Revisión gobernada por `.github/CODEOWNERS`. Apache-2.0 cubre únicamente el material de autoría autorizado por el desarrollador. La disponibilidad pública de las fuentes oficiales está verificada; su redistribución empaquetada aún requiere evidencia/base revisada. Sin merge, release ni migración de consumidores.
