import json


def open_json(path):
    with open(path, 'w') as file:
        return json.load(file)


print(open_json("json.json"))