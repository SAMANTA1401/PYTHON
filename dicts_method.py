dicts = {'one':'jello','two':'hello','three':'def'}

dicts2=dicts.fromkeys(dicts,"five")

# print(dicts2)

print(dicts.get("one"))

print(dicts.keys())

print(dicts.values())

print(dicts.items())

dicts.update({"four":"sdfaer"})

print(dicts)

del dicts["one"]

print(dicts)

