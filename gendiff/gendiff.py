"""Generate diff from two files in different formats."""

from gendiff.compare import compare_dicts
from gendiff.formatters.json import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import parse_file


def format_diff(diff, formatter_type):
    """
    Format diff according to formatter type.

    Args:
        diff (list): diff of two dictionaries
        formatter_type (str): format type for diff

    Returns:
        str
    """
    formatters = {
        'plain': plain,
        'json': json_format,
        'stylish': stylish,
    }
    supported_formatter_types = set(formatters.keys())

    if formatter_type not in supported_formatter_types:
        raise ValueError(
            'formatter_type parameter can only take the following values: '
            f'plain, json, stylish. Current value is {formatter_type}'
        )

    return formatters[formatter_type](diff)


def generate_diff(file1_path, file2_path, formatter_type='stylish'):
    """
    Generate diff comparing two json, yaml files.

    Args:
        file1_path (str): path to first file
        file2_path (str): path to second file
        formatter_type (str): the format in which the diff will be formatted

    Returns:
        diff (str)
    """
    try:
        dict1 = parse_file(file1_path)
        dict2 = parse_file(file2_path)
    except ValueError as err:
        return f'Error parsing files: {err}'
    except Exception as err:
        return f'Unexpected error: {err}'

    diff = compare_dicts(dict1, dict2)

    return format_diff(diff, formatter_type)

