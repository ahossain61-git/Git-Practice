
from calculator import add, subtract, multiply, divide


def test_addition():
    assert add(10, 5) == 15


def test_subtraction():
    assert subtract(10, 5) == 5


def test_multiplication():
    assert multiply(10, 5) == 50


def test_division():
    assert divide(10, 5) == 2


def test_division_by_zero():
    assert divide(10, 0) == "Cannot divide by zero"
def test_branch_protection():
    assert 2 + 2 == 4
