def format_indent(depth):
    return ' ' * (depth * 4 - 2)


def format_dict_value(value, depth):
    parts = []
    for key in value:
        indent = format_indent(depth + 1)
        formatted_value = to_str(value[key], depth + 1)
        parts.append(f"{indent}  {key}: {formatted_value}")
    output = '\n'.join(parts)
    return f"{{\n{output}\n{format_indent(depth)}  }}"


def to_str(value, depth):
    if value is None:
        return 'null'

    if isinstance(value, bool):
        return 'true' if value else 'false'

    if isinstance(value, dict):
        return format_dict_value(value, depth)

    return value


def render_subject(subject, depth=0):
    indent = format_indent(depth)

    value = subject['value']

    if subject['status'] == 'root':
        rows = map(lambda child: render_subject(child, depth + 1), value)
        result = '\n'.join(rows)
        return f'{{\n{result}\n}}'

    if subject['status'] == 'subtree':
        rows = map(lambda child: render_subject(child, depth + 1), value)
        result = '\n'.join(rows)
        return f"{indent}  {subject['key']}: {{\n{result}\n{indent}  }}"

    result = to_str(value, depth)

    if subject['status'] == 'added':
        return f"{indent}+ {subject['key']}: {result}"

    if subject['status'] == 'deleted':
        return f"{indent}- {subject['key']}: {result}"

    if subject['status'] == 'unchanged':
        return f"{indent}  {subject['key']}: {result}"

    raise ValueError(f"Unknown status: {subject['status']}")


def render_stylish(data):
    return render_subject(data)
