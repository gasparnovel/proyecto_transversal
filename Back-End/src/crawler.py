import urllib.request
list_links = []
keys = ['webpage', 'links']
values = []
total = {}


def get_html(url):  # Transforma el html en un string
    try:    # Intenta convertir el html en un string
        request = urllib.request.urlopen(url)
        page = request.read().decode('utf-8')
        return page
    except:         # Si no consigue procesarlo, dice que ha ido mal
        print('No es posible leer el url')


def get_all_links(page):
    # Crea una lista con todos los enlaces de html
    page = get_html(page)  # Llama a la funcion para transformarlo en un string
    while True:
        url, endpos = get_next_target(page)
        if url:
            # Como hay enlaces que llevan a un apartado concreto de otro
            # html, los descartamos
            if '#' in url or url in list_links or '..' in url:
                page = page[endpos+1:]
                continue
            else:
                # Añade el url a la lista con los links
                list_links.append(url)
                # Devuelve el HTMl a partir de end_quote, que es la posición donde
                # acaba el HTML
                page = page[endpos:]
        else:
            break
    assert len(list_links) > 0
    return list_links


def get_next_target(page):
    # Dentro de la página que se le da, busca todos los
    # enlaces
    assert type(page) is str
    # star_link define donde empieza la etiqueta HTML del enlace
    start_link = page.find("<a href")
    if start_link == -1:
        # Si no hay ningún enlace, devuelve esto
        return None, 0
    # start_quote marca donde empieza el enlace, en este caso dentro del HTMl sería
    # despues de 'src='
    start_quote = page.find('"', start_link + 1)
    # end_ quote marca donde termina el enlace
    end_quote = page.find('"', start_quote + 1)
    # el url sería el texto que hay entre las comillas de 'src='
    url = page[start_quote + 1: end_quote]
    # Devuelve el url para meterlo en list_links y el final del url para seguir
    # buscando el siguiente url desde esa posición
    return url, end_quote


# Crea una 'webpage' para despues checkear los html
# uno a uno)
def get_webpage(link):
    if type(link) is str:
        final = link.rfind("/")  # Busca la última '/'
        webpage = link[0:final + 1]  # Webpage es el url hasta la ultima '/'
        return webpage
    else:
        return ''


# Crea un diccionario con la 'webpage' (hasta el úlimo '/' y
# la lista de links para después checkear que html tiene
# los productos)
def crawler(page):
    values = [get_webpage(page), get_all_links(page)]
    total = dict(zip(keys, values))
    assert type(total) is dict
    return total


if __name__ == "__main__":
    assert get_webpage("hola/que") == "hola/"
    assert get_next_target('<a href>') == ('<a href', -1)
    assert get_all_links(
        "file:///C:/proyecto_transversal/Front-End/html/Inicio.html")
