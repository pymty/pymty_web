#################################
Sitio público de Python Monterrey
#################################

Introducción
============

Cómo forma de facilitar el acceso a las distintas partes que conforman al grupo de Python Monterrey surge la iniciativa de
centralizar por medio de un sitio web completo, originalmente se pensó que bastaría solamente con el sitio en meetup, pero
las recurrentes solicitudes a aspectos particulares sentaron la base para comenzar este sitio.

El dominio oficial de el sitio es: http://www.pymty.org

La ultima versión es visible en: http://pymty-web.appspot.com

Requisitos
==========

Python 2.7, Mako_, CherryPy_ y el `Google App Engine SDK`_.


Cómo ejecutar el sitio
======================

* Instalar `Google App Engine SDK`_  para **Python**
* Dentro de el directorio raíz del repositorio:
 * Ejecuta el script ``mkenv.sh``. De momento no tenemos una solución automática para windows.
 * Para ejecutar en el servidor local la aplicación usa: ``dev_appserver.py  --host 0.0.0.0 pymty``.

Estructura general
==================

Plantillas
----------

Todo lo que refiere a HTML esta contenido en ``pymty/pymty/templates`` utiliza Mako_ para la manipulación de plantillas.
La estructura esta basada en html5boilerplate_, utiliza `responsive mobile menu`_ y css directo.

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

Subir cambios a AppEngine
-------------------------

La aplicación esta relacionada directamente a cuentas de google, por lo que implica autorizar al usuario que quiera subir la aplicación, en caso de que
quieras subirla de forma individual puedes hacerlo con el comando ``appcfg.py update pymty/``.

Contribuir cambios
==================

Se recomienda el flujo de trabajo común de GitHub: clonar, modificar, push request. En caso de que seas un contribuyente frecuente se te ofrecerá
el acceso para subir cambios de forma directa.

Para más información de hacia donde va el sitio consulta el directorio ``docs``.

Notas
=====

* Tristemente usa Python 2.7 por que AppEngine aún no funciona con Python 3.
* virtualenv es meramente utilizado para facilitar la obtención de dependencias, siempre se puede bajar el módulo directamente y desempaqueta dentro de `pymty`.
* ``dev_appserver.py`` es parte de el SDK de python para el Google App Engine.
* La razón de por que no usamos bien distutils, virtualenv y las herramientas estándar de python es por la forma de montar las aplicaciones en AppEngine.
  Donde básicamente es poner todas tus dependencias en el directorio de la aplicación, ya sea directamente o con una liga simbólica.
* La aplicación decidí hacerla para AppEngine con el fín de que fuera practicamente gratis con el tráfico esperado y de paso hacerla un poco más interesante.


.. _`Google App Engine SDK`: https://cloud.google.com/appengine/downloads
.. _Mako: http://www.makotemplates.org/
.. _CherryPy: http://www.cherrypy.org/
.. _`recorrido de objetos`: http://docs.cherrypy.org/en/latest/tutorials.html#tutorial-1-a-basic-web-application
.. _html5boilerplate: http://html5boilerplate.com/
.. _`responsive mobile menu`: http://responsivemobilemenu.com/
