import json

# Assuming these modules are correctly set up in your project structure
import module.create_account as create_account
import module.login_admin as login_admin    
import module.login_user as login_user
import module.file_function as file_functions 

# ================= MAIN APPLICATION =================
def main():
    # Load initial data
    # Note: trains are loaded here just in case you need them in the main menu later,
    # though currently, your login modules handle train data directly.
    accounts = file_functions.ACCOUNTS_FILE
    while True:
        
        print("\n===== Ticket Booking Platform =====")
        print("1. Create account")
        print("2. Login Account")
        print("3. Exit")

        choice = int(input("Enter here (1-3):  "))

        # Create account
        if choice == 1:
            # We pass the consolidated save function as the callback
            create_account.main()
            
        # Login Account
        elif choice == 2:
            print("\nLogin as:")
            acc_num=int(input("Enter your login ID: "))
            pin = input("Enter your password: ")
            if acc_num in accounts and accounts[acc_num]["pin"] == pin and accounts[acc_num]["Account_ty"] == "Admin":
                print(f"Welcome, {accounts[acc_num]['name']}! You have successfully logged in as an Admin.")
                login_admin.admin_panel()

            elif acc_num in accounts and accounts[acc_num]["pin"] == pin and accounts[acc_num]["Account_ty"] == "User":
                login_user.main()

            else:
                print("Invalid login credentials! Please try again.")
if __name__ == "__main__":
    main()