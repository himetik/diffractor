"""Compare two dicts."""


def compare_dicts(dict1, dict2):
    """
    Compare two dicts.

    Args:
        dict1 (dict): first dictionary
        dict2 (dict): second dictionary

    Returns:
        (list): list of dicts
    """
    # Get the union of keys from both dictionaries
    keys = set(dict1) | set(dict2)

    # Initialize an empty list to store differences
    diff = []

    # Iterate through the sorted keys
    for key in sorted(keys):
        # Get value from each dictionary, defaulting to None if key is missing
        value1 = dict1.get(key, None)
        value2 = dict2.get(key, None)

        if key not in dict1:
            # Key exists in dict2 but not in dict1 (added key)
            diff.append({'key': key, 'type': 'added', 'value': value2})
        elif key not in dict2:
            # Key exists in dict1 but not in dict2 (removed key)
            diff.append({'key': key, 'type': 'removed', 'value': value1})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            # Both values are dictionaries; recurse to compare them
            children = compare_dicts(value1, value2)
            diff.append({'key': key, 'type': 'complex', 'children': children})
        elif value1 != value2:
            # Values are different; record as changed
            diff.append({
                'key': key,
                'type': 'changed',
                'old-value': value1,
                'new-value': value2,
            })
        else:
            # Values are equal; record as equal
            diff.append({'key': key, 'type': 'equal', 'value': value1})

    # Return the list of differences
    return diff
