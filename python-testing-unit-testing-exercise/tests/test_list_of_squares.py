import pytest
from programs import list_of_squares

def test_enter_zero():
    assert list_of_squares.list_of_squares(0) == {}

def test_enter_integer():
    assert list_of_squares.list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def test_enter_string():
    with pytest.raises(expected_exception=TypeError):
        list_of_squares.list_of_squares("string")