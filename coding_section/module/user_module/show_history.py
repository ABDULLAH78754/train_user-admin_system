import json
import module.file_function as filefunction

def show_history():
    history = filefunction.history
    if not history:
        print("\nNo booking history available.")
        return
    
    print("\n--- Booking History ---")
    for booking_id, details in history.items():
        print(f"Booking/PNR ID: {booking_id}")
        print(f"  User ID: {details.get('current_user', 'N/A')}")
        print(f"  Train ID: {details.get('train_id', 'N/A')}")
        print(f"  Date: {details.get('date', 'N/A')}")
        print(f"  Status: {details.get('status', 'N/A')}")
        print("-" * 20)