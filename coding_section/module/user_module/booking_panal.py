import json
import random
import os
import module.user_module.calculate_fare as calculate_fare
import module.file_function as file_function

def booking_panel():
    trains = file_function.trains
    tickets = file_function.tickets
    history = file_function.history 
    print("\nFor booking a ticket, please enter the following details:")
    
    try:
        tr_num_input = int(input("Enter train number: "))
        tr_num = str(tr_num_input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if tr_num in trains:
        print(f"You have selected: {trains[tr_num].get('train_name', 'Unknown')}")

        # Normalize route keys
        route = {k.lower().strip(): v for k, v in trains[tr_num].get('stations', {}).items()}

        if not route:
            print("Train route data is missing!")
            return

        print("Available stations:", ", ".join(route.keys()).title())

        st = input("Enter starting journey station: ").lower().strip()
        en = input("Enter ending journey station: ").lower().strip()

        if st == en:
            print("Start and destination cannot be the same!")
            return

        if st in route and en in route:
            distance, fare = calculate_fare(route, st, en)

            print(f"Distance between stations: {distance} km")
            print(f"Ticket Fare: ${fare}")

            con = input("Confirm booking? (yes/no): ").lower()

            if con == "yes":
                PNR = random.randint(10**11, 10**12 - 1)
                print(f"✅ Booking confirmed! Your PNR is: {PNR}")
                tickets[PNR] = {
                    "train_number": tr_num,
                    "train_name": trains[tr_num].get('train_name', 'Unknown'),
                    "from": st,
                    "to": en,
                    "distance": distance,
                    "fare": fare,
                    "status": "Booked"
                }
                file_function.tic_save_data(tickets, file_function.TICKETS_FILE)

                history[PNR] = {
                    "train_id": tr_num,
                    "date": "Today",
                    "status": "Booked"
                }
                file_function.save_history(history, file_function.HISTORY_FILE)


            else:
                print("Booking cancelled.")
        else:
            print("Invalid station!")
            print("Available stations:", ", ".join(route.keys()).title())
    else:
        print("Train not found!")
