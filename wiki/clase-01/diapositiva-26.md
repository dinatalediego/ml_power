# Diapositiva 26 · Entrada al bloque de categorías

[Índice](README.md) · [Anterior](diapositiva-25.md) · [Siguiente](diapositiva-27.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Canal, distrito, proyecto y tipología necesitan una representación. Asignar códigos enteros a nombres crea distancias artificiales si se tratan como números. One-hot evita ese orden, pero dimensión y pesos siguen importando. En datos mixtos se elige una distancia o algoritmo compatible con numéricas y categorías.

## Historia 1: Distritos numerados

El equipo codifica Jesús María=1, Lince=2 y Miraflores=3. El algoritmo interpreta que el primero está dos veces más lejos del tercero que del segundo. El analista reemplaza esa codificación nominal. Si interesa distancia geográfica, utiliza una representación geográfica real y decide su peso.

## Historia 2: Canales distintos

Un lead viene de feria y otro de digital. One-hot representa la diferencia sin afirmar que feria está por encima o por debajo. Marketing pondera el canal junto a actividad. El objetivo es descubrir perfiles, evitando que el origen determine toda la segmentación por construcción.

## Historia 3: Tipología y tamaño

Un dúplex de 100 m² y un flat de 100 m² comparten área, pero pueden responder a preferencias diferentes. Pricing combina categoría y numéricas en una métrica apropiada. Decide cuánto debe pesar el tipo de producto al seleccionar comparables, en vez de confiar en un código arbitrario.

## Aplicación a tu trabajo

¿Qué columnas son nombres, cuáles son ordinales y cuáles son medidas?

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

26/33

<details>
<summary>Notas del docente en el archivo original</summary>

Bloque 5: ¿qué tan lejos está «Arequipa» de «Cusco»?

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-25.md) · [Siguiente](diapositiva-27.md)
