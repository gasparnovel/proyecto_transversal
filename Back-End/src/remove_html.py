import urllib.request
from get_products import get_all_products
productos_sin_hmtl = []


def remove_space(lista):
    # Por cada item de la lista, lo limpia de marcas que puedan dar fallos
    lista_limpia = []
    for item in lista:
        item = item.replace('\r', '')
        item = item.replace('\n', '')
        item = item.replace('  ', '')
        # Añade cada item limpio en una nueva lista
        lista_limpia.append(item)
    assert len(lista_limpia) == len(lista)
    return lista_limpia


def remove_html(page):
    if type(page) is not str:
        return []
    # invoca esta funcion para coger los productos del hmtl
    lista = get_all_products(page)
    # limpia el html de espacios y otras marcas que puedan provocar un error
    lista = remove_space(lista)
    tag = False
    quote = False
    productos_sin_hmtl = []
    for item in lista:
        out = ""
        for c in item:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag and not quote:
                quote = c
            elif c == quote:
                quote = False
            elif not tag:
                out = out + c
        assert out.find('<') == -1
        productos_sin_hmtl.append(out)
    assert len(productos_sin_hmtl) == 13
    return productos_sin_hmtl
