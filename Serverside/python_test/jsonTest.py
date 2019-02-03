import json


def open_json(path):

    # If a file exists
    try:
        # Open the file and load the data as a dictionary
        with open(path, 'r+') as file:
            return json.load(file)  # Loads data using file object

    # If the file does not exist, then create it
    except FileNotFoundError:
        jsonTxt = "{}"

        # Create new json with minimum required data to be concidered a json
        with open(path, 'w+') as file:
            file.write(jsonTxt)
            return json.loads(jsonTxt)  # json.loads turns a string into a json, hence the extra 's' vs json.load


json.dump({"Hello": "He"}, open("lol", "w+"))
print(open_json("json.json")["sdsd"])