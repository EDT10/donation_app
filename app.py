#Task 2: Show homepage and initialize app data

from donations_pkg import homepage
from donations_pkg import user

database = {"admin" : "password123"}
donations = []
authorized_user = ""

homepage.show_homepage()

if authorized_user == "":
    print("You must be logged in to donate\n")
else:
    print("Logged in as:", authorized_user)

# ask_user = int(input("Please choose an option: "))

#TASK 3: Handle user input

while True:
    ask_user = int(input("Please choose an option: "))
    # homepage.show_homepage()

    if ask_user == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = user.login(database, username, password)
        homepage.show_homepage()
        if authorized_user == "":
            print("You must be logged in to donate\n")
        else:
            print("Logged in as:", authorized_user)
        continue


    elif ask_user == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = user.register(database, username)
        if authorized_user != "":
            database[username] = password
        # print(database)
        # print("Logged in as:", authorized_user)
        
        homepage.show_homepage()
        continue


        #Task 6
    elif ask_user == 3:
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)
        homepage.show_homepage()
        continue

        #Task 7
    elif ask_user == 4:
        homepage.show_donations(donations)
        homepage.show_homepage()

    elif ask_user == 5:
        print("Goodbye")
        quit()