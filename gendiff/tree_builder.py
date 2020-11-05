
def build_subtree(first_data, second_data):
    result = []
    keys = set(first_data.keys()).union(second_data.keys())

    for key in sorted(keys):
        if key not in first_data:
            subject = {
                'key': key,
                'value': second_data[key],
                'status': 'added'
            }
            result.append(subject)
        elif key not in second_data:
            subject = {
                'key': key,
                'value': first_data[key],
                'status': 'deleted'
            }
            result.append(subject)
        elif isinstance(first_data[key], dict) and isinstance(second_data[key], dict):
            subject = {
                'key': key,
                'value': build_subtree(first_data[key], second_data[key]),
                'status': 'subtree'
            }
            result.append(subject)
        elif first_data[key] != second_data[key]:
            subject = {
                'key': key,
                'value': first_data[key],
                'status': 'deleted'
            }
            result.append(subject)
            subject = {
                'key': key,
                'value': second_data[key],
                'status': 'added'
            }
            result.append(subject)
        else:
            subject = {
                'key': key,
                'value': first_data[key],
                'status': 'unchanged'
            }
            result.append(subject)

    return result


def build_tree(first_data, second_data):
    return {
        'status': 'root',
        'value': build_subtree(first_data, second_data)
    }
