# for data in range(101):
    # print(data)

# a={
#     "name":"ajay",
#     "age":30,
#     "city":"jaipur",
#     "tel-":84747478747,
# }    
# print(a)


a = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "data1": { 
        "level": "Advanced",
        "data2": [ 1, 2, 3, 4, 5, { "data3": "dummy_value" } ]
    }
}
# print(a["age"])
# print(a["data1"]["data2"])
print(a["data1"]["data2"][5]["data3"])