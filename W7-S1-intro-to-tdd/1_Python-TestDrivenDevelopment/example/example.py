# ----------------------------
# Test-Driven Development (TDD) Overview
# ----------------------------

# TDD is a software development approach where tests are written before code.
# The process involves a Red-Green-Refactor cycle:
# 1. Red: Write a test that fails.
# 2. Green: Write minimal code to make the test pass.
# 3. Refactor: Optimize the code while keeping it functional.

# This approach leads to better design, fewer bugs, and a more maintainable codebase.

import unittest

# ----------------------------
# Example 1: Simple Addition Test
# ----------------------------

def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        """Test cases for add_numbers function."""
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

# ----------------------------
# Example 2: Red-Green-Refactor with is_even
# ----------------------------

def is_even(number):
    """Returns True if number is even, else False."""
    return number % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        """Test cases for is_even function."""
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

# ----------------------------
# Example 3: Advanced TDD - Factorial and Prime Functions
# ----------------------------

def factorial(n):
    """Calculates factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)

def is_prime(n):
    """Checks if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestMathFunctions(unittest.TestCase):
    def test_factorial(self):
        """Test cases for factorial function."""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_is_prime(self):
        """Test cases for is_prime function."""
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))

# ----------------------------
# Running the Tests
# ----------------------------

if __name__ == '__main__':
    unittest.main()  # Runs all tests across all classes