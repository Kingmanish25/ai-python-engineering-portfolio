import json

data = {
    "name": "John",
    "age": 30
}

json_data = json.dumps(data, indent=4)

print(json_data)
