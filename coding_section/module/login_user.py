import json
import os
import module.user_module.Show_train as show_trains
import module.user_module.show_history as show_history


# --- Main Function ---
def main():   
    while True:
        print("\n=== Welcome to the User Panel ===")
        print("1. Book a ticket.")
        print("2. View booking history.")
        print("3. Exit.")
        
        try:
            choice = int(input("Enter here: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
            
        if choice == 1:
            print("\nLoading trains...")
            show_trains()
        elif choice == 2:
            print("\nViewing booking history...")
            show_history()
        elif choice == 3:
            print("Exiting user panel... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()