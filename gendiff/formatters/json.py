import json


def json_format(diff):
    # Convert the 'diff' object to a JSON-formatted string with minimal spacing.
    json_str = json.dumps(diff, separators=(',', ':'))
    # Replace JSON boolean and null values with their unquoted counterparts.
    json_str = json_str.replace('"true"', 'true')
    json_str = json_str.replace('"false"', 'false')
    json_str = json_str.replace('"null"', 'null')
    # Return the formatted JSON string.
    return json_str
