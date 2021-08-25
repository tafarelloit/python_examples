"""
Regular for
"""
numbers = [0,1,2,3,4]
doubled_numbers = []
for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

"""
Inline for
"""

doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

"""
print a list 
"""
friend_ages = [22,34,55,79]
age_strings = [f"my friend is {age} years old" for age in friend_ages]
print(age_strings)

"""
another use case
"""
friend = input("enter your friend name : ")
friends = ["Itamar","Antonio","Tafarello","Sophia","Isabella","Edna"]
friends_lower = [name.lower() for name in friends]
if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of my friends")
else:
    print(f"{friend} is not my friend")