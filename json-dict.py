import json

#Opens json file
with open("tanks_data.json", "r") as json_file:
    data = json.load(json_file)
    print("Type:", type(data))
    print("\ntanks:",data['tanks'])



    