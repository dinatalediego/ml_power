# Diapositiva 22 · Box-Cox y su jacobiano

[Índice](README.md) · [Anterior](diapositiva-21.md) · [Siguiente](diapositiva-23.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Para x>0, Box-Cox es (x^λ−1)/λ si λ≠0 y ln(x) si λ=0. Con λ=1 resulta x−1, equivalente a identidad salvo un desplazamiento. El jacobiano es x^(λ−1), que permite comparar verosimilitudes en la escala original. La transformación es monótona, pero cambia diferencias y distancias. No admite ceros ni negativos.

## Historia 1: Presupuestos con cola derecha

Los presupuestos positivos son S/ 300.000, 450.000, 700.000 y 1.800.000. El analista prueba una potencia cercana al logaritmo y observa menor predominio del último caso. Comercial interpreta diferencias relativas entre tickets. Mantiene soles originales para describir cada grupo y no convierte el resultado en un precio nuevo.

## Historia 2: Conteos con cero

Un lead tiene cero proformas. El analista intenta Box-Cox y el procedimiento rechaza el dato. Comprueba que cero es válido y elige otra transformación, como log1p o Yeo-Johnson. Añadir una constante arbitraria cambia la geometría, por lo que debe justificarse y documentarse.

## Historia 3: El parámetro engañoso

El equipo compara λ usando solo la varianza de los valores transformados. Algunas potencias parecen mejores por comprimir más la escala. El analista incorpora el jacobiano en la verosimilitud o usa una implementación adecuada. Comprimir números no equivale a mejorar el ajuste estadístico.

## Aplicación a tu trabajo

¿Todos los valores son estrictamente positivos y qué significa comprimir su cola?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Box-Cox: una familia contra la asimetría

El jacobiano x^(λ−1) es la pieza que hace comparables las verosimilitudes entre distintos λ.
permite estimar el mejor λ usando máxima verosimilitud.

22/33

Fórmula de Box-Cox

El Jacobiano

λ=1: no transforma nada (identidad).
λ=0: se convierte en logaritmo.
λ<1: comprime la cola derecha (reduce sesgo positivo).
λ>1: expande valores grandes.

Es una familia continua: cuando λ→0, la fórmula converge suavemente al logaritmo.

<details>
<summary>Notas del docente en el archivo original</summary>

Box y Cox (1964). Si Y = ψ_λ(X) es gaussiana, la densidad de X incluye el factor |dψ/dx| = x^(λ−1). Por qué importa en no supervisado: K-means favorece clústeres esféricos, GMM asume componentes gaussianas y PCA se basa en covarianzas sensibles a colas pesadas. Una variable muy asimétrica (ingresos, áreas, conteos) produce un núcleo aplastado y una cola que K-means parte en clústeres artificiales. Exige x > 0.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-21.md) · [Siguiente](diapositiva-23.md)
