# Diapositiva 27 · El peso oculto del one-hot

[Índice](README.md) · [Anterior](diapositiva-26.md) · [Siguiente](diapositiva-28.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Dos categorías distintas tienen distancia cuadrada dos en one-hot sin escalar. Si cada dummy no constante se estandariza a varianza uno, aporta dos en esperanza entre observaciones independientes, por lo que un bloque de C dummies aporta 2C. Esa afirmación es sobre promedio, no sobre cada par. Multiplicar el bloque por 1/√C equilibra ese caso. FAMD usa otra normalización y no equivale exactamente a esa regla.

## Historia 1: Diez proyectos votan demasiado

El modelo contiene presupuesto estandarizado y diez dummies de proyecto también estandarizadas. El bloque proyecto aporta en promedio 20 a la distancia cuadrada frente a dos del presupuesto. El analista reduce el peso del bloque y compara. Los perfiles dejan de depender casi exclusivamente del proyecto consultado.

## Historia 2: El canal muy raro

Un canal representa 1 % de leads. Estandarizar su dummy divide por una desviación cercana a 0,10. Esos leads quedan muy lejos de los demás. Marketing verifica si la rareza merece tanta importancia o si refleja una campaña pequeña. La frecuencia de captura puede producir un peso inesperado.

## Historia 3: Bloques con distintos tamaños

El pipeline combina proyecto con diez categorías y canal con cuatro. Aplicar un único peso global a todas las dummies no balancea cada variable por separado. El analista define bloques y compara contribuciones. También revisa codificación sin estandarizar, donde el aporte no crece linealmente con C.

## Aplicación a tu trabajo

¿Cuánto aporta cada bloque categórico frente a una variable numérica?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

El peso oculto del one-hot

PROPOSICIÓN 3

Distancia entre dos categorías distintas

1

Dos categorías distintas quedan a distancia √2; sin escalar, el aporte máximo es 2.

2

Estandarizar cada dummy reescala su aporte a exactamente 2, sin importar la frecuencia de la categoría.

3

Una variable con C categorías estandarizadas pesa C veces más que una numérica estandarizada (que aporta 2)

Una variable de 10 categorías estandarizada pesa 10 veces más que una numérica. Solución: ponderar el bloque por 1/√C o usar FAMD, método que automáticamente balancea numéricas y categóricas

27/33

El aporte total de un bloque de C categorías estandarizadas es proporcional a C. Eso quiere decir, que el peso de la variable categórica crece linealmente con el número de categorías.

Varianza de cada dummy:

<details>
<summary>Notas del docente en el archivo original</summary>

Con C = 10 categorías equiprobables: one-hot sin escalar aporta 2(1 − 1/10) = 1.8; una numérica estandarizada aporta 2; el bloque de dummies estandarizadas aporta 20. Además, las categorías raras reciben valores enormes tras estandarizar (1/√(p(1−p))). Soluciones: ponderar el bloque por 1/√C (ColumnTransformer con transformer_weights) o FAMD, que escala cada dummy por 1/√p_c. La codificación ordinal impone |a − b| con intervalos iguales: solo si el orden y el espaciado tienen sentido.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-26.md) · [Siguiente](diapositiva-28.md)
