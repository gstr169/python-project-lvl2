import pytest
from gendiff import generate_diff


@pytest.fixture
def text_result():
    with open('gendiff/tests/fixtures/result.txt') as file:
        result = file.read()
    return result


def test_generate_diff(text_result):
    first_file, second_file = 'gendiff/tests/fixtures/file1.json', 'gendiff/tests/fixtures/file2.json'
    assert generate_diff(first_file, second_file) == text_result
