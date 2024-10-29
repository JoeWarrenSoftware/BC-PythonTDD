# ----------------------------
# pytest Basics
# ----------------------------

# pytest is a powerful testing framework in Python that makes it easy to write simple as well as scalable test cases.

# To use pytest, install it using pip:
# $ pip install pytest
# Optional: you can create a virtual environment (venv) before installing pytest for following best practices.

import pytest

# This demonstrates `pytest` usage including 
# fixtures, parameterization, exception handling, and test grouping.

# ----------------------------
# Step 1: Defining Calculator and Database Classes for Testing
# ----------------------------

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

class DatabaseConnection:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def disconnect(self):
        self.connected = False

    def execute_query(self, query):
        if not self.connected:
            raise ConnectionError("Database is not connected!")
        return f"Results for query: {query}"

# ----------------------------
# Step 2: Writing Basic pytest Functions for Calculator
# ----------------------------

def test_add():
    calc = Calculator()
    assert calc.add(3, 4) == 7
    assert calc.add(-1, 1) == 0

def test_add_negative():
    calc = Calculator()
    assert calc.add(-1, -1) == -2

def test_add_zero():
    calc = Calculator()
    assert calc.add(0, 5) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 5) == 15

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calc.divide(1, 0)

# ----------------------------
# Using Fixtures in pytest
# ----------------------------

import pytest

@pytest.fixture
def db_connection():
    db = DatabaseConnection()
    db.connect()
    yield db
    db.disconnect()

def test_query_execution(db_connection):
    result = db_connection.execute_query("SELECT * FROM users")
    assert result == "Results for query: SELECT * FROM users"

def test_database_disconnected(db_connection):
    db_connection.disconnect()
    with pytest.raises(ConnectionError, match="Database is not connected!"):
        db_connection.execute_query("SELECT * FROM users")

# ------------------------------------------
# Using Fixtures Scope and Autouse in pytest
# ------------------------------------------

import pytest

# Function-scoped fixture (default)
@pytest.fixture
def function_fixture():
    print("\nSetting up function_fixture")
    yield
    print("Tearing down function_fixture")

# Class-scoped fixture
@pytest.fixture(scope="class")
def class_fixture():
    print("\nSetting up class_fixture")
    yield
    print("Tearing down class_fixture")

# Module-scoped fixture
@pytest.fixture(scope="module")
def module_fixture():
    print("\nSetting up module_fixture")
    yield
    print("Tearing down module_fixture")

# Test functions
def test_one(function_fixture):
    print("Running test_one")

class TestClass:
    def test_two(self, class_fixture):
        print("Running test_two")

    def test_three(self, class_fixture):
        print("Running test_three")

def test_four(module_fixture):
    print("Running test_four")



# ----------------------------
# Test Parametrization with pytest
# ----------------------------

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

# ----------------------------
# Some Advanced pytest Techniques with Grouping Tests and Coverage
# ----------------------------

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@pytest.mark.parametrize("input_a, input_b, expected", [
    (6, 3, 2),
    (10, 2, 5),
    (15, 5, 3)
])
def test_divide_parametrized(input_a, input_b, expected):
    assert divide(input_a, input_b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Grouped Tests in a Class
class TestMathOperations:
    
    @pytest.mark.parametrize("input_a, input_b, expected", [
        (20, 4, 5),
        (100, 10, 10)
    ])
    def test_divide_grouped(self, input_a, input_b, expected):
        assert divide(input_a, input_b) == expected

    def test_divide_by_zero_grouped(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)

# ----------------------------
# Running Tests
# ----------------------------
# To run all tests, execute:
# $ pytest <filename>.py
# For coverage report:
# $ pytest --cov=<filename>.py --cov-report=term-missing