# 📝 pytest Assignment

## 🎯 Assignment Overview

In this assignment, you will apply various `pytest` techniques to test a Python class that simulates a real-world system. This assignment will encompass unit testing, fixtures, test parameterization, and advanced testing techniques such as exception handling and generating coverage reports.

## 📚 Key Learnings

By completing this assignment, you will learn:

- How to use `pytest` for unit testing and validate functionality.
- How to design and implement fixtures for complex systems.
- How to efficiently run multiple test scenarios using test parameterization.
- Best practices for organizing tests and handling exceptions.
- How to generate coverage reports to assess the completeness of your tests.

## 👤 User Story

As a Python developer, I want to ensure my code is robust and reliable by testing various scenarios, managing resources effectively, and applying advanced testing techniques.

## ✅ Acceptance Criteria

- The Python script is named `YOURNAME_W7S2_assignment.py`.
- The script demonstrates:
  - Creating a Python class that models a real-world system (e.g., `BankAccount`, `WebServer`).
  - Writing comprehensive test cases for class methods using `pytest`.
  - Implementing `pytest` fixtures to manage setup and teardown operations.
  - Using test parameterization to cover multiple test cases efficiently.
  - Grouping tests, handling exceptions, and generating coverage reports.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `YOURNAME_W7S2_assignment.py`.

2. **🖊️ Write a Class**: Create a Python class to model a real-world system. For example, a `BankAccount` class with methods like `deposit()`, `withdraw()`, and `get_balance()`.

3. **✏️ Implement pytest Fixtures**: Write a fixture to handle setup and teardown of your system. For example, you can create a fixture that initializes an instance of the `BankAccount` before tests run and closes it afterward.

4. **✍️ Write Test Cases**:
   - **Unit Tests**: Write test functions that cover normal functionality and edge cases for your class methods.
   - **Parameterized Tests**: Use `@pytest.mark.parametrize` to validate the functionality of methods with various inputs. Aim for at least five parameterized test cases.

5. **🔍 Handle Exceptions**: Write tests to ensure that exceptions are raised correctly when invalid inputs are provided (e.g., attempting to withdraw more than the available balance).

6. **📊 Generate Coverage Reports**: Use `pytest-cov` to check coverage and ensure that all critical paths of your code are tested.

7. **📤 Run pytest**: Ensure all your test cases pass, and check the coverage report to verify your test completeness.

8. **💬 Comment Your Code**: Ensure that each section of the script is properly commented for clarity.

## Advanced Challenge (Optional)

- Explore the use of fixtures with different scopes (function, module, class, or session) for efficient resource management.
- Implement grouping of tests using test classes to organize related test cases.

## Additional Resources

- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [pytest Fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [pytest Parametrize Documentation](https://docs.pytest.org/en/stable/parametrize.html)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/en/latest/)
- [Real Python: Testing with pytest](https://realpython.com/python-testing/)

## Submission

Once you complete the assignment, submit the `YOURNAME_W7S2_assignment.py` file.

Good luck, and happy testing!