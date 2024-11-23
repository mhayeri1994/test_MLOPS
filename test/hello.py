def add(a, b):
    return a + b

import pytest
#from math_utils import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
