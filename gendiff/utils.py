import json


def load_json(filename) -> dict:
    with open(filename) as file:
        data = json.load(file)
    return data


def generate_diff(first_file, second_file):
    first_data, second_data = load_json(first_file), load_json(second_file)
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
