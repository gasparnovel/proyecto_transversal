from src.get_products import get_next_product
import pytest


def test_basico():
    assert get_next_product([]) == ''


def test():
    assert get_next_product('hola') == (None, 0)


def test_producto():
    assert get_next_product(
        'class="producto"> hola </div><div>') == (' hola ', 23)
