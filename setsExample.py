"""
Sets don't hold order, do not have duplicates
Easy to make comparison between sets
"""
friends = {"Itamar","Antonio","Tafarello"}
print(friends)

#adding a value
friends.add("Programmer")
print(friends)

#adding a value again , notice the value is not added
friends.add("Programmer")
print(friends)

#removing a value
friends.remove("Programmer")
print(friends)

family = {"Itamar","Edna","Sophia","Isabella"}

#create a new set with the element(s) that are not common in both sets
newset = family.difference(friends)
print(newset)

#create a new set with the element(s) that are common in both sets
newset = family.intersection(friends)
print(newset)

#create a new set with the element(s) are not in both sets
newset = family.symmetric_difference(friends)
print(newset)

#create a new set with the element(s) of both sets
newset = family.union(friends)
print(newset)




