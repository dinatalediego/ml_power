# Diapositiva 07 · La media atenúa la correlación

[Índice](README.md) · [Anterior](diapositiva-06.md) · [Siguiente](diapositiva-08.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Si solo X tiene una fracción π de ausencias MCAR y se imputa con su media, aproximadamente Var(X imputada)=(1−π)Var(X) y Cov(X imputada,Y)=(1−π)Cov(X,Y). Por ello ρ imputada≈√(1−π)ρ. La fórmula gráfica y las notas coinciden. El texto del paso 3 menciona 1−π y debe leerse con esta corrección. Si ambas variables faltan, el resultado depende de sus mecanismos y patrones conjuntos.

## Historia 1: Presupuesto y área buscada

Presupuesto y área deseada tienen correlación 0,80 en un ejemplo. Falta presupuesto en 25 % de los leads bajo MCAR. Al imputar la media, la correlación esperada cae a √0,75×0,80≈0,693. El analista no presenta esa caída como cambio de preferencia del comprador: es un efecto de preparación.

## Historia 2: El segmento del promedio

De 300 leads, 90 reciben exactamente S/ 500.000 porque falta presupuesto. K-means encuentra un grupo alrededor de ese valor. Comercial cree que hay una demanda concentrada en ese ticket. El analista cruza el grupo con el indicador de imputación y descubre una concentración artificial.

## Historia 3: Más filas no corrigen el sesgo

El equipo incorpora otros 5.000 leads manteniendo 25 % de imputación por media. La correlación se estima con mayor precisión, pero conserva la atenuación. Decide contrastar KNN e imputación múltiple. El tamaño de la muestra reduce incertidumbre, sin arreglar automáticamente una representación distorsionada.

## Aplicación a tu trabajo

¿Una concentración de valores podría deberse a tu regla de imputación?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Imputar con la media encoge la correlación

PROPOSICIÓN 1

Demostración

1

Los nπ valores imputados están en la media: no suman nada al cálculo de la varianza.

2

tanto la variabilidad individual como la relación conjunta se achican en la misma proporción

3

la correlación se reduce en un factor 1−π. Cuantos más faltantes (π), más se encoge.

Esto significa que aunque recuperemos el tamaño del dataset, perdemos la fuerza de las relaciones.

7/33

imputar con la media reduce la correlación entre variables.

π: proporción de valores faltantes en la variable

<details>
<summary>Notas del docente en el archivo original</summary>

Simulación con n = 240, π = 0.33 y MCAR: la correlación pasa de 0.79 a 0.65; la fórmula predice √(1−π)·ρ = 0.65. El sesgo no depende del tamaño muestral: más datos no lo corrigen. En clustering el efecto se ve geométricamente: los imputados se apilan en una recta y forman un micro-cúmulo artificial en el centro. La mediana tiene el mismo problema.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-06.md) · [Siguiente](diapositiva-08.md)
