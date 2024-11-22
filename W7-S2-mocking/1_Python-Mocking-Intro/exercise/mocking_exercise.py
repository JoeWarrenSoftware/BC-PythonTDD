import requests
import unittest
from unittest.mock import patch

def fetch_data(url):
    """Function to fetch data from an API endpoint."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

class TestFetchData(unittest.TestCase):
    def test_fetch_data(self):
        #"""Test the fetch_data function without mocking (not recommended)."""
        url = "https://catfact.ninja/fact"
        data = fetch_data(url)
        assert data['length'] > 0 # It seems whenever the API is called a DIFFERENT cat fact and lengh comes back
        print("Real Test Completed")

    @patch('requests.get')
    def test_fetch_data_mocked(self, mock_get):
        #"""Test the fetch_data function with mocking."""
        # Arrange: Set up the mock to return a specific response
        mock_get.return_value.json.return_value = {"fact":"Approximately 1/3 of cat owners think their pets are able to read their minds.","length": 100}
        
        # Act: Call the function under test
        url = "https://catfact.ninja/fact"
        data = fetch_data(url)

        # Assert: Check the results
        assert data['length'] == 100
        mock_get.assert_called_once_with(url)  # Ensure the mock was called with the correct URL
        print("Mock Test Completed")

if __name__ == '__main__':
    unittest.main()