import urllib
from remove_html import productos_sin_hmtl


def make_dictionary(lista):
    if lista == ':':
        return ''
    else:
        return lista


if __name__ == "__main__":
    assert make_dictionary(':') == ''
    assert make_dictionary('h') == 'h'
