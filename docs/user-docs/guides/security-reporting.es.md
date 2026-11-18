# Comunicar un problema de seguridad de forma segura

[English](security-reporting.md) | [Português](security-reporting.pt.md) | [Español](security-reporting.es.md)

La ruta pública de reporte del Harness está **sin verificar**. La ruta prevista es GitHub Private Vulnerability Reporting de este repositorio, sujeta a disponibilidad y verificación para el público previsto. Esta preparación no envió reportes ni activó canales.

Las observaciones anteriores de H02 cubrieron otro piloto público y una recepción interna del Harness. Son evidencia histórica y no establecen una ruta pública del Harness. @elviszoz y @evertonspohrversat comparten monitoreo, triaje y coordinación; Elvis mantiene la coordinación responsable. Cualquiera puede atender un reporte. Registre un responsable efectivo y un traspaso de atención explícitamente reconocido si esa persona no está disponible; no se requieren dos respuestas. La asignación y CODEOWNERS no configuran notificaciones ni demuestran acceso o recepción. El responsable confirmó la participación de ambos en el triaje compartido y en las pruebas futuras. La recepción pública sigue sin verificar. Un traspaso real se registra cuando sea necesario; no exige una simulación separada antes de publicar.

La política de revisión exige una aprobación de CODEOWNER elegible que no sea autor de la PR; es independiente del triaje de seguridad. La aprobación del propio autor no satisface el requisito, y la responsabilidad compartida no exige dos aprobaciones. La rama base efectiva determina la elegibilidad; consulte la [transición de responsables](../../handoffs/harness-publication-blockers/transition.md#general-ownership-and-base-branch-transition).

En la secuencia aprobada en GitHub Free, la preparación privada confirma responsables, destinatarios reales y la alternativa segura. La activación del PVR nativo y la prueba externa de envío, recepción y exclusión de acceso ocurren solamente después de visibilidad pública autorizada por separado y controles verificados. Un 404 en estado privado no exige activación privada de pago ni demuestra una ruta pública de reporte. Consulte la [transición delimitada](../../handoffs/harness-publication-blockers/transition.md).

## Antes de compartir detalles

Lea las instrucciones reales de seguridad del destino. Confirme destino confidencial, reportantes previstos, destinatarios permitidos y tratamiento de datos antes de enviar información sensible. No publique detalles de explotación, credenciales, información de clientes ni adjuntos sensibles en issues comunes. Una sesión administrativa o URL funcional no demuestra acceso externo ni confidencialidad.

## Cuando la ruta no esté disponible

Use un contacto de mantenedor ya visible solamente para pedir, sin detalles sensibles: “Necesito instrucciones confidenciales para reportar un problema de seguridad en este repositorio.” Espere una ruta apropiada y verificada. Ante acceso denegado o cambio de destino, deténgase y solicite instrucciones actualizadas. Mantenga el reporte privado si no existe una ruta adecuada. El ejemplo no envía mensajes ni autoriza a un agente a hacerlo.

Resultado esperado: instrucciones seguras o una brecha explícita de verificación, sin presumir recepción. Aquí no se proporciona correo interno, endpoint nuevo, plazo de respuesta ni período de retención.

## Verificación del mantenedor

Para la prueba pública posterior, autorizada por separado, use un reporte identificado y no sensible de un reportante del público previsto. Verifique el acceso aplicable de Elvis y Everton mediante evidencia de configuración o acceso al servicio. Observe la recepción real por un responsable efectivo y el acceso denegado a una persona no autorizada. No se requieren notificaciones o respuestas duplicadas ni un traspaso simulado. Una falla real de acceso o recepción sigue pendiente; registre un traspaso real cuando sea necesario. No infiera entrega de notificaciones por la asignación, envíe otro reporte automáticamente ni use credenciales ajenas. Mantenga identificadores y contenido restringidos. Verifique nuevamente tras cambios de visibilidad o público; nunca use vulnerabilidades reales en esta prueba.

Controles, activación de canales, permisos y mensajes requieren autorización específica. Una alternativa documental no completa la verificación de la ruta. Cada producto verifica su alcance. Consulte [Security](../../../standards/core/security.md), [resolución actual de pendientes](../../handoffs/harness-publication-blockers/README.md) y [contribución](contributing.es.md).

[Quickstart](../quickstart.es.md) · [Harness](../../../README.es.md)
