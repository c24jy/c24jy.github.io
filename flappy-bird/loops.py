#create a lists of taken usernames
taken_usernames = ["julie", "thomas", "rhia", "tyler"]

name= input("What is your name?")

while name in taken_usernames:
    name = input("Sorry, that name is taken! Please input a new name:")


print("Hiya, " + name + "!")

