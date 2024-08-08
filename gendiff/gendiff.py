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
    # Define a dict. mapping formatter types to their corresponding functions
    formatters = {
        'plain': plain,  # Function to format the diff in plain text
        'json': json_format,  # Function to format the diff as JSON
        'stylish': stylish,  # Function to format the diff in a stylish manner
    }
    # Create a set of supported formatter types for quick lookup
    supported_formatter_types = set(formatters.keys())

    # Check if the provided formatter_type is valid; raise an error if not
    if formatter_type not in supported_formatter_types:
        raise ValueError(
            'formatter_type parameter can only take the following values: '
            f'plain, json, stylish. Current value is {formatter_type}'
        )

    # Call the appropriate formatting function based on the formatter_type
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
        # Parse the first file and convert its contents to a dictionary
        dict1 = parse_file(file1_path)

        # Parse the second file and convert its contents to a dictionary
        dict2 = parse_file(file2_path)
    except ValueError as err:
        # Handle parsing errors and return an appropriate message
        return f'Error parsing files: {err}'
    except Exception as err:
        # Handle any other unexpected errors and return an appropriate message
        return f'Unexpected error: {err}'

    # Compare the two dictionaries to get the differences
    diff = compare_dicts(dict1, dict2)

    # Format the diff according to the specified formatter type and return it
    return format_diff(diff, formatter_type)
