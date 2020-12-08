import urllib
from remove_html import productos_sin_hmtl


def get_keys(texto):
    keys = []
    dos_puntos = ':'
    for item in texto:
        if ':' == item:
            item = ''
            return item
        if item.count(dos_puntos) == 1 and len(texto) == 1:
            separador = item.find(':')
            item = item[0:separador]
            keys.append(item)
            return keys
        if item.count(dos_puntos) == 1:
            separador = item.find(':')
            item = item[0:separador]
            keys.append(item)
            continue
        if item.count(dos_puntos) > 1:
            separador = item.find(':')
            key = item[0:separador]
            keys.append(key)
        else:
            return item
    return keys


if __name__ == "__main__":
    assert get_keys(':') == ''
    assert get_keys('h') == 'h'
    assert get_keys('h:') == 'h'
    assert get_keys('h: a') == 'h'
    assert get_keys(['h:']) == ['h']
    assert get_keys(['h:', 'a:']) == ['h', 'a']
    assert get_keys([' hola: que tal marca: droide']) == ['hola', 'marca']
