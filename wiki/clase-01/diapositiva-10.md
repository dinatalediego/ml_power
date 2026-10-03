# Diapositiva 10 · La ausencia como variable

[Índice](README.md) · [Anterior](diapositiva-09.md) · [Siguiente](diapositiva-11.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Un indicador binario señala que un campo estaba ausente, aun después de imputarlo. Puede revelar conducta o proceso de captura bajo diversos mecanismos, sin demostrar MNAR. Estandarizar una bandera con prevalencia π divide por √(π(1−π)), dando valores elevados cuando es rara. Su peso debe controlarse para evitar grupos definidos únicamente por vacíos.

## Historia 1: No declara presupuesto

Dos leads reciben presupuesto imputado de S/ 500.000, pero solo uno dejó el campo vacío. El equipo conserva esa diferencia para explorar patrones. Si el grupo con ausencia solicita más asesoría, diseña una conversación para completar información. No deduce automáticamente mayor o menor capacidad de compra.

## Historia 2: El canal forma el grupo

El formulario de una campaña omite cinco preguntas. Cinco indicadores correlacionados dominan la distancia y crean un clúster exclusivo de esa campaña. El analista revisa ausencia por canal, reduce pesos y compara la solución. El grupo reflejaba diseño del formulario más que intención inmobiliaria.

## Historia 3: Una bandera rara

Solo 1 % de las unidades carece de área total. Al estandarizar, esa bandera recibe una magnitud cercana a diez para esos registros. Pricing la utiliza para control de calidad, pero no la deja dominar los comparables. El peso depende de la pregunta que intenta responder.

## Aplicación a tu trabajo

¿El grupo que encontraste está definido por conducta o por campos vacíos?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Cuando faltar también es información

Cuándo ayuda

Bajo MNAR, r lleva señal: «no declara ingreso» puede ser un segmento real.

Riesgo

Estandarizado, cada indicador pesa como una variable completa: aparecen clústeres de «faltó / no faltó».

Control

El peso w fija cuánto importa el patrón frente a los valores; verificar si los grupos se explican solo por r.

10/33

Como cuando alguien no declara su ingreso, eso puede ser porque gana mucho y no quiere decirlo. Entonces, el “faltante” no es aleatorio: está dando una señal sobre la persona.

Distancias entre observaciones: La distancia entre dos personas se calcula considerando tanto los valores imputados como el patrón de faltantes, con un peso w que regula la importancia del patrón.

<details>
<summary>Notas del docente en el archivo original</summary>

El indicador es binario con varianza π(1 − π); estandarizado aporta 2 en esperanza a la distancia al cuadrado, como cualquier variable numérica. Varios indicadores correlacionados (variables que suelen faltar juntas) pueden dominar la solución. scikit-learn: SimpleImputer(add_indicator=True) o MissingIndicator.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-09.md) · [Siguiente](diapositiva-11.md)
