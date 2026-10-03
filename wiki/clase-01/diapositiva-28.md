# Diapositiva 28 · Gower y datos mixtos

[Índice](README.md) · [Anterior](diapositiva-27.md) · [Siguiente](diapositiva-29.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Gower promedia diferencias normalizadas por rango en numéricas y discrepancias 0/1 en nominales, usando solo campos comparables y pesos elegidos. Con poco solapamiento, la distancia puede ser poco fiable y si no hay ninguno queda indefinida. Se combina con métodos que aceptan disimilitudes, como PAM o clustering jerárquico. K-Prototypes balancea costos con γ. Sin objetivo, target encoding no es una opción natural.

## Historia 1: Dos departamentos

En un ejemplo, dos unidades difieren 10 m² en un rango de 50 m²: aporte 0,20. Difieren dos pisos en rango de diez: 0,20. Tienen tipologías distintas: uno. Con iguales pesos y sin faltantes, Gower es (0,20+0,20+1)/3≈0,467. Pricing puede discutir cada aporte directamente.

## Historia 2: Muchos distritos

El equipo usa frecuencia para codificar 40 distritos. Dos distritos con 5 % de leads reciben el mismo número y resultan indistinguibles en esa variable. El analista reconoce la pérdida de identidad y compara Gower u otra representación. Frecuencia describe popularidad, sin preservar todas las diferencias entre categorías.

## Historia 3: Pocos campos compartidos

Dos leads coinciden en canal, pero faltan presupuesto, edad y área en uno. Gower puede dar distancia cero usando solo canal. Comercial evita llamarlos idénticos y revisa cobertura del cálculo. Una distancia pequeña basada en poca información requiere interpretación distinta de una sustentada en todos los campos.

## Aplicación a tu trabajo

¿Tu algoritmo acepta una matriz de distancias o necesita coordenadas numéricas?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Datos mixtos: Gower y compañía

Numerical: Diferencia normalizada por el rango de la variable.
Categorical: 0 si son iguales, 1 si son distintos.
Faltantes: δikj=0 si falta el dato → Gower ignora esa variable en el cálculo.

Codificación | Cuándo | Cuidado
--- | --- | ---
One-hot | Variables nominales con pocas categorías | Dimensión y peso del bloque
Ordinal | Variables con orden natural (ej. bajo, medio, alto) | Impone intervalos iguales
Frecuencia | Variables con muchísimas categorías | Categorías con igual frecuencia colapsan
K-Prototypes | Mezcla numérica + categórica | γ equilibra ambos costos
FAMD / MCA | Reducir y visualizar categóricos | Interpretar ejes con cuidado

Target encoding no aplica: en no supervisado no hay variable objetivo.

28/33

La distancia de Gower

<details>
<summary>Notas del docente en el archivo original</summary>

Gower (1971): promedia disimilitudes por variable en [0, 1]; Rⱼ es el rango de la variable numérica j y wⱼ pesos opcionales. Como no produce coordenadas, se combina con algoritmos que aceptan una matriz de disimilitud (PAM, jerárquico, DBSCAN precomputado). K-Prototypes (Huang, 1998) suma la euclidiana en lo numérico y las discrepancias en lo categórico, ponderadas por γ.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-27.md) · [Siguiente](diapositiva-29.md)
