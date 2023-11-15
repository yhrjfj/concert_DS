class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UserLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
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
            print(current.data)
            current = current.next

class ConcertRegistrationSystem:
    def __init__(self):
        self.user_list = UserLinkedList()
        self.admin_otp_mapping = {}

    def register_user(self, name, email, phone):
        user_data = f"Name: {name}, Email: {email}, Phone: {phone}"
        self.user_list.append(user_data)
        return user_data

    def generate_otp(self, user_data):
        otp = hash(user_data) % (10 ** 6)  # Simplified OTP generation
        self.admin_otp_mapping[user_data] = otp
        return otp

    def confirm_registration(self, user_data, entered_otp):
        if user_data in self.admin_otp_mapping:
            stored_otp = self.admin_otp_mapping[user_data]
            return stored_otp == int(entered_otp)
        return False

    def display_user_list(self):
        print("User Registrations:")
        self.user_list.display()

    def login_or_register(self):
        while True:
            choice = input("Enter 'L' to login or 'R' to register: ")
            if choice.upper() == 'L':
                email = input("Enter your email: ")
                phone = input("Enter your phone number: ")
                user_data = f"Email: {email}, Phone: {phone}"
                if user_data in self.admin_otp_mapping:
                    otp = self.admin_otp_mapping[user_data]
                    entered_otp = input("Enter OTP to login: ")
                    if otp == int(entered_otp):
                        print("Login successful!")
                        return
                    else:
                        print("Invalid OTP. Please try again.")
                else:
                    print("User not found. Please register first.")
            elif choice.upper() == 'R':
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                phone = input("Enter your phone number: ")
                user_data = self.register_user(name, email, phone)
                otp = self.generate_otp(user_data)
                print(f"OTP sent to user: {otp}")
                entered_otp = input("Enter OTP to confirm registration: ")
                if self.confirm_registration(user_data, entered_otp):
                    print("Registration confirmed!")
                    return
                else:
                    print("Invalid OTP. Registration not confirmed.")
            else:
                print("Invalid choice. Please try again.")

# Example Usage:
concert_system = ConcertRegistrationSystem()

# Login or Register
concert_system.login_or_register()

# Display User List
concert_system.display_user_list()
