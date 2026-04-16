# taller_formularios_nombre_estudiantes

## Taller 2 Django
En parejas, crear un proyecto en Django, bajo el nombre **taller_formularios_nombre_estudiantes**. En el proyecto se deben diseñar dos aplicaciones independientes, denominadas **asistencia y solicitudes**, las cuales deben registrarse en el archivo de configuración settings.py. En la aplicación **asistencia**, será necesario desarrollar un modelo denominado Asistencia y asociarlo a un formulario que permita la captura de los siguientes campos:
- **Nombre completo:** campo de texto de hasta 150 caracteres.
- **Documento de identidad:** campo de texto alfanumérico.
- **Correo electrónico:** campo de tipo email.
- **Fecha de asistencia:** campo de tipo fecha.
- **Hora de ingreso:** campo de tipo hora.
- **Hora de salida:** campo de tipo hora.
- **Presente:** campo de tipo booleano que confirme la asistencia.
- **Observaciones:** campo de texto libre opcional.

En la aplicación **solicitudes**, será necesario diseñar un modelo denominado
Solicitud que esté asociado a un formulario con los siguientes campos:

- **Nombre del solicitante:** campo de texto de hasta 150 caracteres.
- **Documento de identidad:** campo de texto alfanumérico.
- **Correo electrónico:** campo de tipo email.
- **Teléfono de contacto:** campo numérico.
- **Tipo de solicitud:** campo de selección entre varias opciones (ejemplo:
académica, administrativa, técnica, otra).
- **Asunto:** campo de texto corto.
- **Descripción detallada:** campo de texto largo.
- **Fecha de la solicitud:** campo de tipo fecha.
- **Archivos adjuntos (opcional):** campo de carga de archivo.  

Cada formulario deberá implementarse mediante la clase ModelForm de Django, de manera que los datos registrados se integren correctamente a la base de datos. Será indispensable desarrollar vistas que permitan la visualización de los formularios y la recepción de los datos enviados a través del método POST. Tras la validación de
la información, los registros deberán almacenarse y el sistema tendrá que redirigir a una página de confirmación donde se muestre un mensaje de éxito.  
La configuración de rutas en el proyecto principal deberá enlazar correctamente los accesos de ambas aplicaciones. La aplicación asistencia deberá contar con una ruta para presentar el formulario de registro con los campos descritos y otra ruta destinada a la visualización de la confirmación. De manera análoga, la aplicación solicitudes deberá incluir una ruta para el formulario de solicitud y otra para el mensaje de confirmación de envío.  
Por último, será necesario crear las plantillas correspondientes (diseño libre) para cada aplicación, garantizando que los formularios se representen de forma clara y completa, junto con sus páginas de confirmación. Una vez finalizado el desarrollo, se deberá ejecutar el servidor de Django y verificar mediante pruebas funcionales que los registros se almacenen de manera correcta en la base de datos, siendo posible su consulta a través del panel de administración del framework.