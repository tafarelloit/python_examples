friends = ["Rolf","ruth","Tony","Mike","Jen","ruth"]
time_since_seen = [3,7,15,11,9,88]
money_in_the_bank = ["Y","N","Y","Y","N","Y"]

#create a dictionary
long_timers_dict = dict(zip(friends,time_since_seen))

print(long_timers_dict)

#create a list of tuples
parsa_list = list(zip(friends, time_since_seen, money_in_the_bank))

print(parsa_list)