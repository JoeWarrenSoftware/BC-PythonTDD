

import pytest

# Define the fixture
@pytest.fixture
def data_a():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def data_b():
    return [6,7,8,9,10]

# Define the test function
def test_combined_data(data_a, data_b):
    assert sum(data_a + data_b) == 55
