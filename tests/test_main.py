import pytest
from main import sort_by_field

def test_sort_by_field():
    # Sample input data
    data = {
        'country': {
            1: {'name': 'USA'},
            2: {'name': 'RUSSIA'},
            3: {'name': 'FRANCE'}
        }
    }

    # Expected result after sorting by name
    expected_result = {
        1: {'name': 'FRANCE'},
        2: {'name': 'RUSSIA'},
        3: {'name': 'USA'}
    }

    # Call the function to sort the data
    result = sort_by_field(data["country"], "name")
    
    # Assert that the sorted data matches the expected result
    assert result == expected_result
