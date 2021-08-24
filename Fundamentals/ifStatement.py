username = input("Input user name ->")

friendsList = ["Itamar","Tafarello"]
friendsSet = {"Itamar","Antonio"}
friendsTuples = ("Tafarello","Tony")

if username in friendsList:
    print("Hello friend list")
    is_friend = True
elif username in friendsSet:
    print("Hello friend set")
    is_friend = True
elif username in friendsTuples:
    print("Hello friend tuples")
    is_friend = True
else:
    print("Sorry buddy you are not in the list.")
    #there is a catch here is_friend is not defined so it will failed in the evaliation below

if is_friend is False:
    print("you are not my friend !")