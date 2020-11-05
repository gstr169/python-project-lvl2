from gendiff.formatter.stylish import render_stylish


def format_output(format_name, tree):
    if format_name == 'stylish':
        return render_stylish(tree)

    raise ValueError(f'Unknown format: {format_name}')


__all__ = ['render_stylish', 'format_output']
