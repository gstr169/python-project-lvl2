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
def test_generate_diff():
    first_filename, second_filename = f'file1.{format}', f'file2.{format}'
    assert generate_diff(get_path(first_filename), get_path(second_filename)) == get_data('result.txt')
