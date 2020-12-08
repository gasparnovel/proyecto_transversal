from crawler import crawler
import urllib.request
# page = "http://127.0.0.1:5500/Front-End/html/Inicio.html"


def get_html_products(page):
    # Busca cual de los html de list_links
    # es el html con los productos
    total = crawler(page)
    contador = 0
    while contador < len(total['links']):
        url = total['webpage'] + total['links'][contador]
        request = urllib.request.urlopen(url)
        page = request.read().decode('utf-8')
        if page.find('class="producto"') == -1:
            contador += 1
        else:
            contador = len(total['links'])
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
