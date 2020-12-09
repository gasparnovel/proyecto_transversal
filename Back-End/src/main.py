from .make_dictionary import make_dictionary
# run("file:///C:/proyecto_transversal/Front-End/html/Inicio.html")
# page = "file:///C:/proyecto_transversal/Front-End/html/Inicio.html"


def run(page):
    return make_dictionary(page)


if __name__ == "__main__":
    assert run("file:///C:/proyecto_transversal/Front-End/html/Inicio.html")
