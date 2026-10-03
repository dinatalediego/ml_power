# Diapositiva 11 · Elegir tratamiento de faltantes

[Índice](README.md) · [Anterior](diapositiva-10.md) · [Siguiente](diapositiva-12.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

La tabla compara eliminación, media/mediana, KNN, MICE e indicadores. No existe una elección universal: importa mecanismo, cobertura, costo y estabilidad. La fórmula √(1−π) se deriva para imputación por media bajo condiciones concretas. La mediana también puede crear concentraciones artificiales, pero no comparte necesariamente esa fórmula exacta. Los indicadores pueden ser útiles fuera de MNAR.

## Historia 1: Pocas ausencias

De 10.000 unidades comparables, 20 carecen de piso por un fallo confirmado como aleatorio. El equipo evalúa excluirlas de este análisis y reporta 99,8 % de cobertura. Si los 20 fueran precisamente todos los dúplex, la misma cifra ya no justificaría eliminar sin revisar el sesgo.

## Historia 2: Relaciones locales

En 2.000 leads, el presupuesto cambia de forma distinta según área y dormitorios buscados. El analista prueba KNN con variables escaladas y oculta valores conocidos de entrenamiento para comparar error de imputación. Después revisa estabilidad de los grupos. Una mejor imputación individual no garantiza por sí sola mejores segmentos.

## Historia 3: Decisión bajo incertidumbre

Con 30 % de presupuestos ausentes, comercial quiere interpretar segmentos de capacidad de compra. El equipo usa varias imputaciones y reporta qué perfiles se mantienen. Si los resultados cambian mucho, busca completar datos o reformula el segmento con actividad observada. La incertidumbre puede cambiar la decisión de negocio.

## Aplicación a tu trabajo

¿Qué método preserva mejor cobertura y estructura en tu caso?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Faltantes: para qué, límites y cómo

Método | Supuesto | Para qué sirve | Límite | Cómo se usa
--- | --- | --- | --- | ---
Eliminación | MCAR | Rápida; sin sesgo si MCAR | Pierde 1−(1−p)^d de las filas | dropna(), con p·d pequeño
Media / mediana | MCAR | Línea base inmediata | Atenúa ρ por √(1−π) | SimpleImputer, strategy='median'
KNN | MAR, estructura local | Relaciones no lineales | O(n²p); exige escalar | KNNImputer, weights='distance'
MICE | MAR | Relaciones multivariadas e incertidumbre | Costo; supuestos de cada modelo | IterativeImputer, sample_posterior=True, m veces
Indicadores | MNAR informativo | Convierte la ausencia en señal | Puede dominar la distancia | add_indicator=True, con peso w

11/33

<details>
<summary>Notas del docente en el archivo original</summary>

Regla de decisión: razonar primero el mecanismo. MCAR plausible y pérdida pequeña: eliminar es aceptable. MAR: KNN o MICE. Sospecha de MNAR: indicadores y análisis de sensibilidad (comparar soluciones bajo distintos supuestos).

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-10.md) · [Siguiente](diapositiva-12.md)
