friends = ["Rolf","ruth","Tony","Mike","Jen","ruth"]
team = ["Matheus","Gui","Jeff","mike","Rony","Rony"]
#transform to a set eliminating the duplicates
friends_lower = set([f.lower() for f in friends])
team_lower = set([t.lower() for t in team])
print(friends_lower)
print(team_lower)
print(friends_lower.intersection(team_lower))

present_friends = [
    name.title() for name in team if name.lower() in friends_lower
]

print(present_friends)


present_friends = [
    name.title() 
    for name in team 
    if name.lower() in [f.lower() for f in friends]
]

print(present_friends)