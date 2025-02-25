import pytest
from programs import factorial

def test_one(): 
    assert factorial.fact(1) == 1
    
def test_zero():
    assert factorial.fact(0) == 1