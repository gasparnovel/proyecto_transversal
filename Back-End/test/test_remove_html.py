from src.remove_html import remove_space
import pytest


def test_espacios():
    assert remove_space(['  ']) == ['']


def test_n():
    assert remove_space(['\n']) == ['']


def test_r():
    assert remove_space(['\r']) == ['']


def test_combinado():
    assert remove_space(['\r \n']) == [' ']


def test_varios_items():
    assert remove_space(['n', 'b']) == ['n', 'b']


def test_final():
    assert remove_space(['\n n', '\r b']) == [' n', ' b']
