import urllib
from remove_html import productos_sin_hmtl


def make_dictionary(lista):
    assert type(lista) is list
    separador = ':'
    keys = []
    values = []
    todos_productos = []
    for item in lista:
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


if __name__ == "__main__":
    assert make_dictionary([':']) == []
    assert make_dictionary(['h']) == ['h']
    assert make_dictionary(['h:']) == ['h']
    assert make_dictionary(['h: q']) == [{'h': 'q'}]
    assert make_dictionary(['h: q m: u']) == [{'h': 'q', 'm': 'u'}]
