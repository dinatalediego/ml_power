# Diapositiva 25 · Separar escala de forma

[Índice](README.md) · [Anterior](diapositiva-24.md) · [Siguiente](diapositiva-26.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

La tabla reúne métodos que igualan magnitudes, reducen sensibilidad a extremos, eliminan correlaciones o cambian forma. La elección depende de algoritmo y propósito. Un orden frecuente es imputar, transformar y escalar, con excepciones como KNN, que necesita escala para encontrar vecinos. Ningún método garantiza segmentos útiles por sí solo.

## Historia 1: Actividad de leads

El equipo parte de interacciones con cola larga. Compara log1p más escala con RobustScaler sobre conteos originales. Revisa perfiles y estabilidad, porque ambas opciones dan diferentes distancias. Elige la que distingue patrones de actividad relevantes sin exagerar registros extremos o borrar clientes intensivos válidos.

## Historia 2: Comparables transparentes

Pricing necesita explicar por qué dos departamentos son parecidos. Empieza por variables claras y una escala robusta. Solo prueba whitening si la redundancia altera el resultado. Prefiere un procedimiento cuya ganancia pueda demostrar con casos, en lugar de sumar técnicas por estar disponibles.

## Historia 3: Un porcentaje acotado

Porcentaje vendido ya está entre cero y uno, mientras días en tubería no tiene límite fijo. El analista no concluye que la primera variable ya tiene el peso correcto. Revisa dispersión y prioridad comercial. Tener un rango cómodo para mostrar un dato no define su influencia en clustering.

## Aplicación a tu trabajo

¿Cada transformación tiene una razón que puedes explicar al gerente?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Escala y forma: para qué, límites y cómo

Técnica | Para qué sirve | Límite | Cómo se usa
--- | --- | --- | ---
Estandarización | Poner todas las variables en la misma escala (K-means, PCA) | Sensible a atípicos | StandardScaler()
Min-max | Llevar los datos a un rango fijo, normalmente [0,1] (%, reflectancia) | Un extremo comprime el resto | MinMaxScaler()
Robusto | Ajustar variables con colas pesadas o muchos outliers (Colas pesadas o atípicos) | No acota el rango, solo reduce la influencia de extremos | RobustScaler()
Whitening | Eliminar correlaciones entre variables, dejar la covarianza como identidad. | Ruido en λ pequeños; puede borrar la separación | PCA(whiten=True)
Box-Cox | Reducir asimetría positiva (colas largas, positiva, x > 0) | No admite ceros ni negativos | PowerTransformer, method='box-cox'
Yeo-Johnson | Reducir asimetría en variables con cualquier signo (positivos y negativos) | Normaliza marginales, no la conjunta | PowerTransformer, method='yeo-johnson'

25/33

<details>
<summary>Notas del docente en el archivo original</summary>

Orden habitual: primero la transformación de potencia (forma) y luego el escalado (peso). PowerTransformer estandariza al final por defecto. Cuándo no escalar: variables con las mismas unidades donde la varianza tiene significado físico.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-24.md) · [Siguiente](diapositiva-26.md)
