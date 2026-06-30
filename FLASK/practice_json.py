import json

with open("test.json") as data:
    dummy_data=json.load(data)
    print(dummy_data)
    for x in dummy_data:
        # print (x['username'])
        print(x['password'])

