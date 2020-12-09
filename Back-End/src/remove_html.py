import urllib.request
from .get_products import get_all_products
productos_sin_hmtl = []


def remove_space(lista):
    # Por cada item de la lista, lo limpia de marcas que puedan dar fallos
    assert type(lista) is list
    lista_limpia = []
    for item in lista:
        # Quita todos los dobles espacio, los '\n' y '\r' que dan fallos
        # en remove_html
        item = item.replace('\r', '')
        item = item.replace('\n', '')
        item = item.replace('  ', '')
        # Añade cada item limpio en una nueva lista
        lista_limpia.append(item)
    # Comprueba que la lista antigua y la nueva tengan la misma longitud
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
        # Quita las marcas HTML de cada item de la lista
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
                # Si el carácter no está dentro de un etiqueta, se añade a 'out'
                out = out + c
        # Comprueba que en 'out' no haya ninguna '<', si devuelve 'out' con
        # alhúm '<', ha fallado el código
        assert out.find('<') == -1
        # Cuando todo el item de la lista está sin etiquetas, se inserta en la lista
        # de los productos
        productos_sin_hmtl.append(out)
    # Comprueba que la lista de los productos sin HTML tenga la misma longitud que que la lista que entra
    assert len(productos_sin_hmtl) == len(lista)
    return productos_sin_hmtl


if __name__ == "__main__":
    assert remove_space(['  ']) == ['']
    assert remove_space(['\n']) == ['']
    assert remove_space(['\r']) == ['']
