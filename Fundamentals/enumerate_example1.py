friends = ["Rolf","ruth","Tony","Mike","Jen","ruth"]
counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

print("================")
for counter,friend in enumerate(friends):
    print(counter)
    print(friend)

print("================")
#print a list of tuples
print(list(enumerate(friends)))

#or
#print a list of tuples
print(list(zip([0,1,2,3,4,5],friends)))


print("================")
#print a dict
print(dict(enumerate(friends)))