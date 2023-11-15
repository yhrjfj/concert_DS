def main():
    print("Welcome to the event menu!")
    print("Please select an option:")
    print("1. Create new event")
    print("2. Edit existing event")
    print("3. Delete event")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        create_event()
    elif choice == "2":
        edit_event()
    elif choice == "3":
        delete_event()
    else:
        print("Invalid choice. Please try again.")

def create_event():
    # code to create a new event
    pass

def edit_event():
    # code to edit an existing event
    pass

def delete_event():
    # code to delete an event
    pass

if __name__ == "__main__":
    main()
