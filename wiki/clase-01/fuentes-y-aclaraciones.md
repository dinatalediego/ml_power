# Fuentes, precisiones y conexión con Medallio

[Volver al índice](README.md)

## Material principal

Archivo aportado por el usuario: **Preprocesamiento de datos para aprendizaje no supervisado.pptx**, 33 diapositivas. Kevin Fernandez, Maestría en Data Science, Unidad de Posgrado FIEECS-UNI. Se revisaron texto editable, tablas y notas. Se inspeccionaron también las fórmulas gráficas de la diapositiva 7 y el aporte de varianza de la diapositiva 3. La transcripción no sustituye las figuras del original.

## Naturaleza de las historias

Todas las cantidades, clientes y situaciones numéricas de las 99 historias son sintéticos. El contexto corresponde al rubro inmobiliario y al trabajo con leads, proformas, unidades, separaciones, minutas, pricing y stock. No se consultó Redshift ni Medallio. Los ejemplos no demuestran una incidencia real ni una recomendación de precios para un proyecto.

## Precisiones al leer la clase

| Slide | Precisión |
| --- | --- |
| 3 | Con las dos variables del ejemplo, estandarizar da 50 % de aporte esperado a cada una. La nota que menciona 25 % necesitaría cuatro variables equivalentes. |
| 5–6 | MCAR justifica casos completos para representar la distribución conjunta sin selección por valores. Otros objetivos estadísticos pueden admitir condiciones más específicas. MAR e ignorabilidad requieren supuestos adicionales sobre parámetros. |
| 7 | La fórmula gráfica y las notas muestran √(1−π) cuando falta una sola variable bajo MCAR. El paso textual que dice 1−π no corresponde a la correlación en ese caso. |
| 8 | p es el número de variables en la fórmula de distancia, mientras en la página 6 p es probabilidad de ausencia. |
| 9, 32 | Una ejecución con sample_posterior=True produce una realización. Para estudiar imputación múltiple hay que generar varias y comparar resultados. |
| 10–11 | Un indicador de ausencia puede ser útil bajo varios mecanismos. No prueba que la ausencia sea MNAR. La fórmula exacta de atenuación no se traslada automáticamente a imputar la mediana. |
| 14–16 | El score teórico de Isolation Forest y las salidas de scikit-learn tienen distinta orientación. LOF también presenta salidas negativas en la API. Una alerta no implica eliminar. |
| 18–20 | Cifras de balance y covarianza corresponden al ejemplo de ajuste. No garantizan el mismo comportamiento en futuros datos. |
| 22–24 | Box-Cox exige positivos. λ=1 da x−1. Yeo-Johnson admite todos los signos y no garantiza normalidad conjunta. |
| 27 | El aporte dos por dummy estandarizada es en esperanza, no exactamente para cada par. FAMD y ponderar por 1/√C son procedimientos diferentes. |
| 28 | Si no hay campos compartidos, Gower queda indefinida. Ignorar faltantes no implica que distancias con distinto solapamiento tengan igual fiabilidad. |
| 30 | Los ARI mostrados usan grupos conocidos de una simulación. No son resultados de Cygnus. Una corrección de lote puede borrar señal cuando lote y fenómeno se confunden. |
| 31–33 | Clustering descriptivo, evaluación de generalización y forecasting son objetivos diferentes. Para operar en el futuro se respeta fecha y disponibilidad de variables. |

## Documentación técnica complementaria

- [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html): vecinos y distancias con valores ausentes.
- [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html): modelos condicionales e imputación posterior.
- [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html): Box-Cox, Yeo-Johnson y estandarización.
- [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html): orientación de scores y predicción.
- [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html): densidad local y novelty.
- [Guía de preprocesamiento](https://scikit-learn.org/stable/modules/preprocessing.html): escalas y codificación.

Referencias académicas citadas por la clase: Rubin (1976), Little y Rubin (2019), van Buuren (2018), Liu, Ting y Zhou (2008), Breunig et al. (2000), Box y Cox (1964), Yeo y Johnson (2000), Gower (1971), Huang (1998), Johnson, Li y Rabinovic (2007). Se conservan como referencias del material, sin afirmar que se haya revisado aquí cada publicación completa.

## Cómo llevarlo a Medallio sin confundir granularidades

Las siguientes son propuestas conceptuales de variables. Deben verificarse nombres, disponibilidad y reglas contra el esquema vigente antes de implementarlas.

| Objetivo | Una fila representa | Variables candidatas | Comprobación |
| --- | --- | --- | --- |
| Perfiles de demanda | Lead en una fecha de corte | Presupuesto, área buscada, visitas, canal | Cada campo estaba disponible al corte y no contiene el desenlace futuro. |
| Comparables de pricing | Unidad | Área, piso, tipología, precio por m² | Moneda y definición de áreas consistentes, sin duplicados por fuente. |
| Fricción comercial | Separación en una fecha de corte | Días abiertos, acciones realizadas, proyecto | Diferenciar eventos no ocurridos de fechas desconocidas. |
| Patrones de absorción | Proyecto y mes | Ventas, stock y etapa comercial | Misma definición de venta, entrada al stock y tratamiento retrospectivo de caídas. |

Estos nombres no certifican tablas existentes ni alteran reglas de negocio del data warehouse. Tampoco mezclan leads y unidades en una sola matriz por comodidad.

## Plantilla para decidir

| Decisión | Supuesto | Evidencia a revisar | Efecto a comparar |
| --- | --- | --- | --- |
| Imputación | Por qué falta el dato | Ausencia por canal, fecha y proyecto | Cobertura y estabilidad de asignaciones |
| Atípicos | Error o caso válido | Fuente, documento y revisión de negocio | Influencia en centros y comparables |
| Escala y forma | Qué significa cercanía | Aportes de distancia y distribuciones | Perfiles bajo alternativas razonables |
| Categorías | Peso de cada bloque | Frecuencias, desconocidas y dimensión | Grupos explicados solo por canal o proyecto |
| Evaluación | Uso futuro o exploración | Corte temporal, duplicados y disponibilidad | Estabilidad, interpretación y utilidad operativa |
