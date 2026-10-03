# Diapositiva 31 · Fuga de información

[Índice](README.md) · [Anterior](diapositiva-30.md) · [Siguiente](diapositiva-32.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Separar antes de fit impide que medias, vecinos, λ, PCA o selección de parámetros incorporen prueba. En uso futuro, el corte debe respetar fecha y momento de disponibilidad. Duplicados cruzados también contaminan evaluación. Explorar descriptivamente toda una base es un objetivo distinto de medir generalización sobre un conjunto reservado. Elegir K con etiquetas de evaluación externas impide usarlas luego como validación independiente.

## Historia 1: Mediana del semestre futuro

El analista evalúa en julio un modelo supuestamente ajustado hasta junio, pero calcula la mediana usando enero a julio. La distribución de julio ya influyó en el modelo. Reconstruye el preprocesamiento solo con enero a junio y vuelve a evaluar. Así mide el escenario disponible en la fecha real.

## Historia 2: Una minuta conocida después

Para segmentar leads al crearse, el equipo agrega si llegaron a minuta durante el trimestre siguiente. Esa variable revela el desenlace futuro. El analista la reserva para describir resultados posteriores, sin incluirla como información disponible al crear el lead. El corte temporal se aplica también a variables derivadas.

## Historia 3: Escoger K con el test

El equipo prueba veinte configuraciones y conserva la de mejor ARI frente a una clasificación externa del conjunto de prueba. Después reporta ese ARI como validación independiente. El analista usa un conjunto para selección y otro reservado para evaluación, o reconoce el carácter exploratorio del análisis.

## Aplicación a tu trabajo

¿Cada variable y transformación existía en el momento de la decisión?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Data leakage: el conjunto de prueba no se toca

La media de prueba ya entró al modelo.

Con fuga

datos completos

fit_transform

split

evaluar

Sin fuga

split

fit en train

transform train y test

evaluar

Fuentes típicas en no supervisado

1

Ajustar escalador, imputador, λ o PCA con todos los datos antes de separar.

2

Elegir K o hiperparámetros con las etiquetas externas que luego validan.

3

Fuga temporal: estadísticos que usan el futuro (ventanas centradas).

4

Duplicados o casi duplicados a ambos lados del corte.

31/33

Error: el test ya contaminó el preprocesamiento.

Correcto: el test se mantiene intacto hasta la evaluación.

<details>
<summary>Notas del docente en el archivo original</summary>

En no supervisado también hay fuga: cuando el modelo asignará clústeres a datos nuevos o cuando se evalúa estabilidad o generalización con datos retenidos. Todo parámetro de preprocesamiento (μ, σ, medianas, IQR, λ, modelos de imputación, vectores de PCA, parámetros de ComBat) es parte del modelo y se estima solo con entrenamiento. La media global mezcla la de prueba con peso n_te/n. En series temporales, el corte respeta el tiempo.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-30.md) · [Siguiente](diapositiva-32.md)
