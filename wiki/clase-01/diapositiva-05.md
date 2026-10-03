# Diapositiva 05 · MCAR, MAR y MNAR

[Índice](README.md) · [Anterior](diapositiva-04.md) · [Siguiente](diapositiva-06.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

MCAR: faltar es independiente de los valores observados y ausentes. MAR: la ausencia puede explicarse por variables observadas. MNAR: depende de información no observada, incluido el propio valor faltante. Son supuestos sobre el mecanismo, no etiquetas que se deducen solo de un porcentaje. MAR y MNAR no se distinguen con certeza usando únicamente lo observado. La ignorabilidad estadística requiere también condiciones sobre los parámetros del mecanismo.

## Historia 1: Una pérdida aleatoria

Un fallo elimina el campo presupuesto de 50 formularios elegidos al azar entre 1.000. Si la selección fue realmente independiente del contenido, MCAR es plausible. El analista compara distribuciones y registros técnicos. Una caída ocurrida solo durante una campaña concreta ya no respalda ese mismo supuesto.

## Historia 2: El formulario móvil

Los leads de celular omiten presupuesto en 40 % de los casos y los de escritorio en 10 %. Si el dispositivo está registrado y explica la ausencia, MAR es una hipótesis de trabajo. El analista incorpora dispositivo y canal al modelo de imputación y revisa si queda un patrón sin explicar.

## Historia 3: El comprador reservado

Algunos compradores con mayor ingreso prefieren no declararlo. Aunque el CRM guarde edad y distrito, la ausencia podría seguir dependiendo del ingreso desconocido. El equipo trata MNAR como posibilidad, compara escenarios y evita afirmar que quienes callan tienen necesariamente ingresos altos.

## Aplicación a tu trabajo

¿Qué evidencia del formulario o del proceso respalda tu supuesto de ausencia?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Tres mecanismos de ausencia (Rubin, 1976)

MCAR

La ausencia no depende de ningún valor.

Ej.: un sensor de PM2.5 se apaga por cortes eléctricos al azar.

MAR

Depende solo de lo observado.

Ej.: los jóvenes omiten más su ingreso y la edad sí se registra.

MNAR

Depende del propio valor que falta.

Ej.: quienes ganan más son los que no declaran su ingreso.

Bajo MAR el mecanismo es ignorable: basta modelar los datos. MAR frente a MNAR no se puede probar con lo observado: se argumenta con el dominio.

5/33

<details>
<summary>Notas del docente en el archivo original</summary>

R es la matriz indicadora de ausencia; en la notación completa aparece un parámetro φ del mecanismo. Si el mecanismo es MAR y φ es distinto de θ, la verosimilitud de θ se obtiene integrando los faltantes y R se ignora. Existe el test de Little para MCAR, pero ningún test separa MAR de MNAR: los valores que lo decidirían son justamente los que faltan. Interpretación práctica: el método de imputación es un supuesto sobre el mecanismo.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-04.md) · [Siguiente](diapositiva-06.md)
