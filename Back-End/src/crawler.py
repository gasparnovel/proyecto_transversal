import urllib.request
list_links = []
keys = ['webpage', 'links']
values = []
total = {}


def get_html(url):  # Transforma el html en un string
    try:
        request = urllib.request.urlopen(url)
        page = request.read().decode('utf-8')
        return page
    except:         # Si no consigue procesarlo, dice que ha ido mal
        print('No es posible leer el url')


def get_all_links(page):
    # Crea una lista con todos los enlaces de html
    page = get_html(page)
    while True:
        url, endpos = get_next_target(page)
        if url:
            if url == '#' or url in list_links:
                page = page[endpos+1:]
                continue
            else:
                list_links.append(url)
                page = page[endpos:]
        else:
            break
    assert len(list_links) > 0
    return list_links


def get_next_target(page):
    # Dentro de la página que se le da, busca todos los
    # enlaces
    assert type(page) is str
    start_link = page.find("<a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link + 1)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote


# Crea una 'webpage' para despues checkear los html
# uno a uno)
def get_webpage(link):
    if type(link) is str:
        final = link.rfind("/")
        webpage = link[0:final + 1]
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
