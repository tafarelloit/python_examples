from _typeshed import FileDescriptor


friend_ages = {"Itamar": 55, "Ismar": 52, "Ismariane":49}

print(friend_ages)

print(friend_ages["Itamar"])

print(friend_ages["Itamar"])


friend_ages = (
    {"Name": "Itamar", "age": 55},
    {"Name": "Ismar", "age": 52},
    {"Name": "Ismariane", "age": 49},
)

print(friend_ages)
print(friend_ages[0])
print(friend_ages[0]["Name"])

#Not valid
#print(friend_ages["Name"])

#print all elements in the tuple
for value in friend_ages:
    #display each attribute of the dictionary
    print(value["Name"], value["age"])


#Transform the list of tuple into a dictionary
friend_ages = [("Itamar", 55), ("Ismar", 52), ("Ismariane",49)]
newdict = dict(friend_ages)
print(newdict)


