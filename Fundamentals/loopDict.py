friends = [
    {"name":"Itamar","age":55},
    {"name":"Antonio","age":45},
    {"name":"Tafarello","age":155},
]

#print complete dict for each element of the list
for value in friends:
    print(value.values())

"""
dict_values(['Itamar', 55])
dict_values(['Antonio', 45])
dict_values(['Tafarello', 155])
"""

for value in friends:
    newdic = value.values()
    for nv in newdic:
        print(nv)
"""
Itamar
55
Antonio
45
Tafarello
155
"""

friend_ages = {"Ralf":25,"Anne":26,"Mike":59,"Maggy":59}
#print age
for age in friend_ages.values():
    print(age)

#print name
for name in friend_ages.keys():
    print(name)

#print name and age
for name,age in friend_ages.items():
    print(name, age)