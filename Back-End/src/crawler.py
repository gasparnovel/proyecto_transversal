import urllib.request
list_links = []
page = "file:///C:/Proyecto_transversal/proyecto_transversal/Front-End/html/Inicio.html"


def get_html(url):
    request = urllib.request.urlopen(url)
    page = request.read().decode('utf-8')
    return page


def get_all_links(page):
    page = get_html(page)
    while True:
        url, endpos = get_next_target(page)
        if url:
            if url == '#' or url in list_links or ".." in url:
                page = page[endpos+1:]
                continue
            else:
                list_links.append(url)
                page = page[endpos:]
        else:
            break
    return list_links


def get_next_target(page):
    start_link = page.find("<a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link + 1)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

    # print(gethtml("file:///C:/Proyecto_transversal/proyecto_transversal/Front-End/html/Inicio.html"))
print(get_all_links(page))
