#  Access the nested key ‘salary’ from the following JSON

import json

sampleJson="""{
    "company":{
        "employee":{
            "name":"emma",
            "payable":{
                "salary":7000,
                "bonus":800
                }, 
            "department":"HR"
        }
    }
}"""

data = json.loads(sampleJson)
# print(data)
print(data["company"]["employee"]["payable"]["salary"])