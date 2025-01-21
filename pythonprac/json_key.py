# Parse the following JSON to get all the values of a key ‘name’ within an arra





import json
sampleJson="""[
    {"id":1,
    "name":"name1",
    "color":[
        "red",
        "green",
        "blue"
    ]},
    {"id":2,
    "name":"name2",
    "color":[
        "pink",
        "yellow",
        "blue"
    ]}
]"""

data = []
try:
    data =json.loads(sampleJson)
    print(data)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data] #list comprehension
print(dataList)