# Diapositiva 04 · Entrada al bloque de faltantes

[Índice](README.md) · [Anterior](diapositiva-03.md) · [Siguiente](diapositiva-05.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Esta diapositiva marca el inicio del estudio de ausencias. El primer paso es distinguir un valor desconocido de un cero real y de un campo que no aplica. Después se mide la ausencia por variable, proyecto, canal y fecha. La forma de completar un valor debe ser coherente con por qué falta.

## Historia 1: Cero visitas

Un lead creado hoy tiene cero visitas registradas. Otro tiene visitas desconocidas por una migración incompleta. El analista evita reemplazar ambos con cero. Mantiene el primero como conteo real y marca el segundo como ausencia. Así el modelo no confunde falta de actividad con falta de registro.

## Historia 2: Área libre

Un flat interior tiene área libre cero y una unidad recién cargada tiene área libre vacía. Pricing verifica el plano antes de calcular indicadores. La diferencia importa: rellenar la segunda con cero puede sobreestimar el área techada implícita o alterar el precio comparable.

## Historia 3: Fecha de minuta

Un lead sin minuta todavía no ha llegado a ese evento. Una venta antigua puede tener la fecha pendiente de carga. El equipo distingue situación comercial y calidad de información. No imputa una fecha promedio de minuta a leads abiertos para fabricar duraciones que nunca ocurrieron.

## Aplicación a tu trabajo

¿Cuáles de tus vacíos significan desconocido y cuáles significan que el evento no ocurrió?

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

4/33

<details>
<summary>Notas del docente en el archivo original</summary>

Bloque 1: ¿qué hacemos con lo que no vimos… y por qué no lo vimos?

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-03.md) · [Siguiente](diapositiva-05.md)
