def show_homepage():
    print("         === DonateMe Homepage ===           ")
    print("---------------------------------------------")
    print("| 1.     Login   | 2.    Register           |")
    print("---------------------------------------------")
    print("| 3.     Donate   | 4.    Show Donations    |")
    print("---------------------------------------------")
    print("|                5. Exit                    |")
    print("---------------------------------------------")


#Task 6: Donate Functionality

def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_string = f"{username} donated ${donation_amt}"
    print("Thanks for your donations!")
    return donation_string

#Task 7: Show Donations functionality
def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)


