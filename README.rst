#################################
Sitio público de Python Monterrey
#################################

Introducción
============

Cómo forma de facilitar el acceso a las distintas partes que conforman al grupo de Python Monterrey surge la iniciativa de
centralizar por medio de un sitio web completo, originalmente se pensó que bastaría solamente con el sitio en meetup, pero
las recurrentes solicitudes a aspectos particulares sentaron la base para comenzar este sitio.

El dominio oficial de el sitio es: https://www.pymty.org


Requisitos
==========

Python, Mako_, CherryPy_, (Nix_ o poetry_).


Cómo ejecutar el sitio
======================

Con poetry::

  poetry install
  poetry run pymty


Con nix::

  nix-shell --run pymty


Estructura general
==================

Plantillas
----------

Todo lo que refiere a HTML esta contenido en ``pymty/pymty/templates`` utiliza Mako_ para la manipulación de plantillas.
La estructura esta basada en html5boilerplate_.

El sitio esta diseñado para que sea responsivo basado en media queries, no se piensa utilizar frameworks responsivos
para un sitio tan pequeño como esté, además sirve que practican su css-fu.

Archivos estáticos
------------------

Los archivos que sean entregados de forma directa por el servidor están contenidos dentro de ``pymty/static/``, esto es principalmente javascript, css e imágenes.

Controladores/Vistas Web
-------------------------

El sitio utiliza CherryPy para el mapeo de URL a métodos de objetos. El enrutamiento es por `recorrido de objetos`_, el cual
es el método más común para construir aplicaciones en CherryPy_.

De momento todo esto se encuentra definido en ``pymty/pymty/views/main.py`` donde hace uso de el decorador
``cherrypy.tools.mako`` el cual esta definido en ``pymty/pymty/cptools/makotemplates.py`` este simplemente relacionada
plantillas con los métodos que se invocan, los cuales solamente regresan diccionarios que son usados en las plantillas.


Contribuir cambios
==================

Se recomienda el flujo de trabajo común de GitHub: clonar, modificar, push request. En caso de que seas un contribuyente frecuente se te ofrecerá
el acceso para subir cambios de forma directa.

Para más información de hacia donde va el sitio consulta el directorio ``docs``.


.. _Mako: https://www.makotemplates.org/
.. _CherryPy: https://cherrypy.dev/
.. _`recorrido de objetos`: https://docs.cherrypy.dev/en/latest/tutorials.html#tutorial-1-a-basic-web-application
.. _html5boilerplate: https://html5boilerplate.com/
.. _Nix: https://nixos.org/download.html
.. _poetry: https://python-poetry.org/
