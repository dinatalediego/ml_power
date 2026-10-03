# Diapositiva 30 · Efectos de lote y confusión

[Índice](README.md) · [Anterior](diapositiva-29.md) · [Siguiente](diapositiva-31.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Un efecto de lote agrega o multiplica variación por fuente o proceso. La clase ilustra ComBat y muestra ARI, una comparación con grupos conocidos en su simulación. Cygnus no dispone automáticamente de una verdad equivalente. Antes de corregir, se verifica solapamiento entre lote y fenómeno. Si todo un tipo de cliente pertenece a un solo lote, separarlos estadísticamente puede ser imposible sin supuestos adicionales.

## Historia 1: Cambio de unidad monetaria

Una carga registra presupuesto en miles de soles y otra en soles. Los grupos reflejan el lote. El analista corrige la unidad mediante una regla verificable, en vez de aplicar una corrección estadística a ciegas. Primero resuelve errores conocidos del proceso de captura.

## Historia 2: Dos formularios

Un formulario exige presupuesto y otro permite omitirlo. Tras imputar, el segundo lote queda más concentrado. El equipo compara características compartidas y revisa representación de ausencias. No atribuye el grupo resultante a conducta del comprador sin descartar diferencias de diseño.

## Historia 3: Feria y proyecto confundidos

Todos los leads de una feria consultaron un único proyecto. Una corrección que quite el efecto feria podría eliminar diferencias reales del producto. El analista reconoce la confusión y busca observaciones del mismo proyecto en otros canales. El muestreo puede ser más importante que la técnica de corrección.

## Aplicación a tu trabajo

¿Tienes el mismo tipo de cliente observado en varios lotes para separar sus efectos?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Efectos de lote: variación que no es del fenómeno

Color = grupo real; forma = lote. K-means (K = 2), ARI:

0.98

antes, con el lote

-0.00

antes, con el grupo

-0.00

después, con el lote

0.92

después, con el grupo

30/33

Aquí se ve que el valor observado mezcla el fenómeno real con el efecto del lote.

La corrección

Esta transformación elimina el efecto del lote (γ^ig) y ajusta la escala (δ^ig∗). Resultado: los datos corregidos reflejan mejor el fenómeno real, no las diferencias artificiales entre lotes.

Los números (ARI: Adjusted Rand Index)

La corrección eliminó el efecto de lote y recuperó la estructura verdadera

Puntos se agrupaban por lote

después de corregir

Puntos se agrupan por el grupo real

antes

<details>
<summary>Notas del docente en el archivo original</summary>

Modelo ComBat (Johnson, Li y Rabinovic, 2007): γ aditivo y δ multiplicativo del lote, estimados por Bayes empírico (se encogen hacia una media común). Ejemplos: Sentinel-2 frente a Landsat-8, campañas de encuesta con encuestadores distintos, sensores de distinto fabricante. Simulación: 400 observaciones, 6 variables, dos grupos balanceados entre dos lotes; antes de corregir, K-means encuentra el lote. Advertencia: si lote y grupo están confundidos (todo el grupo B en el lote 2), corregir el lote borra la señal: el diseño del muestreo importa más que el algoritmo.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-29.md) · [Siguiente](diapositiva-31.md)
