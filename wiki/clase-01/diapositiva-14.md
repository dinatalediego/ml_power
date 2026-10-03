# Diapositiva 14 · Isolation Forest

[Índice](README.md) · [Anterior](diapositiva-13.md) · [Siguiente](diapositiva-15.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Isolation Forest divide aleatoriamente variables mediante cortes. Los casos fáciles de aislar suelen recorrer caminos más cortos. El score teórico es s=2^(−E[h]/c(ψ)): valores mayores indican más anomalía. En scikit-learn score_samples usa la orientación opuesta y decision_function incorpora el umbral. No se debe copiar el corte 0,5 del score teórico sobre esos métodos. La alerta no es probabilidad de fraude.

## Historia 1: Actividad automatizada

Un lead tiene 2 visitas, pero 900 interacciones en una hora. El bosque lo aísla rápidamente frente a actividad habitual. El equipo revisa integración y descubre reintentos de una API. Corrige el proceso de carga y conserva la alerta. La combinación extraña permitió encontrar un problema operativo.

## Historia 2: Precio y superficie

Una unidad presenta 65 m² y S/ 6.500.000 frente a departamentos similares mucho más baratos. El equipo consulta moneda y documentos. Si el monto es correcto por características excepcionales, mantiene el dato y lo explica. El algoritmo selecciona candidatos para revisión, sin decidir el precio correcto.

## Historia 3: Puntuación invertida

El analista ordena score_samples de mayor a menor creyendo que arriba están los más raros. La revisión parece inútil. Consulta la API y ordena de menor a mayor. Comprueba también predict, donde −1 indica anomalía. Interpretar correctamente el score cambia qué registros recibe operaciones.

## Aplicación a tu trabajo

¿Tu tablero explica la orientación del score y el motivo de revisión?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Isolation Forest: lo raro se aísla rápido

Punto central: 14 cortes · E[h] ≈ 13.9

Atípico: 3 cortes · E[h] ≈ 3.1

0.80

s(atípico): cerca de 1 = anomalía

0.37

s(central): menor que 0.5 = normal

c(201) = 9.76 normaliza el largo de camino.

14/33

El score s(x,ψ) convierte esa profundidad en un número entre 0 y 1

Se elige una variable q al azar (por ejemplo, edad, ingreso, altura).
Dentro de esa variable, se elige un punto de corte r al azar entre su mínimo y máximo.
Ese corte divide los datos en dos grupos.
Repitiendo este proceso muchas veces, se construye un “bosque” de particiones aleatorias.

<details>
<summary>Notas del docente en el archivo original</summary>

Liu, Ting y Zhou (2008). Las anomalías son pocas y diferentes: en particiones aleatorias quedan aisladas en pocos cortes. c(n) = 2H(n−1) − 2(n−1)/n es el largo promedio de una búsqueda fallida en un árbol binario; si E[h] = c, s = 0.5; si s ≈ 0.5 para todos, no hay anomalías claras. Simulación con 201 puntos y árboles completos; en la práctica ψ = 256 y altura máxima ⌈log₂ψ⌉. Poco sensible a la escala porque corta cada variable por separado.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-13.md) · [Siguiente](diapositiva-15.md)
