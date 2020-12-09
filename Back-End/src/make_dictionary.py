import urllib
from .remove_html import remove_html


def make_dictionary(page):
    # En este módulo entra el url y saca una lista de diccionarios
    # de los productos
    lista = remove_html(page)  # Llama a esta funcion para quitar el HTML
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
            # Se separa cada item para crear una lista de este item
            item = item.split()
            for word in item:
                # Mira cada palabra de item (que ahora es una lista) si tiene ':'
                if separador in word:
                    # Si tla palabra tiene un ':', es que será una clave (ejemplo -> 'Marca:')
                    word = word.replace(':', '')
                    keys.append(word)
                else:
                    # Si en la palabra no está ':',  será un valor (ejemplo -> 'Droide')
                    values.append(word)
            # Crea un diccionario con las claves y valores del item
            diccionario = dict(zip(keys, values))
            assert type(diccionario) is dict
            # Añade el diccionario a la lista con todos los productos y pasa al siguiente
            # item da lista de los productos
            todos_productos.append(diccionario)
        else:
            return lista
    # Comprueba que todos_productos tenga la misma longitud que la lista de productos
    assert len(todos_productos) == len(lista)
    # Comprueba que todos_productos es una lista, en este caso una lista de diccioanrios
    assert type(todos_productos) is list
    # Devuelve la lista de diccionarios
    return todos_productos


if __name__ == "__main__":
    assert make_dictionary([':']) == []
    assert make_dictionary(['h']) == []
    assert make_dictionary(['h:']) == []
    assert make_dictionary(['h: q']) == [{'h': 'q'}]
    assert make_dictionary(['h: q m: u']) == [{'h': 'q', 'm': 'u'}]
    assert make_dictionary(['h: q', 'm: u']) == [{'h': 'q'}, {'m': 'u'}]
