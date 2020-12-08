from make_dictionary import make_dictionary


def run(page):
    try:
        return make_dictionary(page)
    except:
        print('No es un url válido')
