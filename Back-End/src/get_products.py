from .crawler import crawler
import urllib.request
# page = "file:///C:/proyecto_transversal/Front-End/html/Inicio.html"


def get_html_products(page):
    # Busca cual de los html de list_links
    # es el html con los productos
    total = crawler(page)
    contador = 0  # Especifica que valor de 'links' tiene que buscar
    while contador < len(total['links']):
        # La url se forma a partir de 'webpage' y el valor de 'links'
        url = total['webpage'] + total['links'][contador]
        # Transforma el url en un string
        request = urllib.request.urlopen(url)
        page = request.read().decode('utf-8')
        if page.find('class="producto"') == -1:
            # Busca que en el string (el html del url) contenga 'class="producto"'
            # para saber si en esta página hay productos
            contador += 1  # Si no hay productos, sigue con el siguiente url
        else:
            # Si encuntra 'class="producto"' en el html lo devuelve para empezar
            # a buscar los productos
            contador = len(total['links'])
            # el contador coge el valor de la ongitud del valor de 'links' para acabar el While
            return page
    return page


def get_all_products(page):
    # Crea una lista con todos los productos
    lista_productos = []
    page = get_html_products(page)
    while True:
        producto, endpos = get_next_product(page)
        if producto:
            if producto in lista_productos:
                page = page[endpos+1:]
                continue
            else:
                lista_productos.append(producto)
                page = page[endpos:]
        else:
            break
    assert len(lista_productos) > 0
    return lista_productos


def get_next_product(page):
    # Dentro del html con los productos, busca cada
    # producto a partir de 'class="producto"'
    if type(page) is str:
        start_product = page.find('class="producto"')
        if start_product == -1:
            return None, 0
        start_tag = page.find('>', start_product + 1)
        end_quote = page.find('</div>', start_tag + 1)
        producto = page[start_tag + 1: end_quote]
        return producto, end_quote
    return ''
