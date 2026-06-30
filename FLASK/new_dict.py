import json 


data={}
data["username"]="anil"
data["password"]="53536356"
data["mail-id"]="anugjsgjg142@gmail.com"
data["mob-number"]="null"

print(data)


with open ("new_data.json","a") as dummy:
    json.dump(data, dummy, indent=4)

data_to_add={}
data_to_add["username"]=data["username"]
data_to_add["username"]=data["username"]