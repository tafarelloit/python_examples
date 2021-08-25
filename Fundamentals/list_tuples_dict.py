friends = [["Itamar",55],["Antonio",45],["Tafarello",155]]

for name,age in friends:
    print(name,age)


friends = [("Itamar",55),("Antonio",45),("Tafarello",155)]

for name,age in friends:
    print(name,age)


friends = [
    {"name":"Itamar","age":55},
    {"name":"Antonio","age":45},
    {"name":"Tafarello","age":155},
]
for value in friends:
    print(value["name"],value["age"])
