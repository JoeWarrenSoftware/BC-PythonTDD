import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("input_a, input_b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
    (-50, -50, -100)
])
def test_add_parametrized(input_a, input_b, expected):
    assert add(input_a, input_b) == expected