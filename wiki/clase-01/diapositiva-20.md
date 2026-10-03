# Diapositiva 20 · La geometría del whitening

[Índice](README.md) · [Anterior](diapositiva-19.md) · [Siguiente](diapositiva-21.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

En dos dimensiones, estandarizar puede dejar una nube elíptica porque conserva correlación. Whitening produce covarianza identidad en los datos de ajuste bajo las condiciones de cálculo. Eso no garantiza que el conjunto futuro tenga igual covarianza ni que cada grupo sea esférico. Las coordenadas transformadas pueden mezclar variables originales y requieren interpretación.

## Historia 1: Área y ticket

Unidades grandes suelen costar más. Estandarizar área y precio deja una diagonal visible. Pricing analiza si necesita comparar tamaño y precio relativo por separado. Whitening reduce la duplicación global, pero luego debe traducir los grupos a m² y soles para que el equipo comercial los comprenda.

## Historia 2: Ingreso y capacidad

Ingreso declarado y cuota máxima se mueven juntos en un ejemplo de leads. El analista blanquea y observa una nube menos alargada. Revisa que la cuota no fuera calculada automáticamente a partir del ingreso. Si es una derivación exacta, eliminar la redundancia puede ser más claro que transformar.

## Historia 3: Cambió el mercado

Un whitening ajustado en el primer semestre se aplica al segundo. La nube vuelve a mostrar correlación porque cambiaron producto y demanda. El equipo mide desviación y decide si requiere revisión. Covarianza identidad durante el ajuste describe ese conjunto, sin prometer estabilidad eterna.

## Aplicación a tu trabajo

¿Puedes explicar un eje transformado en términos de tus variables originales?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Whitening: la geometría

Original: ingreso vs edad

Estandarizado: aún correlacionado

ZCA: Cov = I

Estandarizar iguala varianzas pero conserva la elipse; blanquear elimina la correlación: dos variables redundantes dejan de contar doble.

20/33

Estandarización → se igualan las varianzas, pero la correlación sigue → la elipse se estira, pero no se vuelve circular.

Estandarizado

ZCA Whitening

Whitening → la covarianza se convierte en identidad → la nube se vuelve esférica, sin correlación.

<details>
<summary>Notas del docente en el archivo original</summary>

Datos simulados con correlación 0.85; tras ZCA la covarianza muestral es exactamente la identidad. Con la estandarización sola, dos variables muy correlacionadas cuentan casi dos veces la misma información en la distancia euclidiana.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-19.md) · [Siguiente](diapositiva-21.md)
