# Diapositiva 08 · KNN para imputar con vecinos

[Índice](README.md) · [Anterior](diapositiva-07.md) · [Siguiente](diapositiva-09.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

KNNImputer utiliza vecinos con información compartida. La distancia nan_euclidean reescala la suma de diferencias cuadradas por p/|Oab| y luego toma su raíz. Aquí p significa número total de variables, no proporción de ausencias. Los vecinos promedian el campo faltante, con pesos uniformes o por distancia. La escala debe ajustarse con entrenamiento antes de buscar vecinos. La alta dimensión y pocos campos compartidos reducen la calidad.

## Historia 1: Un presupuesto parecido

A un lead le falta presupuesto, pero busca dos dormitorios y 70 m² en un proyecto. Tres vecinos comparables declaran S/ 450.000, S/ 470.000 y S/ 490.000. Con pesos uniformes se imputa S/ 470.000. El analista contrasta el resultado con la media global de S/ 620.000 y conserva una bandera de imputación.

## Historia 2: Vecinos elegidos por soles

El analista utiliza presupuesto para imputar área deseada, junto con visitas y edad. Sin escalar, los soles deciden casi todos los vecinos. Ajusta una escala en entrenamiento que admita NaN, transforma, imputa y revisa ejemplos concretos. La vecindad debe reflejar afinidad comercial, no solo unidades de medida.

## Historia 3: Muy poca coincidencia

Dos leads comparten únicamente edad entre diez variables. La distancia corrige por diez, pero se apoya en una sola observación compartida. El equipo evita confiar ciegamente en ese vecino, mide solapamiento y compara con una regla más sencilla. La corrección matemática no crea información ausente.

## Aplicación a tu trabajo

¿Qué campos disponibles hacen que dos de tus leads sean vecinos útiles?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

KNN: imputar mirando a los vecinos

Oab: son las variables observadas en ambas filas. El factor p/|Oab| hace comparables distancias calculadas con distinto número de variables.

5.00

valor real

5.13

KNN

3.38

media

8/33

<details>
<summary>Notas del docente en el archivo original</summary>

KNNImputer usa la distancia nan_euclidean y promedia la variable faltante entre los K vecinos que la tienen observada, con pesos uniformes o inversos a la distancia. Respeta relaciones no lineales y multimodalidad: en la curva senoidal la media global queda lejos del valor real. Límites: escalar antes (si no, la variable de mayor varianza decide quiénes son vecinos), costo O(n²p), y en alta dimensión las distancias se concentran.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-07.md) · [Siguiente](diapositiva-09.md)
