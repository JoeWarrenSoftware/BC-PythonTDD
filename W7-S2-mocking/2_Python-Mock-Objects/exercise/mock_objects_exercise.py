from unittest.mock import Mock
import unittest

class Database:
    def Connect():
        print("Database connected!")

    def GetData():
        data = { id: 1, "color": "red", "age": 20}
        return data
    
class DataService:
    def __init__(self, database: Database):
        self.database = database

    def GetColor(self):
        self.database.Connect()
        data = self.database.GetData()
        return data["color"]
    
    def GetAge(self):
        self.database.Connect()
        data = self.database.GetData()
        return data["age"]

class TestIsEven(unittest.TestCase):
    def test_use_data_service_color(self):
        # Create the mocked object with the type Database
        mock_database = Mock(spec=Database)

        # Override how it will return the function
        mock_database.GetData.return_value = { id: 1, "color": "blue", "age": 20}

        # Create service using mocked database
        service = DataService(mock_database)

        # Call the method you want to test from the service
        color = service.GetColor()

        # Prove the actual return is what we expect
        self.assertEqual(color, "blue")

    def test_use_data_service_age(self):
        mock_database = Mock(spec=Database)
        mock_database.GetData.return_value = { id: 1, "color": "blue", "age": 100}
        service = DataService(mock_database)
        age = service.GetAge()
        self.assertEqual(age, 100)

if __name__ == '__main__':
    unittest.main()
    

