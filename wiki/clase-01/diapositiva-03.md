# Diapositiva 03 · La distancia decide los grupos

[Índice](README.md) · [Anterior](diapositiva-02.md) · [Siguiente](diapositiva-04.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

K-means minimiza distancias euclidianas al cuadrado. Para dos observaciones independientes, una variable aporta en promedio 2σ². Con desviaciones de ingreso de 3.000 soles y edad de 12 años, el ingreso aporta 9.000.000 / 9.000.144 ≈ 99,9984 % del total entre estas dos variables. Estandarizar ambas iguala sus aportes esperados, salvo variables constantes. Los pesos deben responder al negocio.

## Historia 1: Presupuesto contra visitas

Dos leads difieren en S/ 100.000 de presupuesto y en dos visitas. Sin escala, sus contribuciones son 10.000 millones y cuatro. El equipo descubre que el modelo ignora casi por completo las visitas. Estandariza y compara los grupos, verificando que la actividad comercial ahora tenga influencia.

## Historia 2: Área contra piso

Dos departamentos difieren en 20 m² y dos pisos. Sus aportes cuadrados son 400 y cuatro. El analista decide si esa relación es deseada antes de normalizar. Si pricing valora mucho la ubicación vertical, añade un peso explícito y documenta el cambio en los comparables.

## Historia 3: Varias métricas de contacto

El equipo agrega llamadas, mensajes y contactos totales a un clustering de leads. Aunque estandariza cada columna, la actividad queda representada varias veces. Revisa correlaciones y conserva una medida principal. Igualar escalas no elimina la duplicación de información.

## Aplicación a tu trabajo

¿Qué variable dominaría tu distancia si usaras sus unidades originales?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

La distancia decide los grupos

Con σ(ingreso) = 3000 soles y σ(edad) = 12 años (valores ilustrativos), el ingreso aporta el 99.99 % de la distancia esperada: K-means agruparía solo por ingreso.

Sin etiquetas, nadie corrige una mala geometría: en no supervisado el preprocesamiento no «prepara» los datos, decide qué significa estar cerca.

3/33

<details>
<summary>Notas del docente en el archivo original</summary>

K-means minimiza la suma de distancias al cuadrado a los centroides: la métrica es el modelo. Para dos observaciones independientes de la misma distribución, E[(Xⱼ − X'ⱼ)²] = 2σⱼ², así que cada variable aporta en proporción a su varianza: 9·10⁶ de 9.0016·10⁶ en el ejemplo. Tras estandarizar, cada una aporta 25 %. ¿Siempre es correcto igualar pesos? No: si las variables comparten unidades físicas (reflectancias de bandas Sentinel-2), la varianza puede ser información legítima.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-02.md) · [Siguiente](diapositiva-04.md)
