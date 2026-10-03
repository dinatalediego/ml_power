# Diapositiva 19 · Whitening y Mahalanobis

[Índice](README.md) · [Anterior](diapositiva-18.md) · [Siguiente](diapositiva-20.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Si z=W(x−μ) y WΣWᵀ=I, la distancia euclidiana transformada satisface ||W(x−y)||²=(x−y)ᵀΣ⁻¹(x−y), para una covarianza invertible. Whitening transforma covarianza, mientras estandarizar solo modifica varianzas. Autovalores pequeños pueden amplificar ruido. La covarianza global incluye diferencias entre grupos y reducirlas puede debilitar segmentos válidos.

## Historia 1: Precio repetido

Precio total y monto financiado están fuertemente correlacionados. Un clustering cuenta dos veces diferencias similares. El analista prueba whitening y compara con eliminar una variable. Evalúa si los grupos resultantes siguen teniendo sentido para comercial. Una transformación compleja no sustituye revisar qué información necesita el modelo.

## Historia 2: Dos mercados legítimos

Un portafolio tiene vivienda familiar y departamentos de inversión. La mayor varianza viene de la diferencia entre ambos. Whitening reduce el peso de esa dirección y puede acercarlos. El equipo compara perfiles antes y después para no borrar una separación que explica estrategias comerciales distintas.

## Historia 3: Una columna casi duplicada

Dos indicadores de área coinciden casi exactamente. La covarianza tiene un autovalor cercano a cero y su inversa amplifica pequeñas diferencias de carga. El analista elimina redundancia o regulariza. Una diferencia de centímetros no debe convertirse en la característica más influyente de los comparables.

## Aplicación a tu trabajo

¿La correlación representa redundancia o una separación útil para el negocio?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Whitening es Mahalanobis

PROPOSICIÓN 2

Demostración

1

Definición de blanqueo: la nube resultante es esférica.

2

Invertir la identidad: W es una «raíz cuadrada» de Σ⁻¹.

3

Sustituir en la norma euclidiana del vector blanqueado.

Ojo: Σ total incluye la separación entre grupos; blanquear puede encoger justo la dirección que separa los clústeres.

19/33

<details>
<summary>Notas del docente en el archivo original</summary>

Vale para cualquier W con WΣWᵀ = I: PCA-whitening (Λ^(−1/2)Uᵀ) o ZCA (UΛ^(−1/2)Uᵀ, el blanqueo más parecido a x). Consecuencia: K-means sobre datos blanqueados es K-means con distancia de Mahalanobis global. Advertencia: la Σ total incluye la separación entre grupos; el autovalor de la dirección que separa los clústeres es grande precisamente por esa separación, y blanquear lo encoge. Si algún λ ≈ 0, Λ^(−1/2) amplifica ruido: se regulariza con (Λ + εI)^(−1/2).

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-18.md) · [Siguiente](diapositiva-20.md)
