import urllib
from remove_html import productos_sin_hmtl


def get_keys(texto):
    keys = []
    for item in texto:
        if ':' == item:
            item = ''
            return item
        if ':' in item:
            separador = item.find(':')
            item = item[0:separador]
            keys.append(item)
            return keys
        else:
            return item


if __name__ == "__main__":
    assert get_keys(':') == ''
    assert get_keys('h') == 'h'
    assert get_keys('h:') == 'h'
    assert get_keys('h: a') == 'h'
    assert get_keys(['h:']) == ['h']
