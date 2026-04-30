🚆 Ticket Booking System (Python)
A simple command-line based Ticket Booking System built using Python.
This project allows users to create accounts, login, view trains, book tickets, and manage travel history. It also includes an Admin panel for managing trains and fares.

A good README acts as the first impression of your project and helps users understand how to use it effectively 

📌 Features
👤 User Features
Create account (User/Admin)

Login system with authentication

View available trains

Book tickets

Calculate fare automatically

View booking history

🛠️ Admin Features
Add new trains

Update train timings

Update stations & routes

Set fare per km

Delete trains

🧱 Project Structure
Ticket Booking System/
│
├── main.py                  # Main entry point
├── module/
│   ├── create_account.py    # Account creation
│   ├── login_admin.py       # Admin panel
│   ├── login_user.py        # User panel
│   ├── file_function.py     # File handling (JSON)
│
│   └── user_module/
│       ├── booking_panal.py
│       ├── calculate_fare.py
│       ├── show_history.py
│       ├── Show_train.py
│
└── DATA/
    ├── accounts.json
    ├── train_details.json
    ├── ticket_history.json
    └── Ticket_boocked.json
⚙️ How It Works
The system uses JSON files to store data such as:

Accounts

Train details

Booking history

Tickets

A centralized file handler (file_function.py) manages all read/write operations
→ Example: 


The main program (main.py) controls user flow:
→ Example: 


🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/ticket-booking-system.git
cd ticket-booking-system
2. Run the project
python main.py
🖥️ Usage
Main Menu
1. Create Account
2. Login Account
3. Exit
After Login
User Panel

Book ticket

View history

Admin Panel

Add / Update / Delete trains

Manage fare

💰 Fare Calculation Logic
Distance is calculated between selected stations

Fare is calculated as:

Fare = Distance × 0.14
→ Implementation: 


📂 Data Storage
All data is stored locally using JSON:

Safe loading with error handling

Automatic file creation if missing

Integer key conversion for IDs

⚠️ Requirements
Python 3.x

No external libraries required (pure Python)

🧠 Future Improvements
GUI version (Tkinter / Web app)

Online database (MySQL / Firebase)

Payment integration

Seat selection system

Multi-user session handling

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a new branch

Make changes

Submit a pull request

📄 License
This project is open-source and available under the MIT License.

👨‍💻 Author
Abdullah

B.Tech Student

Interested in Python, AI & Software Development

