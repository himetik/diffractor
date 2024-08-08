"""Parse files."""

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
    # Use the json.load function to parse the JSON data
    # This function expects a file-like object and reads from it
    return json.load(json_data)


def parse_yaml(yaml_data):
    """
    Parse yaml data.

    Args:
        yaml_data: yaml data for parsing

    Returns:
        dict
    """
    # Use the yaml_load function to parse the YAML data
    # The Loader is specified to handle the parsing
    return yaml_load(yaml_data, Loader=Loader)


def get_file_info(file_path):
    """
    Retrieve information about a file given its path.

    Args:
        file_path (str): The path to the file.

    Returns:
        tuple: A tuple containing:
            - file_abs_path (pathlib.Path): The absolute path of the file.
            - file_extension (str): File extension (including the dot).
    """
    # Create a pathlib.Path object from the given file path
    file_path_obj = pathlib.Path(file_path)

    # Resolve the absolute path of the file
    file_abs_path = file_path_obj.resolve()

    # Get the file extension (including the dot)
    file_extension = file_path_obj.suffix

    # Return the absolute path and the file extension
    return file_abs_path, file_extension


def parse_file(file_path):
    """
    Parse json or yaml file.

    Args:
        file_path (str): file path

    Returns:
        dict
    """
    # Define a dictionary of parsers for different file extensions
    parsers = {
        '.json': parse_json,  # Function to parse JSON files
        '.yml': parse_yaml,  # Function to parse YML files
        '.yaml': parse_yaml,  # Function to parse YAML files
    }

    # Get the absolute path and file extension of the given file
    file_abs_path, file_extension = get_file_info(file_path)

    # Check if the file extension is supported; if not, raise an error
    if file_extension not in parsers.keys():
        raise ValueError(
            f'Unsupported file type: "{file_extension}". '
            f'Supported file types: {", ".join(parsers.keys())}'
        )

    # Open the file and use the appropriate parser function based on extension
    with open(file_abs_path) as file_obj:
        return parsers[file_extension](file_obj)
