import random
import datetime
import module.file_function as file_function
import module.Admin_module.Station_save as station_save


def admin_panel():
    trains = file_function.trains

    while True:
        print("\n--- Admin Panel ---")
        print("1. Add train")
        print("2. Update time")
        print("3. Update stations")
        print("4. Fare")
        print("5. Delete train")
        print("6. Exit")

        try:
            choice = int(input("Enter here: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        # ================= ADD TRAIN =================
        if choice == 1:
            train_number = str(random.randint(10000, 99999))
            print("\nEnter Train Details")
            train_name = input("Enter train name: ")

            print(f"Train no: {train_number}")

            time_input = input("Enter starting time (HH:MM:SS): ")
            try:
                h, m, s = map(int, time_input.split(":"))
                train_time = datetime.time(h, m, s)
            except ValueError:
                print("Invalid time format!")
                continue

            try:
                total_stations = int(input("Enter total number of stations: "))
                avg_speed = float(input("Enter average speed: "))
            except ValueError:
                print("Invalid number input!")
                continue

            # 🔥 SAVE TRAIN (IMPORTANT FIX)
            trains[train_number] = {
                "train_name": train_name,
                "train_time": str(train_time),
                "total_stations": total_stations,
                "avg_speed": avg_speed,
                "total_distance": "0",
                "fare": "0"
            }

            file_function.save_json_data(trains, file_function.TRAINS_FILE)

            # Call station function
            station_save.stations(
                total_stations,
                avg_speed,
                train_number,
                train_name,
                train_time
            )

            print("✅ Train added successfully!")

        # ================= UPDATE TIME =================
        elif choice == 2:
            train_number = input("Enter train number: ")

            if train_number in trains:
                time_input = input("Enter new time (HH:MM:SS): ")

                try:
                    h, m, s = map(int, time_input.split(":"))
                    new_time = datetime.time(h, m, s)
                except ValueError:
                    print("Invalid time format!")
                    continue

                trains[train_number]["train_time"] = str(new_time)
                file_function.save_json_data(trains, file_function.TRAINS_FILE)

                print("✅ Time updated successfully!")
            else:
                print("❌ Train not found")

        # ================= UPDATE STATIONS =================
        elif choice == 3:
            train_number = input("Enter train number: ")

            if train_number in trains:
                try:
                    total_stations = int(input("Enter total stations: "))
                    avg_speed = float(input("Enter avg speed: "))
                except ValueError:
                    print("Invalid input!")
                    continue

                station_save.stations(
                    total_stations,
                    avg_speed,
                    train_number,
                    trains[train_number]["train_name"],
                    trains[train_number]["train_time"]
                )

                print("✅ Stations updated!")
            else:
                print("❌ Train not found")

        # ================= FARE =================
        elif choice == 4:
            train_number = input("Enter train number: ")

            try:
                rate = float(input("Enter fare per km: "))
            except ValueError:
                print("Invalid fare input!")
                continue

            if train_number in trains:
                distance = float(trains[train_number].get("total_distance", 0))
                fare = distance * rate

                trains[train_number]["fare"] = str(fare)
                file_function.save_json_data(trains, file_function.TRAINS_FILE)

                print(f"Total distance: {distance} km")
                print(f"Fare: ₹{fare}")
            else:
                print("❌ Train not found")

        # ================= DELETE =================
        elif choice == 5:
            train_number = input("Enter train number: ")

            if train_number in trains:
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    del trains[train_number]
                    file_function.save_json_data(trains, file_function.TRAINS_FILE)
                    print("✅ Train deleted!")
            else:
                print("❌ Train not found")

        # ================= EXIT =================
        elif choice == 6:
            print("Exiting admin panel...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    admin_panel()