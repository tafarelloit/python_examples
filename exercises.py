lottery_numbers = {13, 21, 22, 5, 8}

players = [
{"player":"Itamar","numbers": {5,56,23,14,67}},
{"player":"Ismar","numbers": {13,21,7,8,12}}
    ]

print(players[0]["player"])

for player in players:
    howmanycorrect = player["numbers"].intersection(lottery_numbers)
    print(len(howmanycorrect))