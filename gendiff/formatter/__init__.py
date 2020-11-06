from gendiff.formatter.stylish import render_stylish
from gendiff.formatter.plain import render_plain
from gendiff.formatter.json import render_json


def format_output(format_name, tree):
    if format_name == 'stylish':
        return render_stylish(tree)

    if format_name == 'plain':
        return render_plain(tree)

    if format_name == 'json':
        return render_json(tree)

    raise ValueError(f'Unknown format: {format_name}')


__all__ = ['render_stylish', 'format_output']
