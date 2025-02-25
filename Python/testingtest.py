import pytest
def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum


def test_count():
    assert count([1,2,3,4,4,4,4,5],4) == 4
    assert  count(["test", "new", "line", "quick", "brown", "fox", "fox"], "fox") == 2