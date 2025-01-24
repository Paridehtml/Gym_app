import json
with open("gym_app.json", "r") as file:
    data = json.load(file)

activities = data["activities"]
memberships = data["memberships"]
personal_trainers = data["personal_trainers"]
personal_profile = data["personal_profile"]


def sign_in():
    print("\n-- Sign in for access --\n")
    while True:
        while True:
            username = input("Insert your username: \t")
            if username != "user1": print("\nUser not recognized, try again\n") 
            else: break
        while True:
            password = input("\nType your password here: \t")
            if password != "password1": print("\nIncorrect password, please try again") 
            else: break
        print("\nWelcome to the Gym app\n")
        break

def main_menu():
    print("\n---------------------")
    print("***** MAIN MENU *****")
    print("---------------------\n")
    print("1. Get you membership\n")
    print("2. Join an activity\n")
    print("3. Tap in\n")
    print("4. Check your progress\n")
    print("5. Your profile\n")
    choice = input("What you want to do today? type here a number from the list: ")
    if choice == "1": get_mermbership()
    elif choice == "2": join_activity(username="example_user")
    elif choice == "3": tap_in()
    elif choice == "4": progress()
    elif choice == "5": profile()
        
def get_mermbership():
    print("\n----- MEMBERSHIPS -----\n")
    print("We offer different options to become a member: \n")
    for membership in data["memberships"]:
        print(f"{membership["id"]} - {membership["name"]}: £{membership["price"]}")
    while True:
        user_choice = input("\nType your selected option: ")
        if user_choice == "1": print("Thank you for purchasing the Exercise Membership, you are now a member."); break
        elif user_choice == "2": print("Thank you for purchasing the Premium Membership, you are now a member.");  break
        elif user_choice == "3": print("Thank you for purchasing the VIP Membership, you are now a member."); break
        elif user_choice == "back": return main_menu()
        else: print("Please enter a valid number, or 'back' to go back to the main menu\n")
    while True:
        command = input("Do you want to go back to menu? ")
        if command == "yes":
            main_menu()
        elif command == "no":
            break 
        else:
            print("please type 'yes' or 'no' ")
            

def join_activity(username):
    #try:
    #    with open("gym_app.json", "r") as file:
    #        data = json.load(file)
    #except FileNotFoundError:
    #    print("File 'gym_app.json' missing")
    #    return
    print("\n----- ACTIVITIES -----\n")
    print("Book an activity selecting one of the following:\n")
    for activity in data["activities"]:
        print(f"'{activity['name']}' for the special price of {activity['price']}")
    while True:
        
        user_choice1 = input("\nWhich one will be more suitable for you? \n")
        selected_activity = None
        for activity in data["activities"]:
            if user_choice1.lower() == activity["name"].lower():
                selected_activity = activity
                print(f"\nthank you for choosing us, your activity {selected_activity["name"]} has been successfully booked!\n") 
                break

            elif user_choice1.lower() == "back":
                return main_menu()        
            
            elif selected_activity.lower() != activity["name"].lower() or selected_activity.lower() != "back":
                print("\nThis activity is not available. Please select one from the list above, or type 'back' to return to the main menu ")  
                join_activity(username)  

        with open("gym_app.json", "w") as file: 
            json.dump(data, file, indent=4)
        booking = {"username": username, "activity": selected_activity["name"]} 
        data["bookings"].append(booking)  
        
        while True:
            back = input("\nType 'back' to go back to the main manu or 'stay' to check more activities ")
            if back.lower() == "back":
                return main_menu()
            elif back.lower() == "stay":
                print()
            else: 
                print("Please type 'back' or 'stay' to continue")
             

        
                    
    
def tap_in():
    try:
        with open("gym_app.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"personal_profile": {"frequency": 0}}

    while True:
        new_tap = input("Please type 'in' to register your exercise or 'back' to go back to the menu: ").lower()
        if new_tap == "back":
            return main_menu()
        elif new_tap == "in":
            data["personal_profile"]["frequency"] += 1
            print(f"Great! Your activity has been recorded. Total frequency: {data['personal_profile']['frequency']}")
            
            with open("gym_app.json", "w") as file:
                json.dump(data, file, indent=4)
            break
        else:
            print("Invalid input. Please type 'in' or 'back'.")
    
 

status_membership = ["none", ]
#sign_in()
print(f"membership status: {status_membership}")
main_menu()

#try: choice = input("Select your option: ")
        #except ValueError: print("\nInvalid input! Choose a number from the list.\n")
