import urllib
from remove_html import productos_sin_hmtl


def get_keys(texto):
    if ':' in texto:
        texto = ''
        return texto
    else:
        return texto


if __name__ == "__main__":
    assert get_keys(':') == ('')
    assert get_keys('h') == ('h')
