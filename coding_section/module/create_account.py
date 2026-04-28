import random
import json
import module.file_function as file_function

Admin_Id=6556
Admin_pin=1212


#Save account details function


def main():

    accounts = file_function.accounts
    print("1. Admin account")
    print("2. User account")

    B=int(input("Enter here:"))
            #Admine account creating section
    if B==1:
        C=int(input("Enter pre define Id:"))
        D=int(input("Enter pre define pin:"))
                #admin account section
        if C==Admin_Id and D==Admin_pin:
            print("Enter your details:")
            account_name=input("Enter your Name:")
            age=int(input("Enter your age:"))
            if age>=18:
                ID_PROOF=int(input("Enter your Id number:"))
                phone_no = int(input("Enter your phone number:"))
                Password=input("Create password:")
                Account_type="Admin"
                account_number=random.randint(10**11,10**12)
                print(f"Login ID:{account_number}")
                accounts[account_number] = {
                    "name": account_name,
                    "age": age,
                    "pin": Password,
                    "phone": phone_no,
                    "id_proof": ID_PROOF,
                    "Account_ty": Account_type 
                    }
                         # Save to file
                file_function.save_json_data(accounts, file_function.ACCOUNTS_FILE)

                print("Your account created successfully!.")
            else:
                print("You are not eligible due to your age.")
        else:
            print("Invalid details.")
            #user account
    elif B==2:
        print("Enter your details:")
        account_name=input("Enter your Name:")
        age=int(input("Enter your age:"))
        if age>=18:
            ID_PROOF=int(input("Enter your Id number:"))
            phone_no = int(input("Enter your phone number:"))
            Password=input("Enter Password:")
            Account_type="User"
            account_number=random.randint(10**11,10**12)
            print(f"LOGIN ID:{account_number}")
            accounts[account_number] = {
                "name": account_name,
                "age": age,
                "pin": Password,
                "phone": phone_no,
                "id_proof": ID_PROOF,
                "Account_ty": Account_type
                }
                         # Save to file
            file_function.save_json_data(accounts, file_function.ACCOUNTS_FILE)

            print("Your account created successfully!.")
        else:
            print("You are not eligible due to your age.")
    else:
        print("Invalid option.")
if __name__ == "__main__":
    main()