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