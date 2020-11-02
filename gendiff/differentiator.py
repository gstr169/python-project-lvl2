import os
from gendiff.parsers import parse_data


def get_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()[1:]


def get_data(file_path):
    with open(file_path) as file:
        data = parse_data(file, get_format(file_path))
    return data


def generate_diff(first_file, second_file):
    first_data, second_data = get_data(first_file), get_data(second_file)
    minus_template = '  - {}: {}\n'
    no_changes_template = '    {}: {}\n'
    plus_template = '  + {}: {}\n'
    result = '{\n'
    for key, value in sorted(first_data.items()):
        if second_value := second_data.pop(key, None):
            if value == second_value:
                result += no_changes_template.format(key, value)
            else:
                result += minus_template.format(key, value)
                result += plus_template.format(key, second_value)
        else:
            result += minus_template.format(key, first_data[key])

    for key, value in sorted(second_data.items()):
        result += plus_template.format(key, value)

    result += '}'
    return result
