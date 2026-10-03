# Diapositiva 32 · Pipeline reproducible

[Índice](README.md) · [Anterior](diapositiva-31.md) · [Siguiente](diapositiva-33.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Pipeline y ColumnTransformer mantienen ajuste y transformación coherentes. El ejemplo de clase transforma numéricas, codifica categorías, detecta atípicos y ajusta K-means. Usa una sola imputación y excluye anomalías del ajuste, decisiones que deben validarse. Para Cygnus conviene un corte temporal cuando se aplicará a leads futuros, imputar categóricas explícitamente y ponderar bloques según la codificación usada.

## Historia 1: Mismo lead, mismo proceso

Un modelo ajustado en junio guarda imputador, transformación y codificador. En julio, un lead recibe exactamente esas transformaciones antes de predict. El analista evita recalcular medianas con el lote diario. Comercial puede comparar asignaciones porque el procedimiento aprendido se mantiene estable hasta una actualización documentada.

## Historia 2: Un canal desconocido

Aparece una nueva campaña que el encoder no vio. Con handle_unknown=ignore se evita el fallo, pero el bloque queda en ceros para esa variable. El equipo registra la novedad y revisa el efecto. Tolerar una categoría nueva no significa que el modelo ya entienda su significado.

## Historia 3: Anomalías visibles

Isolation Forest marca 40 de 2.000 leads. El equipo decide cuáles excluir del ajuste de K-means tras revisar causas. Al reportar, conserva todos con bandera de anomalía y asignación separada cuando corresponda. Si los borrara también del tablero, perdería precisamente los casos que requieren seguimiento.

## Aplicación a tu trabajo

¿Puedes volver a ejecutar el mismo pipeline y explicar cada decisión de ajuste?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Todo en un pipeline de scikit-learn

num = Pipeline([
    ("imp", IterativeImputer(sample_posterior=True, random_state=0)),
    ("yj",  PowerTransformer(method="yeo-johnson")),
])
cat  = OneHotEncoder(handle_unknown="ignore")
prep = ColumnTransformer([("num", num, cols_num),
                          ("cat", cat, cols_cat)],
                         transformer_weights={"cat": w})
 
X_tr, X_te = train_test_split(X, test_size=0.2, random_state=0)
Z_tr = prep.fit_transform(X_tr)           # solo train
ok   = IsolationForest(random_state=0).fit_predict(Z_tr) == 1
km   = KMeans(n_clusters=4, n_init=10).fit(Z_tr[ok])
etiq = km.predict(prep.transform(X_te))   # solo transform

Un orden razonable

1

Auditar: tipos, % de faltantes, lotes, duplicados.

2

Separar train / test (o por tiempo) antes de ajustar.

3

Imputar (KNN o MICE; indicadores si MNAR).

4

Corregir lotes si el diseño lo permite.

5

Transformar forma, luego escalar.

6

Codificar y ponderar bloques.

7

Detectar atípicos; decidir con el dominio.

8

Modelar y validar estabilidad.

32/33

<details>
<summary>Notas del docente en el archivo original</summary>

Imports: Pipeline, ColumnTransformer, enable_iterative_imputer (sklearn.experimental), IterativeImputer, PowerTransformer, OneHotEncoder, train_test_split, IsolationForest, KMeans. cols_num, cols_cat y w los define cada proyecto (w ≈ 1/√C, proposición 3). El orden no es fijo: KNN exige escalar antes de imputar y detectar atípicos puede requerir una primera pasada robusta. Los atípicos se excluyen del ajuste de K-means, no del reporte: igual reciben etiqueta.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-31.md) · [Siguiente](diapositiva-33.md)
