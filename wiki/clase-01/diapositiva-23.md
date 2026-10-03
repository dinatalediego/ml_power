# Diapositiva 23 · Estimar lambda sin mirar el futuro

[Índice](README.md) · [Anterior](diapositiva-22.md) · [Siguiente](diapositiva-24.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

La verosimilitud perfil de Box-Cox contiene −n/2·ln(σ̂²λ)+(λ−1)Σln(xi), salvo constantes. El segundo término corrige el cambio de escala. El λ≈−0,02 mostrado proviene de una simulación lognormal y no prescribe el parámetro para Cygnus. PowerTransformer aprende λ en fit y estandariza por defecto. Se ajusta únicamente con entrenamiento.

## Historia 1: El lambda del proyecto

El analista usa 800 presupuestos positivos de entrenamiento y estima λ=0,15 en un ejemplo. Mañana transforma otros 50 con ese mismo parámetro. No recalcula incluyendo los nuevos para evaluar rendimiento. Así sabe cómo funciona el modelo cuando recibe información realmente posterior.

## Historia 2: Copiar el menos 0,02

Pricing copia el λ de la clase para todas las áreas. Al revisar el catálogo, muchas unidades tienen distribución bastante simétrica. El analista estima o compara transformaciones en entrenamiento y verifica utilidad comercial. Un número didáctico ilustra una técnica, sin convertirse en regla del portafolio.

## Historia 3: Dos escalados consecutivos

El pipeline añade StandardScaler después de PowerTransformer con configuración por defecto. El analista comprueba que este último ya estandariza. Simplifica el proceso o establece standardize=False si desea una escala diferente después. Documentar cada paso evita transformaciones redundantes difíciles de interpretar.

## Aplicación a tu trabajo

¿Qué conjunto de datos aprendió tu lambda y cuándo se actualiza?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Elegir λ por máxima verosimilitud

Sumando el log-jacobiano sobre la muestra aparece (λ − 1) Σ ln xᵢ; maximizando en μ y σ² queda la verosimilitud perfil ℓ(λ).

λ̂ = -0.02 ≈ 0

ingreso simulado lognormal (n = 500): el logaritmo, como predice la teoría

23/33

<details>
<summary>Notas del docente en el archivo original</summary>

Sin el término (λ − 1) Σ ln xᵢ, las verosimilitudes con distintos λ estarían en escalas distintas y no serían comparables. En scikit-learn: PowerTransformer(method='box-cox'), que además estandariza por defecto. λ se estima solo con entrenamiento (bloque 6).

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-22.md) · [Siguiente](diapositiva-24.md)
