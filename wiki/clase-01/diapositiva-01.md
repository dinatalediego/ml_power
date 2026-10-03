# Diapositiva 01 · Preprocesamiento como parte del modelo

[Índice](README.md) · [Siguiente](diapositiva-02.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

La clase explica cómo construir la representación que usarán los algoritmos sin etiquetas. Agrupar leads, encontrar unidades comparables y detectar registros extraños son problemas diferentes. La selección de filas, variables y distancias determina qué patrones pueden aparecer. Esta clase prepara clustering y detección de anomalías. Un pronóstico de ventas requiere además definir horizonte, objetivo y validación temporal.

## Historia 1: Los leads que parecían iguales

Un analista agrupa 600 leads por presupuesto e interacciones. Encuentra tres grupos casi idénticos en actividad, pero separados por presupuesto. Al revisar las unidades, descubre que los soles dominaban la distancia. Decide escalar y repetir. Aprende que los segmentos dependen de cómo representa al cliente, antes de elegir K.

## Historia 2: Departamentos comparables

El equipo de pricing busca comparar 80 departamentos usando área, piso y precio por m². Si incluye además precio total sin revisar redundancia, el tamaño influye dos veces. El analista compara ambas representaciones y explica a gerencia por qué cambiaron los grupos. La selección de variables es una decisión comercial.

## Historia 3: Una anomalía útil

Una unidad de 180 m² aparece muy lejos de departamentos de 60 a 90 m². Operaciones confirma que es un dúplex válido. En vez de borrarlo, el analista lo conserva y lo compara con productos similares. El preprocesamiento debe distinguir calidad del dato de singularidad del producto.

## Aplicación a tu trabajo

¿Quieres que una fila represente un lead, una unidad o un proyecto por mes?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Maestría en Data Science

Unidad de Posgrado FIEECS-UNI

Preprocesamiento de datos
para aprendizaje no supervisado

Kevin Fernandez

Email: kevin.fernandez.m@uni.edu.pe

<details>
<summary>Notas del docente en el archivo original</summary>

Mensaje de apertura: en aprendizaje supervisado, un error de preprocesamiento lo delata el error de validación; en no supervisado nadie lo delata. Por eso esta clase trata el preprocesamiento como parte del modelo: cada decisión cambia la geometría en la que se agrupa o se reduce la dimensión.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Siguiente](diapositiva-02.md)
