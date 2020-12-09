import urllib
from .remove_html import remove_html


def make_dictionary(page):
    # En este módulo entra el url y saca una lista de diccionarios
    # de los productos
    lista = remove_html(page)
    assert type(lista) is list
    todos_productos = []
    for item in lista:
        separador = ':'
        keys = []
        values = []
        if item == separador:
            return []
        if item.count(separador) == 1 and item[-1] == separador:
            key = item.replace(separador, '')
            keys.append(key)
            return keys
        if item.count(separador) >= 1:
            item = item.split()
            for word in item:
                if separador in word:
                    word = word.replace(':', '')
                    keys.append(word)
                else:
                    values.append(word)
            diccionario = dict(zip(keys, values))
            assert type(diccionario) is dict
            todos_productos.append(diccionario)
        else:
            return lista
    assert len(todos_productos) == len(lista)
    assert type(todos_productos) is list
    return todos_productos


if __name__ == "__main__":
    assert make_dictionary([':']) == []
    assert make_dictionary(['h']) == []
    assert make_dictionary(['h:']) == []
    assert make_dictionary(['h: q']) == [{'h': 'q'}]
    assert make_dictionary(['h: q m: u']) == [{'h': 'q', 'm': 'u'}]
    assert make_dictionary(['h: q', 'm: u']) == [{'h': 'q'}, {'m': 'u'}]
