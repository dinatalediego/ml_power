# Diapositiva 24 · Yeo-Johnson admite cualquier signo

[Índice](README.md) · [Anterior](diapositiva-23.md) · [Siguiente](diapositiva-25.md)

> Clase 01. Ejemplos inmobiliarios con cifras sintéticas. Los nombres de proyectos y sistemas contextualizan la explicación, sin afirmar resultados observados de Cygnus.

## Cómo leer esta diapositiva

Para x≥0 utiliza ((x+1)^λ−1)/λ o ln(x+1). Para x<0 utiliza −((1−x)^(2−λ)−1)/(2−λ), o −ln(1−x) si λ=2. Admite ceros y negativos. La asimetría 2,60→0,14 y λ=0,60 pertenecen al ejemplo de clase. Mejorar marginales no garantiza normalidad conjunta ni obliga a borrar varios modos.

## Historia 1: Cambios de ventas

Un proyecto registra cambios mensuales de −4, 0, 2 y 18 ventas. El analista usa Yeo-Johnson para explorar perfiles mensuales sin descartar los meses negativos. Explica resultados en ventas originales. Para pronosticar necesitará además un modelo temporal y una evaluación por horizonte.

## Historia 2: Desviación de precio

Pricing calcula diferencia entre precio por m² de una unidad y la mediana de comparables. Obtiene −200, cero y +600 dólares. Yeo-Johnson permite tratar la cola sin sumar una constante para forzar positividad. El equipo conserva el signo como interpretación del indicador original.

## Historia 3: Dos tipos de cliente

La variación de presupuesto de leads tiene dos picos: compradores que amplían búsqueda y quienes la reducen. La transformación puede reducir asimetría, pero no tiene que convertir ambos perfiles en una campana. Comercial estudia la diferencia antes de imponer una representación que oculte esa conducta.

## Aplicación a tu trabajo

¿Necesitas admitir negativos porque son resultados válidos de tu indicador?

## Contenido del material entregado

Transcripción del texto editable. Las fórmulas o figuras insertadas como imágenes no aparecen en esta transcripción. La explicación anterior desarrolla el concepto usando también las notas del docente.

Yeo-Johnson: Box-Cox con signo

2.60 → 0.14

La asimetría bajo

0.60

El major parámetro λ̂  estimado por la máx. verosimilitud

38 %

Valores eran negativos

24/33

Para x≥0: es igual a Box-Cox aplicado a x+1.
Para x<0: aplica una fórmula simétrica que usa 2−λ y cambia el signo.
Esto asegura que la transformación sea continua y monótona en todo R (no se rompe en el cero).

Después de aplicar Yeo-Johnson

Distribución original, sesgada

<details>
<summary>Notas del docente en el archivo original</summary>

Yeo y Johnson (2000). Útil para variaciones porcentuales, anomalías de temperatura, índices centrados o residuos. Límite: normaliza cada marginal, no la conjunta, y no convierte una variable bimodal en unimodal; tampoco debe: la bimodalidad puede ser justo la estructura que buscamos.

</details>

[Fuentes y aclaraciones](fuentes-y-aclaraciones.md) · [Índice](README.md) · [Anterior](diapositiva-23.md) · [Siguiente](diapositiva-25.md)
