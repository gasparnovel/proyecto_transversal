from src.crawler import get_webpage
from src.crawler import get_next_target
import pytest


def test_basico_webpage():
    assert get_webpage([]) == ''


def test_barra():
    assert get_webpage('/') == '/'


def test_sin_barra():
    assert get_webpage('hola') == ''


def test_texto():
    assert get_webpage('hola/') == 'hola/'
    assert get_webpage('hola/que') == 'hola/'


def test_varias_barras():
    assert get_webpage('hola/que/tal') == 'hola/que/'


def test_basico_target():
    assert get_next_target('') == (None, 0)


def test_next_target():
    assert get_next_target('<a href>') == ('<a href', -1)
    assert get_next_target('<a href> "hola"') == ('hola', 14)
    assert get_next_target('<a href src= "hola">') == ('hola', 18)


def test_varios_target():
    assert get_next_target(
        '<a href src= "hola"> <a href src= "hola"') == ('hola', 18)
