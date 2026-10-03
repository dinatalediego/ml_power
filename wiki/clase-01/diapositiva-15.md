# Diapositiva 15 · LOF y anomalías locales

[Índice](README.md) · [Anterior](diapositiva-14.md) · [Siguiente](diapositiva-16.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

LOF compara densidad de una observación con la de sus vecinos. Una puntuación teórica cercana a uno sugiere densidad similar. Valores claramente mayores señalan menor densidad relativa. Su significado depende de k, métrica y escala. En scikit-learn negative_outlier_factor_ es el negativo de LOF para datos de ajuste. Una rareza local puede pasar inadvertida al comparar todo el portafolio.

## Historia 1: Un flat demasiado caro

En un proyecto, flats de 70 m² tienen precios por m² alrededor de US$ 1.800. Uno alcanza US$ 2.600 y sus características restantes son similares. LOF puede destacarlo entre sus vecinos aunque otros proyectos tengan ese precio habitualmente. Pricing revisa acabados y carga antes de decidir una corrección.

## Historia 2: Duración fuera del entorno

Separaciones de un proyecto suelen durar entre 10 y 20 días. Una lleva 70. En otro proyecto, 70 días es habitual por su proceso contractual. El analista incorpora contexto y analiza vecinos comparables. La rareza depende del entorno, sin concluir que toda separación larga tiene el mismo riesgo.

## Historia 3: Vecindad demasiado pequeña

Con k=3, pequeños cambios en leads alteran muchas alertas. Con k=200, el análisis pierde diferencias locales. El equipo compara varios k y revisa casos con comercial. Busca alertas consistentes y accionables, en vez de elegir el parámetro que produzca el mayor número de anomalías.

## Aplicación a tu trabajo

¿Qué hace que dos unidades o leads compartan un entorno comercial?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

LOF: tu densidad frente a la de tus vecinos

Punto junto al cúmulo denso: LOF = 3.3, aunque está a 2.1 unidades: una distancia típica en el cúmulo disperso. Punto lejano: LOF = 2.1.

LOF ≈ 1: densidad como la de sus vecinos. LOF ≫ 1: menos denso que su entorno.

15/33

Reach-distancia: ajusta la distancia con vecino

Densidad local inversa (lrd) : calcula la densidad local del punto

Factor de outlier local (LOF): compara esa densidad con la de los vecinos

<details>
<summary>Notas del docente en el archivo original</summary>

Breunig et al. (2000). La distancia de alcanzabilidad suaviza las distancias pequeñas; lrd es una densidad local; LOF es el cociente promedio entre la densidad de los vecinos y la del punto. Dentro de un cúmulo homogéneo LOF ≈ 1 sea denso o disperso (medianas 1.05 y 1.02). Un umbral global de distancia marcaría media nube dispersa o ignoraría el atípico local. k = 20 aquí; con k pequeño LOF es ruidoso, con k grande se vuelve global.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-14.md) · [Siguiente](diapositiva-16.md)
