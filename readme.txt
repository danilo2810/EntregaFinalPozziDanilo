-Se parte como base de la plantilla "https://startbootstrap.com/theme/landing-page"
-Se cuenta con 2 Apps, una que gestiona usuarios, y mensajes y otra que contiene los Post
-Se cueta con un modelo Perfil que contiene la informacion de perfil de cada usuario con una clave foranea para eliminar el perfil si se elimina el usuario 
-Se cuenta con un modelo Mensajes que contiene el emisor, receptor, cuerpo de mensjae y estado (Leido, no leido) NO cuenta con clave foranea al eliminar el usuario emisor o receptor el mensaje siempre permanecera
-Se cuenta con un modelo Post que contiene toda informacion del post y su clave foranea es user para que se eliminen todos los post del usuario.

-La navBar tiene 2 formas, una con usuario sin ingresar y una con un usuario y contraseña.
-NavBar 
	-usuario sin ingresar:
		Inicio: se muestra el nombre del blog, una pequeña descripcion del mismo y los 3 post que fueron editados ultimamnete.
		Post: Solo puede ver el titulo, subtitulo, dueño del post y la ultima modificacion. para ver mas debe registrarse o ingresar.
		Registro: Muestra un formulario de registro con usuario, email y contraseña
		Login: Muestra un formulario de ingreso con usuario y contraseña.
		Acerca de mi: Hay una descripcion del creador de la pagina con foto.
	-usuario logueado 
		Al momneto de la entrega se cuentan con 3 usuarios (Julieta, JuanIgnacio, Pedro) y su contraseña es qqqQQQ_111. Se creara el usuario Ana con la misma contraseña en el video.
		Inicio: se muestra el nombre del blog, una pequeña descripcion del mismo y los 3 post que fueron editados ultimamnete.
		Post: En esta pestaña se pueden ver los post creados por el usuario y tambien todos los post creados en el blog. La diferencia incide en que hay un buscador por titulo de post.
		Mis Post: En esta seccion se pueden editar los post creados haciendo click en el titulo o crear uno nuevo completando el formulario.
			Al hacer click en editar post, aparece un formulario en el cual se pueden realziar los cambios necesarios o ELIMINAR el post
		Ver Perfil: En esta seccion se puede modificar el perfil o ELIMINAR el mismo
		N° Buzon: el N° indica la cantidad de mensajes sin leer que tiene el usuario, al hacer click se ingresa a la seccion mensajes que tiene en la columna izquierda los mensajes, tanto leido como 
			  no leidos. Al hacer click en un mensaje, aparece el cuerpo del mismo en la columna derecha junto con un boton responder y se marca el mensaje como leido.
			Por ultimo en la parte inferior se tiene un formulario para enviar mensajes
		Logout: Salir del usuario
		Acerca de mi: Hay una descripcion del creador de la pagina con foto.
