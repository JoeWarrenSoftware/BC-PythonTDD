import pytest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

# Pytest knows to use this as a test method because it starts with test and has some assert...
def test_add():
    calc = Calculator()
    assert calc.add(3, 4) == 7
    assert calc.add(-1, 1) == 0