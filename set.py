dicts = {'one','jello','one','two','hello','one','three','one','def'}

# print(dicts)

# print('one'  in dicts)

# print(len(dicts))

# sorted(dicts)

# print(dicts)

s=set('dssdgregwr')
print(s)
r=set('sdtge')
print(r)

print(s-r)  #letters present in set a, but not in set b

print(s|r)  #Letters present in set a, set b, or both

print(s&r)  #letters present in both set a and set b
print(r^r) #letters present in set a or set b, buth not both 


dicts.add("six")

print(dicts)

print(s.difference(r))

print(s.intersection(r))

print(s.isdisjoint(r))

print(s.issuperset(r))

print(s.issubset(r))

print(s.symmetric_difference(r))

# print(s.union(r))

print(s.update(r))

s.pop()

print(s)

