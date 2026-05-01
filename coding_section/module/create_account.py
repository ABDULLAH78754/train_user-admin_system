import json
import random
import os
import hashlib
import module.file_function as file_function  # Importing the unified file management module

class SaveData:
    
    def save(self, account):
        file_function.accounts[account.account_number] = {
            "name": account.name,
            "age": account.age,
            "phone": account.phone,
            "email": account.email,
            "id_proof": account.id_proof,
            "address": account.address,
            "password": self.hash_password(account.password),
            "account_type": account.account_type
        }

        file_function.save_json_data(file_function.accounts, file_function.ACCOUNTS_FILE)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


def Account_type(account_type, admin_id=None, admin_pin=None):
    if account_type == 1:
        if admin_id == 6556556 and admin_pin == 123456:
            return "Admin"
        else:
            print("❌ Invalid Admin credentials")
            return "Unknown"
    elif account_type == 2:
        return "User"
    else:
        return "Unknown"
    

class Account:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.phone = ""
        self.email = ""
        self.id_proof = ""
        self.address = ""
        self.password = ""
        self.account_number = random.randint(10**11, 10**12 - 1)
        self.account_type = ""

    def take_input(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.phone = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.id_proof = input("Enter your ID proof: ")
        self.address = input("Enter your address: ")
        self.password = input("Enter your password: ")
        self.account_type = int(input("Enter your account type(Admin - 1, User - 2): "))
        if self.account_type == 1:
            admin_id = int(input("Enter Admin ID: "))
            admin_pin = int(input("Enter Admin PIN: "))
            self.account_type = Account_type(self.account_type, admin_id, admin_pin)
        else:
            self.account_type = Account_type(self.account_type)  # Set account type


    def validate(self):
        valid = True

        if self.age < 18:
            print("❌ You are not eligible.")
            valid = False

        if len(self.password) < 8 or len(self.password) > 16:
            print("❌ Password must be 8–16 characters.")
            valid = False

        if not any(c.isupper() for c in self.password):
            print("❌ Add uppercase letter.")
            valid = False

        if not any(c.islower() for c in self.password):
            print("❌ Add lowercase letter.")
            valid = False

        if not any(c.isdigit() for c in self.password):
            print("❌ Add a number.")
            valid = False

        if not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in self.password):
            print("❌ Add special character.")
            valid = False

        if not self.email.endswith("@gmail.com"):
            print("❌ Invalid email.")
            valid = False

        if not (len(self.phone) == 10 and self.phone.isdigit()):
            print("❌ Invalid phone.")
            valid = False

        if not (self.id_proof.isdigit() and len(self.id_proof) == 12):
            print("❌ Invalid ID.")
            valid = False

        return valid

    def display(self):
        print("\n✅ Account Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("ID Proof:", self.id_proof)
        print("Address:", self.address)
        print("Account Number:", self.account_number)


# Main Program
def main():
    print("Welcome to the account creation process.")
    user = Account()
    user.take_input()

    if user.validate():
        print("\n🎉 Account created successfully!")
    
        saver = SaveData()
        saver.save(user)   # ✅ moved here
    
        user.display()
    else:
        print("\n⚠️ Fix errors and try again.")

if __name__ == "__main__":
    main()