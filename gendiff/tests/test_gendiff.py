import os
import pytest
from gendiff import generate_diff


def get_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', filename)


def get_data(filename):
    with open(get_path(filename)) as file:
        result = file.read()
    return result


formats = ['json', 'yml']


@pytest.mark.parametrize('format', formats)
def test_generate_diff(format):
    first_filename, second_filename = get_path(f'file1.{format}'), get_path(f'file2.{format}')
    assert generate_diff(first_filename, second_filename) == get_data('result_stylish.txt')
    assert generate_diff(first_filename, second_filename, 'plain') == get_data('result_plain.txt')
