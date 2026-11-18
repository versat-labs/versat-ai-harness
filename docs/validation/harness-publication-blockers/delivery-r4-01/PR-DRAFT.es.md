# Preparar Harness 0.4.0 con licencia Apache y publicación protegida

Aplica en la rama de entrega la licencia Apache-2.0 y los avisos ya aprobados, con el parche exacto de nueve archivos. Actualiza las guías EN/PT/ES y conserva a Elvis y Everton como CODEOWNERS generales, con una aprobación de quien no abrió la PR y triaje compartido. Simplifica la evidencia de publicación conforme a R4 sin repetir decisiones ya aceptadas.

El dossier `harness-publication-blockers` se prepara para archivo documental en esta entrega. La evidencia de validación final se registra en `docs/validation/harness-publication-blockers/delivery-r4-01/`; la preservación de evidencias privadas y las decisiones anteriores mantienen su alcance. No se cambian los textos jurídicos aprobados ni los registros históricos.

Autor previsto: Everton, mediante su propia cuenta. Revisor: Elvis, conforme al CODEOWNERS de la rama base. No existe Story Shortcut asociado. Mensaje de commit propuesto: `chore: prepare Apache Harness candidate for private review`.

Esta entrega no cambia visibilidad, protección de main, permisos ni canales; no publica versión o etiqueta ni migra consumidores. La referencia local v0.4.0 del catálogo no debe activarse antes de existir y verificarse la release exacta. Tras integración y CI privados, se requiere revisión del delta de exposición; la apertura y protección inmediata, pruebas públicas y eventual release conservan autorización separada.

Validación observada: suite local completa, 179 pruebas aprobadas (131 + 48), paquete válido y entrega SDD previa al archivo aprobada. El resultado final del guard de archivo se conserva en esta carpeta; comprobarlo antes de enviar la PR. El dossier único está en `specs/archive/harness-publication-blockers/`, con `closure: prepared`. El archivo no demuestra merge ni ejecución de CI remoto.

Resultado final observado: entrega seleccionada con `--require-archive` y guard con baseline local `4a56181d3597c5d345a7639f013547e1700420cb` aprobados; 10 checks, 31 escenarios locales y 40 obligaciones retenidas, sin resultados obsoletos. Los controles reales de GitHub siguen sin ejecutar.
