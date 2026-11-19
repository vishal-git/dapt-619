# Demo 1 (complete version): add_number and its tests, in one file.
# Run:  python src/addition.py        -> prints 8
#       pytest -q src/addition.py     -> 2 passed
import pytest


def add_number(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("add_number expects two numbers")
    return a + b


def test_add_number():
    assert add_number(3, 5) == 8
    assert add_number(-1, 1) == 0
    assert add_number(0, 0) == 0


def test_add_number_rejects_strings():
    with pytest.raises(TypeError):
        add_number("a", "b")


if __name__ == "__main__":
    print(add_number(3, 5))
