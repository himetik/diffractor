import json


def json_format(diff):
    def custom_serializer(obj):
        if isinstance(obj, bool):
            return 'true' if obj else 'false'
        elif obj is None:
            return 'null'
        return obj

    json_str = json.dumps(diff, default=custom_serializer, separators=(',', ':'))
    return json_str
