import event
import event

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UserLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data, password):
        new_node = Node((data, password))
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data[0])
            current = current.next

class ConcertRegistrationSystem:
    def __init__(self):
        self.user_list = UserLinkedList()
        self.admin_otp_mapping = {}
        self.user_data_dict = {}

    def register_user(self, name, email, phone, password):
        user_data = f"Name: {name}, Email: {email}, Phone: {phone}"
        self.user_list.append(user_data, password)
        self.user_data_dict[email] = (phone, name, password)
        return email, phone

    def generate_otp(self, user_data):
        otp = hash(user_data) % (10 ** 6)  # Simplified OTP generation
        self.admin_otp_mapping[user_data] = otp
        return otp

    def confirm_registration(self, email, password, entered_otp):
        if email in self.user_data_dict:
            stored_otp = self.admin_otp_mapping[f"Name: {self.user_data_dict[email][1]}, Email: {email}, Phone: {self.user_data_dict[email][0]}"]
            if stored_otp == int(entered_otp) and self.user_data_dict[email][2] == password:
                return True
        return False

    def display_user_list(self):
        print("User Registrations:")
        self.user_list.display()

    def login_or_register(self):
        while True:
            choice = input("Enter 'L' to login or 'R' to register: ")
            if choice.upper() == 'L':
                login_choice = input("Enter 'E' to login with email and password or 'P' to login with phone number: ")
                if login_choice.upper() == 'E':
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    if self.confirm_registration(email, password, input("Enter OTP: ")):
                        print("Login successful!")
                        event.main() # Call the main function of the event module
                        return
                    else:
                        print("Invalid email or password. Please try again.")
                elif login_choice.upper() == 'P':
                    email = input("Enter your email: ")
                    if email in self.user_data_dict:
                        phone = input("Enter your phone number: ")
                        if phone == self.user_data_dict[email][0]:
                            print("Login successful!")
                            event.main() # Call the main function of the event module
                            return
                        else:
                            print("Invalid phone number. Please try again.")
                    else:
                        print("User not found. Please register first.")
                else:
                    print("Invalid choice. Please try again.")
            elif choice.upper() == 'R':
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                phone = input("Enter your phone number: ")
                password = input("Enter your password: ")
                email, phone = self.register_user(name, email, phone, password)
                otp = self.generate_otp(f"Name: {name}, Email: {email}, Phone: {phone}")
                print(f"OTP sent to user: {otp}")
                entered_otp = input("Enter OTP to confirm registration: ")
                if self.confirm_registration(email, password, entered_otp):
                    print("Registration confirmed!")
                    # Allow user to log in after registering
                    print("Logging in...")
                    if email in self.user_data_dict:
                        phone = input("Enter your phone number: ")
                        password = input("Enter your password: ")
                        if phone == self.user_data_dict[email][0] and password == self.user_data_dict[email][2]:
                            print("Login successful!")
                            event.main() # Call the main function of the event module
                            return
                        else:
                            print("Invalid phone number. Please try again.")
                    else:
                        print("User not found. Please register first.")
                    return
                else:
                    print("Invalid OTP or password. Registration not confirmed.")
            else:
                print("Invalid choice. Please try again.")

# Example Usage:
concert_system = ConcertRegistrationSystem()

# Login or Register
concert_system.login_or_register()

# Display User List
concert_system.display_user_list()
