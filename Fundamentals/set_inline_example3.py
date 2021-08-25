friends = ["Rolf","ruth","Tony","Mike","Jen","ruth"]
time_since_seen = [3,7,15,11,9,88]
#build a sets
long_timers = {
    friends[i]: time_since_seen[i] for i in range(len(friends))
    if time_since_seen[i] > 10
}
#without the confitional if time_since_seen[i] > 10
# {'Rolf': 3, 'ruth': 88, 'Tony': 15, 'Mike': 11, 'Jen': 9}

#adding the conditional if time_since_seen[i] > 10 then this would be the result
#{'Tony': 15, 'Mike': 11, 'ruth': 88}
print(long_timers)
