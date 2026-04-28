import random
import datetime
# Import your unified file management module
import module.file_function as file_function

def stations(num, Avg, train_number, train_name, train_time):
    station_data = {}   # Dictionary: {station_name: distance_from_last}
    W = []              # time per station

    total_time = datetime.timedelta()
    total_distance = 0.0

    for i in range(num):
        y = input("Enter station Name / exit: ").lower()
        if y == "exit":
            break

        dist = float(input("Enter distance from last station (Km): "))
        station_data[y] = dist   
        total_distance += dist

        Fare = total_distance * 0.14

        time_taken = dist / Avg   # hours
        W.append(time_taken)

        time_delta = datetime.timedelta(hours=time_taken)
        total_time += time_delta

    print(f"Stations with distance: {station_data}")
    print(f"Time per station (hrs): {W}")
    print(f"Total journey time: {total_time}")
    print(f"Total distance: {total_distance} km")
    print(f"Fare: ${Fare}")

    # Add data to the centralized dictionary
    file_function.trains[train_number] = {
        "train_name": train_name,
        "train_time": str(train_time),
        "stations": station_data,   
        "time_tr": W,
        "total_time": str(total_time),
        "total_distance": str(total_distance),
        "fare": str(Fare)
    }

    # Save using the centralized function and path
    file_function.save_json_data(file_function.trains, file_function.TRAINS_FILE)
    print("Train added successfully!")

# MENU
def admin_panel():
    # Create a local reference to keep the code below cleaner
    trains = file_function.trains 
    
    while True:
        print("\n--- Admin Panel ---")
        print("1. Add train.")
        print("2. Update time.")
        print("3. Update stations.")
        print("4. Fare")
        print("5. Delete train")
        print("6. Exit")

        try:
            F = int(input("Enter here: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if F == 1:
            train_number = random.randint(10000, 99999)
            print("Enter train Details:")
            train_name = input("Enter train name: ")

            print(f"Train no: {train_number}")

            time_input = input("Enter starting time (HH:MM:SS): ")
            try:
                h, m, s = map(int, time_input.split(":"))
                train_time = datetime.time(h, m, s)
            except ValueError:
                print("Invalid time format! Use HH:MM:SS")
                continue

            S = int(input("Enter total number of stations: "))
            Avg = float(input("Enter average speed of train: "))

            stations(S, Avg, train_number, train_name, train_time) 

        elif F == 2:
            train_number = int(input("Enter train number: "))
            if train_number in trains:
                time_input = input("Enter new starting time (HH:MM:SS): ")
                h, m, s = map(int, time_input.split(":"))
                new_time = datetime.time(h, m, s)
                
                trains[train_number]["train_time"] = str(new_time)
                file_function.save_json_data(trains, file_function.TRAINS_FILE)
                print("Train time updated successfully!")
            else:
                print("Train not found.")
                
        elif F == 3:
            train_number = int(input("Enter train number: "))
            if train_number in trains:
                S = int(input("Enter total number of stations: "))
                Avg = float(input("Enter average speed of train: "))
                stations(S, Avg, train_number, trains[train_number]["train_name"], trains[train_number]["train_time"])
            else:
                print("Train not found.")
                
        elif F == 4:
            train_number = int(input("Enter train number: "))
            doller = float(input("Enter fare per km: "))
            if train_number in trains:
                # FIX: Convert the string back to a float before multiplying
                distance = float(trains[train_number]["total_distance"])
                fare = distance * doller  
                
                trains[train_number]["fare"] = str(fare)
                file_function.save_json_data(trains, file_function.TRAINS_FILE)
                
                print(f"Total distance: {distance} km")
                print(f"Fare: ${fare}")
            else:
                print("Train not found.")  

        elif F == 5:
            train_number = int(input("Enter train number: "))
            if train_number in trains:
                del trains[train_number]
                file_function.save_json_data(trains, file_function.TRAINS_FILE)
                print("Train deleted successfully!")
            else:
                print("Train not found.")
    
        elif F == 6:
            print("Exiting admin panel...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    admin_panel()