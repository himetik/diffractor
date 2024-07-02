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
    keys = set(dict1) | set(dict2)

    diff = []
    for key in sorted(keys):
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if key not in dict1:
            diff.append({'key': key, 'type': 'added', 'value': value2})
        elif key not in dict2:
            diff.append({'key': key, 'type': 'removed', 'value': value1})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            children = compare_dicts(value1, value2)
            diff.append({'key': key, 'type': 'complex', 'children': children})
        elif value1 != value2:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': value1,
                'new_value': value2,
            })
        else:
            diff.append({'key': key, 'type': 'same', 'value': value1})

    return diff
