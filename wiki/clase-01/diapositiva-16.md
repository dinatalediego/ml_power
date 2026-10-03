# Diapositiva 16 · Isolation Forest frente a LOF

[Índice](README.md) · [Anterior](diapositiva-15.md) · [Siguiente](diapositiva-17.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

La diapositiva contrasta aislamiento por cortes y densidad local. Isolation Forest suele ser eficiente para muchos registros. LOF necesita una representación de distancias bien elegida y puede ser costoso. Su complejidad depende de dimensión y búsqueda de vecinos, no siempre es exactamente cuadrática. Para nuevos datos LOF requiere novelty=True y se puntúa únicamente el conjunto nuevo con esos métodos.

## Historia 1: Revisión masiva del CRM

El equipo revisa 100.000 leads para detectar actividad y presupuestos inusuales. Empieza con Isolation Forest y valida manualmente una muestra de alertas. No fija contamination como tasa real de errores sin evidencia. Mide cuántas alertas terminan en correcciones o acciones útiles.

## Historia 2: Comparables de un proyecto

Pricing analiza 150 departamentos de una etapa con características conocidas. Prueba LOF sobre variables escaladas para detectar diferencias dentro del entorno. Revisa sensibilidad a k y tipo de unidad. Un método local es útil cuando la pregunta es por qué una unidad difiere de sus comparables cercanos.

## Historia 3: Datos de mañana

El modelo debe alertar sobre los leads que llegan cada día. El analista ajusta LOF con novelty=True sobre históricos y transforma los nuevos con el preprocesamiento aprendido. No mezcla esos leads con entrenamiento para obtener una evaluación retrospectiva artificialmente favorable.

## Aplicación a tu trabajo

¿Buscas rarezas en la base actual o alertas para registros futuros?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Isolation Forest frente a LOF

Criterio | Isolation Forest | LOF
--- | --- | ---
Tipo de anomalía | Detecta outliers global: puntos muy distintos al resto del conjunto | Detecta outliers locales: puntos con densidad menor que la de sus vecino
Costo | O(t·ψ·log ψ); Computacionalmente eficiente | Más pesado O(n²) ingenuo; 
Escala | Poco sensible a si las variables están en diferentes unidades | Muy sensible, exige normalizar las variables
Hiperparámetros | n_estimators, max_samples, contamination | n_neighbors (k), contamination
Límites | Los cortes son paralelos a los ejes, puede perder detalle en densidades complejas. | El puntaje LOF no tiene escala universal y se complica en alta dimensión
Datos nuevos | predict sobre el modelo ajustado | novelty=True y ajustar solo con train

16/33

<details>
<summary>Notas del docente en el archivo original</summary>

Complementarios: IF para anomalías globales y datos grandes; LOF para anomalías contextuales con densidades variables. Detalle que conecta con el bloque 6: LOF con novelty=False solo puntúa los datos de ajuste; para puntuar datos nuevos sin fuga hay que ajustar con novelty=True sobre entrenamiento. Extended Isolation Forest usa hiperplanos oblicuos para evitar artefactos de los cortes paralelos a los ejes.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-15.md) · [Siguiente](diapositiva-17.md)
