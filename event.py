import random

def main():
    print("Welcome to the event menu!")
    print("Please select an option:")
    print("1. Folk Song")
    print("2. Classical Song")
    print("3. Singing Competition")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        create_event("Folk Song")
    elif choice == "2":
        edit_event("Classical Song")
    elif choice == "3":
        delete_event("Singing Competition")
    else:
        print("Invalid choice. Please try again.")

def create_event(event_type):
    # code to create a new event
    token = random.randint(1000, 9999)
    print(f"You have registered for the {event_type} event. Your token is {token}.")

def edit_event(event_type):
    # code to edit an existing event
    token = random.randint(1000, 9999)
    print(f"You have registered for the {event_type} event. Your token is {token}.")

def delete_event(event_type):
    # code to delete an event
    token = random.randint(1000, 9999)
    print(f"You have registered for the {event_type} event. Your token is {token}.")

if __name__ == "__main__":
    main()
