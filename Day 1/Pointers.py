dict1 = {'value': 22}
dict2 = dict1

dict3 = {'value': 33}

dict2 = dict3
dict1 = dict3

print(dict1,dict2,dict3)
print(id(dict1),id(dict2),id(dict3))