import urllib.request
import urllib.parse


x = urllib.request.urlopen(
    "file:///C:/Proyecto_transversal/proyecto_transversal/Front-End/html/Inicio.html")
print(x.read())

# url = "file:///C:/Proyecto_transversal/proyecto_transversal/Front-End/html/Inicio.html"

# values = {}
