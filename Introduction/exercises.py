lottery_numbers = {13, 21, 22, 5, 8}

players = [
{"player":"Itamar","numbers": {1,56,23,14,67}},
{"player":"Ismar","numbers": {13,21,7,8,12}}
    ]

for player in players:
    how_many_right = player["numbers"].intersection(lottery_numbers)
    name = player["player"]
    print(f"Player {name} got {len(how_many_right)} right")