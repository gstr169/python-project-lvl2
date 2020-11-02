import json
import yaml


def parse_data(file_object, file_type: str) -> dict:
    if file_type in {'yml', 'yaml'}:
        data = yaml.safe_load(file_object)
    elif file_type == 'json':
        data = json.load(file_object)
    else:
        raise ValueError(f'Unknown format: {file_type}')
    return data
