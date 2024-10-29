# 📚  Exercises on Pytest

Welcome to the  exercises focused on `pytest`, a powerful testing framework for Python. This README covers the essentials of writing and organizing tests effectively.

## 🐍 Overview of Exercises

### Exercise 1: pytest Basics - Writing and Running Unit Tests

**Challenge:**  
Implement a simple class and write test cases using `pytest`.

**Key Learnings:**  
- Writing and running unit tests with `pytest`.
- Using assertions to verify function correctness.
- Handling exceptions in tests.

**Acceptance Criteria:**  
- Create a class `DataProcessor` with methods for string manipulation and list processing.
- Write corresponding test functions for each method.
- Handle exceptions gracefully.

**File:** `pytest_basics.py`

---

### Exercise 2: pytest Fixtures - Reusing Setup Code

**Challenge:**  
Create a Python class that represents a simple system and write test cases using `pytest` fixtures for setup and teardown.

**Key Learnings:**  
- Writing reusable test setup and teardown code using fixtures.
- Managing test environments efficiently.

**Acceptance Criteria:**  
- Implement a class (e.g., `FileSystem` or `DatabaseConnection`).
- Create a `pytest` fixture for managing resources.
- Write test cases utilizing the fixture.

**File:** `pytest_fixtures.py`

---

### Exercise 3: Test Parametrization with pytest

**Challenge:**  
Create a set of parameterized tests for a function of your choice using `pytest`'s `@pytest.mark.parametrize` decorator.

**Key Learnings:**  
- Benefits of test parametrization in reducing code duplication.
- Running multiple test cases with various inputs efficiently.

**Acceptance Criteria:**  
- Define a function to test.
- Write at least three parameterized test cases.

**File:** `parametrized_tests.py`

---

## 🛠️ General Steps for Each Exercise

1. **Create a new Python file** for each exercise.
2. **Write your code** following the challenge guidelines.
3. **Develop test cases** ensuring clarity and coverage of edge cases.
4. **Run your tests using pytest** to verify all pass successfully.
5. **Comment your code** adequately to enhance readability.

## 📝 Additional Resources

- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [Real Python: Testing with pytest](https://realpython.com/pytest-python-testing/)
- [PyBites: Testing with pytest](https://codechalleng.es/pytest/)

---

## 🗂️ Submission

Once you complete the exercises, submit the following files to your instructor:

- `pytest_basics.py`
- `pytest_fixtures.py`
- `parametrized_tests.py`

Happy testing folks! 🎉
