import json
from pathlib import Path

# --- 1. Global File Paths ---
# Defining distinct constants makes the code much safer to read and use
BASE_DIR = Path(r"E:\Ticket booking system\DATA")

ACCOUNTS_FILE = BASE_DIR / "accounts.json"
TRAINS_FILE = BASE_DIR / "train_details.json"
HISTORY_FILE = BASE_DIR / "ticket_history.json"
TICKETS_FILE = BASE_DIR / "Ticket_boocked.json" 


# --- 2. Unified Save & Load Functions ---
def save_json_data(data, file_path):
    """A single, reusable function to save any dictionary to a JSON file."""
    # This automatically creates the DATA folder if it gets deleted by accident
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4, default=str)


def load_json_data(file_path, convert_keys_to_int=False):
    """A single, reusable function to load JSON data safely."""
    try:
        with open(file_path, "r") as file:
            content = file.read().strip()
            if not content:
                return {} # Return empty if file is blank
            
            data = json.loads(content)
            
            # Convert string keys back to integers if requested
            if convert_keys_to_int and isinstance(data, dict):
                return {int(k): v for k, v in data.items()}
            return data
            
    except FileNotFoundError:
        return {} # Safe fallback if the file doesn't exist yet
    except json.JSONDecodeError as e:
        print(f"Error reading {file_path.name}: {e}. Starting with empty data.")
        return {}


# --- 3. Initialize Data Variables ---
# Now, you just call the loader for each file when the module is imported
accounts = load_json_data(ACCOUNTS_FILE, convert_keys_to_int=True)
trains = load_json_data(TRAINS_FILE)
history = load_json_data(HISTORY_FILE, convert_keys_to_int=True)
tickets = load_json_data(TICKETS_FILE, convert_keys_to_int=True)