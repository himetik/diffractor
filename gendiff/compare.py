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
        if key not in dict1:
            diff.append({'key': key, 'type': 'added', 'value': dict2[key]})
        elif key not in dict2:
            diff.append({'key': key, 'type': 'removed', 'value': dict1[key]})
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            children = compare_dicts(dict1[key], dict2[key])
            diff.append({'key': key, 'type': 'complex', 'children': children})
        elif dict1[key] != dict2[key]:
            diff.append({
                'key': key,
                'type': 'changed',
                'old-value': dict1[key],
                'new-value': dict2[key],
            })
        else:
            diff.append({'key': key, 'type': 'same', 'value': dict1[key]})

    return diff
