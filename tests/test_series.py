import pytest

from series.py import fib

def test_fib():
    actual = fib(10)
    expected = 34
    assert actual == expected