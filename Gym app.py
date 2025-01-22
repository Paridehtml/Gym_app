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
    print("3. Check your progress\n")
    print("4. Tap in\n")
    print("5. Your profile\n")
    choice = input("What you want to do today? type here a number from the list: ")
    if choice == "1": get_mermbership()
        
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
        else: print("Please enter a valid number")

def join_activity():
    print("\n----- ACTIVITIES -----\n")
    print("Book an activity secting one of the following:\n")
    print("1. Pilates\n")
    print("2. Box\n")
    print("3. Swim class\n")

 

status_membership = ["none", ]
print(f"membership status: {status_membership}")
main_menu()
#sign_in()
#try: choice = input("Select your option: ")
        #except ValueError: print("\nInvalid input! Choose a number from the list.\n")