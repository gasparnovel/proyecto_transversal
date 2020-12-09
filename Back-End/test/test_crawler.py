from src.crawler import get_webpage
import pytest


def test_basico():
    assert get_webpage([]) == ''


def test_barra():
    assert get_webpage('/') == '/'


def test_sin_barra():
    assert get_webpage('hola') == ''
