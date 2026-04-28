import json
import os
import module.user_module.booking_panal as booking_panel
import module.file_function as file_function

trains = file_function.trains

def show_trains():
    
    print("\n--- Available Trains ---")
    for train_id, details in trains.items():
        print(f"Train ID: {train_id}")
        print(f"  Name: {details.get('train_name', 'N/A')}")
        print(f"  Number: {details.get('train_number', 'N/A')}")
        print(f"  Time: {details.get('train_time', 'N/A')}")
        
        # Safely extract dictionary keys for station names
        stations = details.get('stations', {})
        if isinstance(stations, dict):
            station_list = list(stations.keys())
        else:
            station_list = stations # fallback if it's already a list
            
        print(f"  Stations: {', '.join(station_list).title()}")
        print("-" * 20)
    
    # Proceed to booking after showing trains
    booking_panel()