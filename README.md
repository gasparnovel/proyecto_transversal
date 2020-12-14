# GO-GO UFO

![Logo GO-GO UFO](./Front-End/imagenes/Logo.PNG)

### Definición general proyecto

Los retos principales de este proyecto consiste en crear una sitio web funcional, diseñar un programa de _Web Scrapping_ que pueda almacenar la información de los productos que se encuentren en el sitio web en una base de datos.

### Utilización

Lo primero que deberíamos hacer para inicializar el programa es isntalar un entorno virutal de Python en la ruta que deseemos. Este ejemplo es para Windows.

```
python -m venv /ruta/hasta/el/entorno/vitual
```

Una vez creado el entorno virtual, creamos el directorio en el cual copiaremos el proyecto.

```
md ./web_scrapping
```

Ahora clonamos el repositorio:

```
git clone https://github.com/Alopezmur/proyecto_transversal.git
```

Iniciamos el entorno virtual e instalamos las dependencias.

```
python -m venv venv
.\venv\Scripts\activate
(venv) pip install -r requirements.txt
```

Una vez instaladas ls dependencias e iniciado el entorno virtual, podemos probar el programa. Lo primero es lanzar python.

```
python
```

Depués importamos la función `run` de `main.py`.

```
>>> from ruta.hasta.main import run
```

Ahora solo queda probar la aplicación a ver si devuelve una lista de diccionarios con los productos del sitio web.

```
run(ruta/hasta/el/sitio/web)
*run("file:///C:/proyecto_transversal/Front-End/html/Inicio.html")*
```

### Autores y contribuciones

Autores: Alejandro López y Gaspar Novel

Gracias a algunos profesores del Dual por la ayudada brindada.
