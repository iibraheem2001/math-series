
from series.series import fib, lucas

def test_fib_0():
    actual = fib(0)
    expected = 0
    assert actual == expected

def test_fib_1():
    actual = fib(1)
    expected = 1
    assert actual == expected

def test_fib_5():
    actual = fib(5)
    expected = 5
    assert actual == expected

def test_fib_8():
    actual = fib(8)
    expected = 21
    assert actual == expected

def test_fib_10():
    actual = fib(10)
    expected = 55
    assert actual == expected


def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_6():
    actual = lucas(6)
    expected = 18
    assert actual == expected

def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected

def test_lucas_14():
    actual = lucas(14)
    expected = 843
    assert actual == expected

