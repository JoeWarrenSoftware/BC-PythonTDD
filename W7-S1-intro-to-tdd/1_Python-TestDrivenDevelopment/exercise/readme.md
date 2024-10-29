
# 🐍 Test-Driven Development (TDD) in Python

## 🎯 Objective

In this exercise, you’ll apply the Test-Driven Development (TDD) process to implement and test multiple Python functions, `tdd_concepts.py`. Through this practice, you will learn how to use TDD effectively by writing tests before implementing each function and using the Red-Green-Refactor cycle.

## 📚 Key Learnings

By completing these exercises, you will learn:

- The TDD cycle: Red-Green-Refactor
- How to write failing tests first, then implement code to pass them
- How TDD improves code design and helps catch bugs early
- Using Python's `unittest` framework for testing

## Functions and Concepts Covered

You will work on the following functions and concepts:

1. **Palindrome Check** - Write a test and function to check if a string is a palindrome.
2. **Alphabet Check** - Write a test and function to verify if a string contains only alphabetic characters.
3. **Math Operations** - Write tests for basic math functions like multiplication and division.
4. **Fibonacci Sequence** - Write tests and implement a function to calculate the nth Fibonacci number.
5. **Anagram Check** - Write tests and implement a function to check if two strings are anagrams.

---

## ✅ Acceptance Criteria

- The Python script is named `tdd_concepts.py`.
- The script demonstrates:
  - Writing a failing test first (Red).
  - Implementing code to pass the test (Green).
  - Refactoring for improved design (Refactor).
- Each function should include:
  - A corresponding test case in the same file.
  - Commented sections for clarity.
- Tests should cover edge cases where applicable (e.g., negative inputs for Fibonacci, different lengths for anagrams).

---

## 🛠️ Steps to Complete

### Setup

1. **📁 Create a new Python file**: Name the file `tdd_concepts.py`.
2. **Import `unittest`**: This will be used to write and run all tests.

### 1: Palindrome Check

1. **Write a failing test**: Start by writing a test for a function that checks if a string is a palindrome.
2. **Implement the function**: Create an `is_palindrome()` function to check if a string reads the same forward and backward.
3. **Refactor if needed**: Simplify or improve the function as necessary.

### 2: Alphabet Check

1. **Write a failing test**: Write a test for a function that checks if a string contains only alphabetic characters.
2. **Implement the function**: Create an `is_alpha()` function to check if a string is alphabetic.
3. **Refactor**: Improve the function’s readability if necessary.

### 3: Basic Math Operations

1. **Write a failing test**: Write tests for basic math functions like `add()` and `multiply()`.
2. **Implement the functions**: Create the functions to perform basic arithmetic.
3. **Run and Refactor**: Ensure all tests pass and improve the code if necessary.

### 4: Fibonacci Sequence and Anagram Check

1. **Write tests for Fibonacci function**: Check valid inputs (e.g., 0, 1, 5, 10) and edge cases (e.g., negative inputs).
2. **Implement Fibonacci function**: Create `fibonacci()` to return the nth Fibonacci number.
3. **Write tests for Anagram function**: Check if two strings are anagrams, including edge cases.
4. **Implement Anagram function**: Create `is_anagram()` to check if two strings are anagrams.

---

## Example Structure in `tdd_concepts.py`

```python
import unittest

# Palindrome Check
def is_palindrome(s):
    # Code for checking palindrome
    pass

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        # Write failing tests, then implement function and refactor
        pass

# Alphabet Check
def is_alpha(s):
    # Code for checking alphabetic characters
    pass

class TestAlphabetCheck(unittest.TestCase):
    def test_is_alpha(self):
        # Write failing tests, then implement function and refactor
        pass

# Basic Math Operations
def add(a, b):
    # Code for addition
    pass

def multiply(a, b):
    # Code for multiplication
    pass

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        # Write failing tests, then implement function and refactor
        pass
    def test_multiply(self):
        # Write failing tests, then implement function and refactor
        pass

# Fibonacci Sequence
def fibonacci(n):
    # Code for Fibonacci calculation
    pass

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        # Write failing tests, then implement function and refactor
        pass

# Anagram Check
def is_anagram(s1, s2):
    # Code for checking anagrams
    pass

class TestAnagram(unittest.TestCase):
    def test_is_anagram(self):
        # Write failing tests, then implement function and refactor
        pass

if __name__ == '__main__':
    unittest.main()
```

---

## Tips

- Follow the Red-Green-Refactor cycle closely: start by writing a failing test, then implement the code to make it pass, and finally refactor.
- Use assertions like `self.assertEqual()` and `self.assertTrue()` to validate function outputs.
- Use Python's built-in `unittest` module for structured testing and better debugging.

## Additional Resources

- [Python `unittest` Documentation](https://docs.python.org/3/library/unittest.html)
- [Real Python: Test-Driven Development with Python](https://realpython.com/test-driven-development-with-python/)

---

Happy testing testers! 🐍