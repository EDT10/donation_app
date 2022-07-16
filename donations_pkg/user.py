#Task 4: Login functionality

def login (database, username, password):
    if username in database:
        if password in database.values():
            print("Welcome back", username, "\n")
            return username
        elif password not in database.values():
            print("Sorry, incorrect password for",username,  "\n")
            return ""
    else:
        print("User not found. Please register \n")
        return ""



  
  
"""   # Old logic i used before for the login function. Had to rewite the function. Kept this old 
  # logic for reference """
  
    # for u_username, p_password in database.items():
    #     if username == u_username and password == p_password:
    #         print("Welcome back", username, "\n")
    #         return username
    #     elif username == u_username and password != p_password:
    #         print("Sorry, incorrect password for",username,  "\n")
    #         return ""
    #     else:
    #         print("User not found. Please register")
    #         return ""

    # print(database)



#Task 5: Register functionality

def register(database, username):
    if username in database:
        print("Username Already registered")
        return ""
    else:
        # database[username] = password
        print("Username", username,"Registered")
        # print(database)
        return username


  
""" Old logic i used before for the register function. Had to rewite the function. Kept this old 
 logic for reference """
    # for u_username in database.keys():
    #     if username == u_username:
    #         print("Username Already registered")
    #         return ""
    #     else:
    #         database[username] = password
    #         print("Username", username,"Registered")