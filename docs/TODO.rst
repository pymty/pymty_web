Tareas por hacer
================

De momento se busca que el sitio este publico y funcional lo antes posible sin enfocarse a terminarlo por completo.

Se ha sugerido una secuencia de iteraciones para entregar por partes y tener algo visible sin tanta elegancia.

Para más información de las iteraciones revisa ``docs/contenido.rst``.

Objetivos generales
-------------------

Reuniones
.........
El contenido que se busca mostrar en esta sección:

 1. Una breve descripción sobre las reuniones, ¿qué son?, ¿qué tipo de reuniones organizamos?
 2. Donde se coordinan (meetup)
 3. A que audiencia van dirigidas
 4. Aclarar costos (gratis)
 5. Historial de reuniones para hacer compendios de minutas o contenido del expositor.

Documentación
.............
Es un compendio de recursos en linea de documentación sobre python o sobre programación en general.

Contribuir
..........
Muestra las formas en que los mismos miembros de el grupo puedan contribuir al mismo.

 1. Dar una platica.
 2. Ofrecer un lugar para llevar a cabo reuniones.
 3. Coordinar algún evento.
 4. Mejorar la página.

Comunidades
...........
Presenta un listado de comunidades afines de la ciudad. El grupo esta para crear puentes no para quemarlos.
Esperamos tener por lo menos intersecciones con grupos de negocios, diseño, programación y emprendedurismo.


Bolsa de trabajo
................
Dado que de formar recurrente ha sido una necesidad el de tener una bolsa de trabajo que
facilite el encuentro de los empleadores en busca de programadores, surge la necesidad
de esta sección.


CSS
----

Mejorar estructura de css
.........................
Actualmente el sitio solo tiene definido el footer y header, aún no tiene una clara definición de cuales
son los puntos de ruptura para los media queries, existen algo de definicion en el archivo de ``main.css``
pero considero que aún esta muy caótico.

Refinar la clase "block"
........................
Esa clase es la que se encargara de manejar la forma de presentar cada cuadro de contendio que se
presente en el contenedor principal. De momento funciona pero es algo a considerar para el contenido
que se vaya agregando.

Definir presentación del texto
..............................
No se ha prestado atención a la presentación de el texto, la tipografía, tamaño y color.


HTML
----
En general en ``docs/contenido.rst`` define el contenido a mostrar, se sugiere utilizar WTForms_ en caso
de que consideren practico el asistirse para los formularios.

Metadatos
..........
Definir metadatos de opengraph_ y una forma de generar sitemaps_.

SEO
...
No se tienen lineamientos sobre cual sería la mejor forma para facilitar el el indexado de el sitio,
como principio sería usar metatags de descripción y titulos significativos.

Modelos
-------

Los modelos de datos serán basados en NDB de AppEngine.



.. _WTForms: https://wtforms.readthedocs.org/en/latest/
.. _opengraph: http://ogp.me/
.. _sitemaps: http://www.sitemaps.org/
.. _NDB: https://developers.google.com/appengine/docs/python/ndb/
