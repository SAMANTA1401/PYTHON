# PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
# sampleJson = {"key1": "value1", "key2": "value2"}

import json
sampleJson = {"key1": "value1", "key2": "value2"}

prettyPrintedJson = json.dumps(sampleJson,indent=2,separators=(":", " = "))
print(prettyPrintedJson)

