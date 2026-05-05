import datetime
import module.file_function as file_function  # Importing the unified file management module

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