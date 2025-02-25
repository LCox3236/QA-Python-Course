import pytest
from programs import vowels

def test_long_word():
    assert vowels.vowels("supercalifragilisticexpialidocious") == 16