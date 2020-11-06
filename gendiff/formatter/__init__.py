from gendiff.formatter.stylish import render_stylish
from gendiff.formatter.plain import render_plain


def format_output(format_name, tree):
    if format_name == 'stylish':
        return render_stylish(tree)

    if format_name == 'plain':
        return render_plain(tree)

    raise ValueError(f'Unknown format: {format_name}')


__all__ = ['render_stylish', 'format_output']
