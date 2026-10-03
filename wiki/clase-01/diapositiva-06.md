# Diapositiva 06 · El costo de eliminar filas

[Índice](README.md) · [Anterior](diapositiva-05.md) · [Siguiente](diapositiva-07.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Con ausencia independiente por celda de probabilidad p y d variables, la proporción esperada de filas completas es (1−p)^d. Con p=0,05 y d=20 queda aproximadamente 35,85 %. Ese cálculo exige independencia. El análisis de casos completos puede sesgar una segmentación si la ausencia selecciona tipos de clientes. Calcular covarianzas por pares también puede producir una matriz incompatible con PCA.

## Historia 1: Los mil leads se reducen

El equipo dispone de 1.000 leads y 20 campos con 5 % de vacíos independientes. Al exigir filas completas espera conservar unos 358. El analista muestra la pérdida antes de entrenar. Decide usar solo las variables necesarias y comparar imputación con eliminación para conservar cobertura.

## Historia 2: La feria desaparece

En una feria se capturó celular y proyecto, pero pocas veces profesión. Al eliminar filas incompletas, casi todos esos leads desaparecen. Marketing interpreta erróneamente que el segmento de feria es pequeño. El analista reporta retención por canal y cambia el tratamiento de profesión.

## Historia 3: Una matriz imposible

Para analizar unidades, el equipo calcula cada correlación usando los registros disponibles en cada par. Los pares representan poblaciones distintas y PCA recibe una matriz con autovalores negativos. El analista vuelve a construir una base coherente e imputa o limita variables antes de calcular la covarianza.

## Aplicación a tu trabajo

¿Qué proporción de leads de cada canal sobreviviría a dropna()?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Eliminar filas: barato hoy, caro mañana

Listwise (casos completos)

Sin sesgo solo bajo MCAR. Se eliminan todas las filas que tengan al menos un dato faltante.

Pairwise

Cada covarianza se calcula con los pares de variables disponibles: la matriz puede no ser semidefinida positiva y romper PCA o Mahalanobis.

6/33

p: proporción de datos faltantes por variable.

d: número de variables en el dataset.

<details>
<summary>Notas del docente en el archivo original</summary>

Si cada celda falta con probabilidad p de forma independiente, una fila de d variables está completa con probabilidad (1 − p)^d. Con 5 % de faltantes por variable y 20 variables, se conserva el 36 % de las filas: se descarta casi dos tercios del esfuerzo de recolección. Regla razonable: eliminar solo si p·d es pequeño y hay evidencia de MCAR.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-05.md) · [Siguiente](diapositiva-07.md)
