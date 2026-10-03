# Diapositiva 13 · Influencia del atípico en el centroide

[Índice](README.md) · [Anterior](diapositiva-12.md) · [Siguiente](diapositiva-14.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Si un grupo de n observaciones tiene media μ y se incorpora xo, el desplazamiento es (xo−μ)/(n+1). Crece sin límite con el extremo. La mediana tolera mucha más contaminación, pero eso no convierte toda anomalía en error. K-medoides u otras variantes robustas pueden ser alternativas cuando la media no representa bien al grupo.

## Historia 1: El ticket que sube

Veinte leads tienen presupuesto promedio de S/ 500.000. Se incorpora uno de S/ 2.000.000 y la media sube unos S/ 71.429. El equipo revisa si representa un inversionista válido o un error. La media del segmento cambió sin que los veinte clientes originales modificaran su presupuesto.

## Historia 2: La duración imposible

Diez separaciones cerradas duran en promedio 20 días. Un registro con fecha incorrecta marca 1.100 días. La media pasa a unos 118 días. El analista verifica fechas y compara mediana. Antes de concluir que administración se demoró más, identifica el efecto de una observación.

## Historia 3: El grupo de una unidad

Con K=4, un departamento de precio extraordinario ocupa por sí solo un clúster. Los otros tres grupos absorben el resto de unidades. Pricing compara una opción robusta y una estratificación por producto. Así evita gastar un segmento completo en un extremo sin utilidad comercial general.

## Aplicación a tu trabajo

¿Cuánto se desplaza tu promedio con el registro más extremo?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Un atípico tiene influencia sin límite

La fórmula nos dice que un solo outlier puede mover la media muchísimo, porque la media es muy sensible. En cambio, la mediana aguanta hasta que la mitad de los datos estén contaminados.

Centroide original (negro) y con el atípico (ámbar): se desplaza 0.57 unidades = (xo − μ)/(nk + 1) con nk = 20.

Detectar no es eliminar: el atípico puede ser un error de captura o el hallazgo más valioso (fraude, deslizamiento, una laguna nueva).

13/33

Desplazamiento del centroide:

Punto de ruptura de la mediana:

<details>
<summary>Notas del docente en el archivo original</summary>

Al agregar xₒ al clúster k, el centroide pasa a (nₖμₖ + xₒ)/(nₖ + 1): el desplazamiento es lineal en xₒ y sin cota. Punto de ruptura: 1/n para la media, 50 % para la mediana, 25 % para el IQR. En K-means, un atípico lejano puede convertirse en centroide de un clúster unitario. Alternativas robustas: K-medoides, K-medianas, trimmed K-means.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-12.md) · [Siguiente](diapositiva-14.md)
