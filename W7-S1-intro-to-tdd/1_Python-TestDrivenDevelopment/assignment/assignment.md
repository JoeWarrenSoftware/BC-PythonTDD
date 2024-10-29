# 📝 Python TDD Assignment

## 🎯 Assignment Overview

In this assignment, you will create and test a series of Python functions using the TDD (Test-Driven Development) methodology. The goal is to apply the Red-Green-Refactor cycle to various scenarios, allowing you to gain hands-on experience in writing, running, and refining test cases.

## 📚 Key Learnings

By completing this assignment, you will learn:
- How to implement and test functions using TDD.
- Writing tests before implementing the code to ensure correctness.
- Refactoring for code clarity, efficiency, and readability.
- Handling edge cases in tests for robust code.

## 👤 User Story

As a Python developer, I want to improve my understanding of TDD by applying it to a range of functions, refining my implementation through testing, and developing a more comprehensive understanding of code quality.

---

## ✅ Acceptance Criteria

- The Python script is named `YOURNAME_W7S1_assignment.py`.
- The script demonstrates:
  - Writing multiple test cases for different functions.
  - Implementing code to pass all test cases.
  - Refactoring the code for clarity, performance, and maintainability.
  - Writing comments for each section of the script to ensure clarity.

---

## 🛠️ Steps to Complete

### 1. **📁 Create a new Python file**  
   - Name the file `YOURNAME_W7S1_assignment.py`.

### 2. **🔍 Define the functions and write initial failing tests**  
   - Implement functions that address different mathematical and logical scenarios:
     - **Factorial Calculation**: `factorial(n)` should compute the factorial of a non-negative integer.
     - **GCD Calculation**: `gcd(a, b)` should compute the greatest common divisor of two integers.
     - **Power Calculation**: `power(base, exponent)` should calculate the base raised to the exponent.
     - **Sorted List Check**: `is_sorted(lst)` should return `True` if a list is sorted, otherwise `False`.
     - **Nth Fibonacci Number**: `fibonacci(n)` should return the nth Fibonacci number.
     - **Matrix Addition**: `matrix_addition(matrix1, matrix2)` should add two matrices (2D lists) of the same dimensions.
     - **Area of Rectangle**: `area_rectangle(length, width)` should calculate the area of a rectangle.
     - **Area of Circle**: `area_circle(radius)` should calculate the area of a circle.
     - **Perfect Square Check**: `is_perfect_square(n)` should return `True` if `n` is a perfect square, otherwise `False`.
   - Write initial tests that you expect to fail (Red stage).

### 3. **🛠 Implement functions to pass tests**  
   - Implement just enough code to pass each failing test for each function.
   - Ensure that tests cover normal cases, edge cases, and invalid inputs.
   - Use assertions to confirm expected results.

### 4. **🔄 Refactor for clarity and performance**  
   - After making all tests pass (Green stage), refactor your code.
   - Optimize functions, enhance readability, and remove redundancies where possible.
   - Add comments to explain each function's logic and purpose.

### 5. **📤 Print and verify results**  
   - Print the results of your tests and implementations for clarity and easy verification.
   - Ensure that all test cases are working as expected without errors.

### 6. **💬 Comment your code**  
   - Add comments for each section and function of the script, explaining the purpose, parameters, and expected behavior.

---

## Advanced Challenge (Optional)

1. Implement additional functions and tests, such as:
   - **Median of List**: Write a function to calculate the median of a list and tests for it.
   - **Area of Triangle**: Create a function for calculating the area of a triangle and write relevant tests.
2. Add parameterized tests to handle multiple inputs in one go using Python’s `unittest` framework.

---

## Tips

- Follow the TDD cycle: Red (failing test), Green (make test pass), Refactor (improve code).
- Aim for simplicity, clarity, and efficiency in code and comments.
- Use `self.assertRaises()` to check for exceptions like `ValueError` for invalid inputs.

---

## Additional Resources

- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Real Python: Getting Started with Testing](https://realpython.com/python-testing/)

## Submission

Once you complete the assignment, submit the `YOURNAME_W7S1_assignment.py` file.

Happy coding, and enjoy the journey of mastering TDD!