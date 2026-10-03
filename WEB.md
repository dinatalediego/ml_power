# Sitio web de ml_power

La web de lectura incluye 33 diapositivas, 99 historias, búsqueda por título y tema, navegación por clase, progreso local e impresión por página.

## Publicar en Vercel

Importar `dinatalediego/ml_power` desde Vercel. La configuración raíz `vercel.json` selecciona sitio estático y carpeta de salida `site`. Los HTML ya están generados, por lo que no requiere instalar dependencias ni ejecutar un build remoto.

También se puede desplegar la carpeta `site` directamente. Incluye su propia configuración con salida `.`.

## Actualizar el contenido

1. Editar las páginas Markdown en `wiki/clase-01`.
2. Ejecutar `python scripts/build_site.py` desde el repositorio.
3. Publicar los archivos modificados de `site` junto con el Markdown.

El generador usa únicamente la biblioteca estándar de Python. El navegador recibe HTML, CSS y JavaScript estáticos. El progreso se guarda en el navegador del lector y no se envía a un servidor.

## Comprobación local

Desde la carpeta `site`, ejecutar `python -m http.server 8000` y abrir `http://localhost:8000`.

Las cifras de las historias son sintéticas. La web no consulta ni publica datos de Medallio.
