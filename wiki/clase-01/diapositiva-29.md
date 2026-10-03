# Diapositiva 29 · Entrada al bloque de lotes y fuga

[Índice](README.md) · [Anterior](diapositiva-28.md) · [Siguiente](diapositiva-30.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

La última transición pregunta si el modelo aprende el fenómeno comercial o cómo se recolectaron los datos. Un lote puede ser fuente, campaña, versión de formulario o migración. Además, cualquier transformación ajustada con información futura puede contaminar evaluación. El diseño del conjunto de entrenamiento forma parte del problema.

## Historia 1: La migración forma un segmento

Los leads migrados tienen diez campos vacíos y los nuevos están completos. El modelo crea dos grupos que coinciden con fecha de migración. El analista cruza origen y calidad antes de describir perfiles de compradores. La diferencia principal proviene del registro, no necesariamente del cliente.

## Historia 2: Unidades duplicadas

Un departamento aparece en una fuente interna y en una importación. Una copia queda en entrenamiento y otra en prueba. El equipo agrupa por identidad de unidad antes de separar. Así evita medir generalización sobre datos que son versiones casi idénticas de lo ya conocido.

## Historia 3: El futuro en una ventana

Para describir leads al día 15, el analista usa interacciones de todo el mes. El perfil incluye acciones posteriores a la fecha de decisión. Reconstruye variables hasta el corte. Una segmentación operativa debe usar lo que realmente estaba disponible al momento de aplicarla.

## Aplicación a tu trabajo

¿Qué diferencias de captura podrían explicar tus grupos mejor que el negocio?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Contenido

▶

Datos faltantes

▶

Atípicos: Isolation Forest y LOF

▶

Escalado y whitening

▶

Transformaciones de potencia: Box-Cox y Yeo-Johnson

▶

Variables categóricas y datos mixtos

▶

Efectos de lote, data leakage y pipeline

29/33

<details>
<summary>Notas del docente en el archivo original</summary>

Bloque 6: cuando el clúster que encuentras es… el laboratorio, el sensor o el mes.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-28.md) · [Siguiente](diapositiva-30.md)
