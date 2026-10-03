# Diapositiva 09 · MICE y la incertidumbre

[Índice](README.md) · [Anterior](diapositiva-08.md) · [Siguiente](diapositiva-10.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

MICE ajusta modelos condicionales para completar cada variable usando las demás. Repite ciclos y genera varias bases con variación en los valores imputados. Las reglas de Rubin combinan estimaciones compatibles y su incertidumbre. Para clustering conviene comparar co-asignación: proporción de bases donde dos personas quedan juntas. Una única ejecución de IterativeImputer no equivale a analizar imputación múltiple.

## Historia 1: Cinco presupuestos posibles

Un lead tiene edad, área buscada y proyecto, pero no presupuesto. Cinco imputaciones producen S/ 440.000, 465.000, 480.000, 452.000 y 475.000. El analista agrupa cada base en vez de tratar un monto como verdad. Aprende cuánto cambia la segmentación por lo que todavía no conoce.

## Historia 2: Pareja estable

Dos leads quedan juntos en nueve de diez bases imputadas. Su co-asignación es 0,90. Otro par coincide en cuatro y obtiene 0,40. Comercial prioriza interpretar los patrones más estables. No compara números de clúster directamente porque las etiquetas pueden intercambiarse entre ejecuciones.

## Historia 3: Profesión y presupuesto

El modelo intenta imputar profesión como si fuera un número continuo. Produce valores sin significado. El analista revisa tipos y usa modelos compatibles con categorías o limita el procedimiento a numéricas. MICE exige decisiones por variable, no una aplicación automática a cualquier columna del CRM.

## Aplicación a tu trabajo

¿Tus segmentos seguirían existiendo con varias imputaciones plausibles?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

MICE: ecuaciones encadenadas

1

Inicializar los faltantes (media o muestreo).

2

Modelar cada variable con faltantes

3

Imputar con valores simulados

4

Repetir T ciclos; generar m bases con semillas distintas

Reglas de Rubin

En clustering: co-asignación

Cik ≈ 1: el par queda junto sin importar la imputación; en clustering nos dice si los grupos encontrados son estables o dependen demasiado de cómo se imputaron los faltantes.

9/33

Se ponen valores iniciales (media o aleatorios) solo para arrancar.

si falta ingreso, se ajusta un modelo de ingreso usando edad, educación, etc.

En lugar de poner la predicción exacta del modelo, se toma un valor aleatorio de la distribución.

Se repite el proceso varias veces (ciclos).
Cada vez los valores imputados se refinan porque los modelos se retroalimentan.

<details>
<summary>Notas del docente en el archivo original</summary>

van Buuren (2018). Se especifica un modelo condicional por variable sin una conjunta explícita. Muestrear de la predictiva evita volver a subestimar la varianza. Rubin combina la varianza dentro de cada imputación (Ū) y entre imputaciones (B, la incertidumbre por no haber observado). En no supervisado no hay un Q natural: se agrupa cada base imputada y se construye la matriz de co-asignación, que se puede agrupar por consenso. scikit-learn: IterativeImputer(sample_posterior=True, random_state=ℓ) para ℓ = 1..m.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-08.md) · [Siguiente](diapositiva-10.md)
