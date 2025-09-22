import pytest
from math_utils import add

@pytest.mark.parametrize('a,b,expected', [
    (1, 1, 2),
    (2, -2, 0),
    (0, 5, 5),
])

def test_add_param(a, b, expected):
    assert add(a, b) == expected