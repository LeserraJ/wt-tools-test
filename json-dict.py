import json

from tinydb import TinyDB, Query
#Opens json file
with open("tanks_data.json", "r") as json_file:
    data = json.load(json_file)
    #print("Type:", type(data))
    #print("\ntanks:",data['tanks'])



db = TinyDB('/workspace/wt-tools-test/tanks_data.json')

print(data)

#print(db)