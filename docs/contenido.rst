Árbol de contenido
==================
El árbol de contenido se presenta en varias formas dependiendo el alcance o iteración a buscar.

Primera iteración
------------------
:/reuniones:
   Presenta una descripción sobre lo que son, una liga a la reunión más próxima y ligas a series de reuniones
   con fines particulares, como por ejemplo tracks para principiantes, cursos en secuencia y el circulo virtuoso.

:/documentacion:
   Un listado de ligas a documentos sobre python en concreto. De preferencia en español.

:/contribuir:
   Una introducción de el por que el grupo necesita de tu contribución y las formas de como puedes ayudar.

:/comunidades:
   Muestra un listado de las comunidades cercanas al grupo con liga a su sitio.

:/trabajos:
   Muestra el listado de trabajos que se captura de forma manual desde la consola de AppEngine y un correo a donde pueden enviar los trabajos a publicar
   trabajos en pymty.org

Segunda iteración
-----------------

Reuniones
..........
:/reuniones/historial:
   Muestra el listado de las reuniones anteriores.

:/reuniones/historial/<identificador>:
   Muestra en particular lo relevante a una reunión en particular, esto puede ser estilo minuta, lista de documentos
   que se expusieron o ligas de interés para referencia al futuro.

Contribuir
..........
:/contribuir:
   Extiende al de la etapa uno mas la ligas a las subsecciones.

:/contribuir/platica:
   Breve descripción sobre lo que implica dar una platica.
   Muestra un formulario con los siguientes campos:

       - Nombre
       - Email
       - Teléfono (opcional)
       - Tema
       - Fecha tentativa
       - Tiempo para exponer
       - Serie de platicas (opcional): Esto es por si se usan tracks de charlas y agrupar por nivel o tema.
       - Comentarios

:/contribuir/lugar:
   Breve descripción sobre lo que implica ofrecer un lugar.
   Muestra un formulario con los siguientes campos:

       - Nombre
       - Email
       - Teléfono (opcional)
       - Disponibilidad (textarea): Fechas y horas
       - Tipo de platica a hospedar (select): [Social|Técnica|Cualquier tipo]
       - Capacidad de personas
       - Dirección (textarea)
       - Comentarios (textarea)

:/contribuir/coordinar:
   Breve descripción sobre lo que implica coordinar un evento.
   Muestra un formulario con los siguientes campos:

       - Nombre
       - Email
       - Teléfono (opcional)
       - Disponibilidad (textarea): Fechas y horas
       - Tipo de platica a coordinar (select): [Social|Técnica|Cualquier tipo]
       - Zona de la ciudad (textarea)
       - Comentarios (textarea)

:/contribuir/website:
   Breve descripción sobre lo que implica desarrollar el sitio web.
   Muestra un formulario con los siguientes campos:

       - Nombre
       - Email
       - Usuario de github
       - Áreas donde te gustaría ayudar (textarea)

Comunidades
............
:/comunidades:
   Extiende a la etapa uno, agrega un logo y liga a su sitio en conjunto con una liga para ver más detalles.

:/comunidades/<identificador>:
   Muestra la vista detallada de la otra comunidad.

Bolsa de trabajo
................
:/trabajos:
   Muestra un header donde menciona la razón de la bolsa de trabajo, luego lo sigue
   un listado de los trabajos activos. A mi parecer el paginado no es necesario
   dado el volumen de trabajos que se estiman tener de forma simultanea.

   La bolsa de trabajo no tiene noción de cuentas de empleador, ni sirve de mediador
   entre los interesados, simplemente es un recurso que ayuda a publicitar una vacante
   que es afín a los intereses de el grupo.

   Los trabajos deben de tener campos para ser moderados y un tiempo de expiración automático
   con la posibilidad de ser editado a convenir.

   Muestra una liga para agregar un nuevo trabajo.

:/trabajos/agregar:
   Muestra un formulario con los siguientes campos:

       - Nombre de (empresa/proyecto/persona)
       - Email
       - Teléfono (opcional)
       - Titulo
       - Descripción (textarea)

   Al guardar se enviará un correo con un uuid, además de mostrarlo en pantalla en
   conjunto con un a liga par ir a la vista de el trabajo.

:/trabajos/editar/<id-de-trabajo>:
   Primero valida que exista un cookie donde esta el uuid en caso de que no este
   redirecciona a ``/trabajos/autorizar/<id-de-trabajo>``. En caso de que si este
   muestra los campos de el formulario de agregar.

:/trabajos/autorizar/<id-de-trabajo>:
   Muestra el formulario para asignar el uuid en la sesión.
   Si asigna otra que no es la correcta muestra un mensaje de error y vuelve a preguntar por el uuid.
   En caso de que sea el correcto redirecciona a ``/trabajos/editar/<id-de-trabajo>``.


:/trabajos/ver/<identificador>:
   Muestra el trabajo en particular con los campos que se capturaron previamente.
   Muestra una liga de editar a ``/trabajos/editar/<id-de-trabajo>``.

Tercera iteración
------------------
:/reuniones/historial/<identificador>:
   Extiende a la etapa uno solo que ahora muestra una lista de documentos
   que se expusieron.

:/reuniones/docs/<identificador>:
   El documento que se relaciona directamente a una reunión, solo se usa de forma implícita en la vista de la reunión.

Agregar la noción de usuarios unificado a todo el sitio, para relacionar expositores, organizadores, contribuyentes,
empleadores y roles particulares para la bolsa de trabajos.

Se busca además integrar el sitio con el API de meetup, idealmente utilizando OAuth de meetup para loggearse en el sitio.

*Aún tiene mucho por definir esta parte.*
