from src.crawler import get_webpage
import pytest


def test_basico():
    assert get_webpage([]) == ''
