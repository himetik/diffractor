import json
import pathlib

from yaml import CLoader as Loader
from yaml import load as yaml_load

def parse_json(json_data):
    """
    Parse json data.

    Args:
        json_data: json data for parsing

    Returns:
        dict
    """
    return json.load(json_data)

def parse_yaml(yaml_data):
    """
    Parse yaml data.

    Args:
        yaml_data: yaml data for parsing

    Returns:
        dict
    """
    return yaml_load(yaml_data, Loader=Loader)

def get_file_extension(file_path):
    """
    Get file extension from file path.

    Args:
        file_path (str): file path

    Returns:
        str: file extension
    """
    return pathlib.Path(file_path).suffix

def parse_file(file_path):
    """
    Parse json or yaml file.

    Args:
        file_path (str): file path

    Returns:
        dict
    """
    parsers = {
        '.json': parse_json,
        '.yml': parse_yaml,
        '.yaml': parse_yaml,
    }

    file_extension = get_file_extension(file_path)

    if file_extension not in parsers:
        raise ValueError(
            f'Unsupported file type: "{file_extension}". '
            f'Supported file types: {", ".join(parsers.keys())}'
        )

    with open(file_path) as file_obj:
        return parsers[file_extension](file_obj)
