import os
from gendiff.parsers import parse_data
from gendiff.tree_builder import build_tree
from gendiff.formatter import format_output


def get_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()[1:]


def get_data(file_path):
    with open(file_path) as file:
        data = parse_data(file, get_format(file_path))
    return data


def generate_diff(first_file, second_file, format_name='stylish'):
    first_data, second_data = get_data(first_file), get_data(second_file)
    result = build_tree(first_data, second_data)
    return format_output(format_name, result)
