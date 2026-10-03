# Diapositiva 18 · Z-score, min-max y escalado robusto

[Índice](README.md) · [Anterior](diapositiva-17.md) · [Siguiente](diapositiva-19.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

StandardScaler utiliza media y desviación. MinMaxScaler usa extremos observados. RobustScaler centra con mediana y escala con IQR. Los dos primeros pueden comprimir el núcleo cuando hay extremos. El robusto conserva mejor ese núcleo, sin limitar valores ni eliminar anomalías. Los cocientes 0,24, 0,13 y 0,99 de la diapositiva corresponden a su simulación, no a garantías universales.

## Historia 1: El presupuesto millonario

Casi todos los presupuestos están entre S/ 350.000 y 700.000, salvo uno de S/ 8 millones. Min-max comprime la mayoría en una franja pequeña. El analista compara escalado robusto y revisa al extremo. Conserva variación entre compradores habituales sin afirmar que el inversionista sea inválido.

## Historia 2: Descuento muy inusual

Los descuentos habituales están entre 8 % y 15 %, pero una carga indica 90 %. StandardScaler usa una desviación inflada. Pricing verifica ese dato y contrasta escalas. Un método robusto ayuda a la exploración, mientras corregir un error confirmado evita que siga afectando otros reportes.

## Historia 3: Un nuevo valor excede uno

MinMaxScaler se ajusta con presupuestos de S/ 300.000 a 900.000. Mañana llega uno de S/ 1.000.000 y obtiene 1,167. El equipo entiende que transform no garantiza [0,1] para valores fuera del rango de ajuste, salvo configuración de recorte. El dato nuevo informa cambio de distribución.

## Aplicación a tu trabajo

¿Tus extremos cambian demasiado la escala del cliente habitual?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Cuatro escaladores, cuatro supuestos

0.24

IQR(ingreso)/IQR(edad) tras estandarizar

0.13

… tras min-max

0.99

… tras escalado robusto

18/33

Estandarización (Z-score)

Min-Max scaling:

Escalado robusto (mediana + IQR)

Whitening / decorrelación

Relación entre ingreso y edad según el método

con robusto se logra casi equilibrio (0.99), mientras que con los otros métodos se pierde balance

Min-Max

Z-score

Robusto

<details>
<summary>Notas del docente en el archivo original</summary>

Simulación: 300 clientes con ingreso ∼ N(2500, 600²) y edad ∼ N(40, 10²), más 3 ingresos atípicos de 24 a 30 mil. Lo deseable: núcleos con dispersión comparable (cociente ≈ 1). Con estandarización, σ̂ del ingreso se infla por los atípicos y su núcleo queda 4 veces más angosto que el de la edad; con min-max, 7 veces: la edad domina la distancia sin que nadie lo decida. El escalado robusto conserva el balance y deja los atípicos lejos, donde un detector los encuentra. Interpretación: escalar es elegir pesos.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-17.md) · [Siguiente](diapositiva-19.md)
