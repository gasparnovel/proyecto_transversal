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
    # Llama a la función para saber qué HTML tiene los productos
    page = get_html_products(page)
    while True:
        # Devuelve el producto para insertarlo en la lista y la posición donde acaba
        producto, endpos = get_next_product(page)
        if producto:
            if producto in lista_productos:
                # Si el producto ya está en la lista, sigue buscando
                page = page[endpos+1:]
                continue
            else:
                # Si el producto no está en la lista, lo añade
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
            # Si no hay ningún producto, devuelve esto
            return None, 0
        # star_tag busca donde acaba la etqueta HTML dónde está el producto
        start_tag = page.find('>', start_product + 1)
        # end_tag busca dónde acaba la etiqueta HTML del Producto
        end_tag = page.find('</div>', start_tag + 1)
        producto = page[start_tag + 1: end_tag]
        # Devuelve el producto para insertarlo en la lista de productos y
        # dónde acaba la etiqueta del producto para buscar el siguiente
        return producto, end_tag
    return ''
