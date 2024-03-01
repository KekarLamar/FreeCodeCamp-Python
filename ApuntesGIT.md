Vale ya hemos estado jugando con ello desde VS code y hemos visto un problema de usar solo los comandos que trae en vez de la terminal. Cuando hemos eliminado una rama desde el repositorio el git local no dejaba de apuntar allí y ese no la borra. Hemos descubierto dos términos nuevos "push" que es para mandarlo al github y para traerte lo del repositorio github usas "pull". El "fetch" que es traerte lo que tengas del github pero todo el repositorio, lo anterior es a nivel de ramas ya sea la main u otras.

	• Hay que controlar el GitHub desde el local a través de la terminal con eso no hay fallos vamos a hacer una recopilación de los comandos más importantes. 
	• Lo primero de todo es tener en tu local una carpeta con tu git. ESTA ES LA FORMA DE LOCAL AL REPOSITORIO PERO ES MEJOR HACER EL REPO EN GITHUB Y CLONARLO EN LA CARPETA QUE QUIERES (desde la terminal de vs code)
		○ git init (esto es del local al remoto)
		○ cd ruta de la carpeta // git clone HTTPS (esto del remoto al local)
	• El primero que tenemos que saber es como conectarlo al github
		○ git remote add origin <URL> (esto es del local al remoto)
	• Puede ser que el nombre de tu rama ponga master pero hay que forzarla para que se llame main
		○ git branch -M main
	• Para actualizar el nombre de local "main" al del repositorio github
		○ git push -u origin main
	• Cuando llevemos a cambio modificaciones los pasos son añadirlo al stage, luego commit y después push. Los cambiamos solo los estamos guardando en la principal
		○ git add.
		○ git commit -m "Comentario"
		○ git push -u origin main (-u identifica la rama remota como la principal, con hacerlo la primera vez ya vale)
	• Vale cuando queremos crear una ramita
		○ git checkout -b NombreRamita
	• En la ramita los pasos para guardar las modificaciones son los mismos el add y luego commit. El tema es que en vez de push volvemos a la rama principal. Vale esto fue por el tutorial pero el pusheo sería igual
		○ git checkout main
	• Puedes checkear todas las ramitas con este comando
		○ git branch
	• Para mergear la ramita con la principal desde local
		○ git merge NombreRamita (esto una vez que has vuelto a la pricipal)
		○ (actualizas la main como antes) git push -u origin main
	• Vale y por último para que tu repositorio lo tengas en cualquier ordenador es lo que se llama hacer pull y es tan sencillo como abrir el código y copiar el HTTPS y escribir:
		○ git clone HTTPS
		
		
Ahora como crear carpetas, no tiene mucho solo la creas de vs Code o desde la propia carpeta local y metes todo lo que quieras dentro. 

Ahora el ritmo de trabajo va a ser lo siguiente, todo lo que haga en local y quiera tenerlo en remoto PUSH, todo lo que tenga en Remoto y quiera tenerlo en el local PULL

	• git push origin RAMA
	• git pull origin RAMA

