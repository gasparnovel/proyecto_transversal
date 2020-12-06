import urllib.request
from get_products import lista_productos
productos_sin_hmtl = []


def remove_space(lista):
    lista_limpia = []
    for item in lista_productos:
        item = item.replace('\r', '')
        item = item.replace('\n', '')
        item = item.replace('  ', '')
        lista_limpia.append(item)
    assert len(lista_limpia) == 13
    return lista_limpia


def remove_html(lista):
    lista = remove_space(lista)
    tag = False
    quote = False
    # productos_sin_hmtl = []
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
        # return out
        productos_sin_hmtl.append(out)
    assert len(productos_sin_hmtl) == 13
    return productos_sin_hmtl


print(remove_html(lista_productos))
# print(remove_space(lista_productos))
# print(productos_sin_hmtl)
# print(len(productos_sin_hmtl))
