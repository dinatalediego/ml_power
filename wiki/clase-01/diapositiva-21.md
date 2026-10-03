# Diapositiva 21 · Entrada al bloque de transformaciones

[Índice](README.md) · [Anterior](diapositiva-20.md) · [Siguiente](diapositiva-22.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Transformar la forma de una distribución y ajustar su escala son decisiones diferentes. Una cola larga puede dominar covarianzas aun después de escalar. Logaritmos y familias de potencia cambian distancias relativas. Antes de transformar se revisa si la cola o la multimodalidad representa comportamiento válido que interesa conservar.

## Historia 1: Muchos contactos, pocos muy activos

La mayoría de leads tiene entre una y diez interacciones, y unos pocos superan cien. El analista explora log1p antes de escalar. Así diferencias entre uno y cinco contactos pueden ser más visibles que pequeñas diferencias entre 100 y 104. Decide si esa interpretación coincide con el proceso comercial.

## Historia 2: Dos tamaños de vivienda

Las áreas se concentran alrededor de 55 y 100 m² porque hay dos familias de producto. El analista evita transformar con la meta de obtener una sola campana. La bimodalidad puede ser precisamente la estructura que pricing necesita distinguir. Primero interpreta el catálogo.

## Historia 3: Variación de absorción

El cambio mensual de ventas tiene meses negativos, cero y positivos. Box-Cox no admite todos esos valores. El equipo considera Yeo-Johnson y conserva también el indicador original para explicarlo. Una transformación válida debe respetar el dominio de la variable.

## Aplicación a tu trabajo

¿Tu asimetría es un problema de representación o una característica que quieres conservar?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Contenido

▶

Datos faltantes

▶

Atípicos: Isolation Forest y LOF

▶

Escalado y whitening

▶

Transformaciones de potencia: Box-Cox y Yeo-Johnson

▶

Variables categóricas y datos mixtos

▶

Efectos de lote, data leakage y pipeline

21/33

<details>
<summary>Notas del docente en el archivo original</summary>

Bloque 4: corregir la forma de las distribuciones.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-20.md) · [Siguiente](diapositiva-22.md)
