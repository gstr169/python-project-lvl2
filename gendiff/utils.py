import json


def load_json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


def generate_diff(first_file, second_file):
    pass
