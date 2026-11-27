# Crear una issue en GitHub

[English](issue-creation.md) | [Português](issue-creation.pt.md) | [Español](issue-creation.es.md)

Use la Skill `github-issue-creation` para convertir una idea o un problema detectado en una issue completa de GitHub en un repositorio de `versat-labs`. Puede describirla en inglés, portugués o español; la issue siempre se escribe en inglés.

## Requisitos previos

- El Plugin del Harness instalado y el repositorio de destino en uso, con el remote `origin` en `versat-labs`.
- Acceso a GitHub desde su agente, mediante un servidor MCP de GitHub o el GitHub CLI autenticado con `gh auth login`.
- Permiso de push en el repositorio, necesario para establecer el campo de issue "Origin".
- En el GitHub CLI, el alcance `project` para agregar issues al proyecto "Portfolio" de la organización: `gh auth refresh -s project`.
- Python con PyYAML, según el `requirements-validation.txt` del Harness.

## Pruébelo

```text
Use $github-issue-creation para abrir una issue: la exportación del informe mensual a CSV falla por timeout cuando tiene más de 10.000 filas. Debería terminar en menos de un minuto.
```

## Qué sucede

1. La Skill lee los formularios de issue del propio repositorio, o los predeterminados de la organización en `versat-labs/.github`: Bug report, Feature request y Chore.
2. Elige el formulario. Si su intención corresponde a más de uno, pregunta cuál desea.
3. Redacta el título y los campos en inglés, y conserva el código, los comandos y las salidas de error exactamente como los escribió.
4. Pide, en un solo mensaje, cualquier campo obligatorio que no pudo completar, como los pasos de reproducción de un bug o la persona de una feature.
5. Pregunta el "Origin", salvo que ya lo haya indicado: **Internal Idea**, para un codeowner o miembro del equipo Versat; **External suggestion**, para un colaborador externo, cliente o socio; o **VIP Customer feature request**, para un cliente VIP que paga por el desarrollo.
6. Muestra una vista previa con el repositorio, el formulario, el título, el cuerpo, el tipo, el Origin y el proyecto "Portfolio". No se crea nada hasta que usted confirme. Las issues de un repositorio público son públicas; quite nombres de clientes u otros datos sensibles antes de confirmar.
7. Crea la issue, establece el tipo y el Origin, la agrega a "Portfolio" e informa el enlace y el resultado de cada paso.

## Resultados y fallos

La Skill informa solo lo que GitHub confirmó. Cuando falla un paso posterior a la creación, como la falta del alcance `project`, recibe el enlace de la issue e instrucciones para completar ese paso en la barra lateral de la issue. Cuando falla la propia creación, no existe ninguna issue y la Skill indica el requisito previo que falta. Nunca reintenta la creación por su cuenta, para evitar duplicados.

La Skill no adjunta archivos. Agregue capturas de pantalla en GitHub después de la creación.

## Vulnerabilidades de seguridad

No informe una posible vulnerabilidad como issue. Cuando su descripción parezca una, la Skill no crea nada y le indica la ruta privada de las [indicaciones para reportes de seguridad](https://github.com/versat-labs/.github/blob/main/SECURITY.es.md):

- En un repositorio público, use **Security → Report a vulnerability**.
- En un repositorio privado, envíe un correo a los CODEOWNERS correspondientes por los canales internos existentes de Versat.
- Cuando la ruta no esté disponible, pida instrucciones privadas a un maintainer sin compartir detalles.
