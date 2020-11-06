def to_str(value):
    if value is None:
        return 'null'

    if isinstance(value, bool):
        return 'true' if value else 'false'

    if isinstance(value, dict):
        return '[complex value]'

    return f"'{value}'"


def render_subject(subject, parent=''):
    # if (key := subject.get('key', '')) or parent:
    #     key = parent + '.' + key
    key = subject.get('key', '')
    if parent:
        key = parent + '.' + key
    value = subject['value']

    if subject['status'] in ('subtree', 'root'):
        rows = filter(None, map(lambda child: render_subject(child, key), value))
        result = '\n'.join(rows)
        return result

    if subject['status'] == 'changed':
        old_value = to_str(value[0])
        new_value = to_str(value[1])
        return f"Property '{key}' was updated. From {old_value} to {new_value}"

    result = to_str(value)

    if subject['status'] == 'added':
        return f"Property '{key}' was added with value: {result}"

    if subject['status'] == 'deleted':
        return f"Property '{key}' was removed"

    if subject['status'] == 'unchanged':
        return ''

    raise ValueError(f"Unknown status: {subject['status']}")


def render_plain(data):
    return render_subject(data)
