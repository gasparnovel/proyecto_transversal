import urllib
from remove_html import remove_html


def make_dictionary(page):
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
            todos_productos.append(diccionario)
        else:
            return lista
    return todos_productos


# print(make_dictionary(
    # "file:///C:/Proyecto_transversal/proyecto_transversal/Front-End/html/Inicio.html"))


if __name__ == "__main__":
    assert make_dictionary([':']) == []
    assert make_dictionary(['h']) == ['h']
    assert make_dictionary(['h:']) == ['h']
    assert make_dictionary(['h: q']) == [{'h': 'q'}]
    assert make_dictionary(['h: q m: u']) == [{'h': 'q', 'm': 'u'}]
    assert make_dictionary(['h: q', 'm: u']) == [{'h': 'q'}, {'m': 'u'}]
