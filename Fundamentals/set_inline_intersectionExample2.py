friends = ["Rolf","ruth","Tony","Mike","Jen","ruth"]
team = ["Matheus","Gui","Jeff","mike","Rony","Rony"]
#transform to a set eliminating the duplicates
friends_lower = {f.lower() for f in friends}
team_lower = {t.lower() for t in team}

present_friends = {name.title() for name in friends_lower.intersection(team_lower)}
print(present_friends)

