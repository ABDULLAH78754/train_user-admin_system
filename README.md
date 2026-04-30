🚆 Train Ticket Booking System (Python)
A console-based Train Ticket Booking System built using Python and Object-Oriented Programming (OOP) principles. This project allows users to create accounts, login, view trains, book tickets, and manage bookings, while admins can manage train data.

📌 Features
👤 User Features
Create account with validation

Secure login system (password hashing 🔒)

View available trains

Book tickets with PNR generation

Calculate fare based on distance

View booking history

🛠️ Admin Features
Add new trains

Update train timings

Modify train stations

Calculate/update fare

Delete trains

🧠 Project Structure
📦 Ticket Booking System
 ┣ 📂 module
 ┃ ┣ 📂 user_module
 ┃ ┃ ┣ booking_panal.py
 ┃ ┃ ┣ calculate_fare.py
 ┃ ┃ ┣ show_history.py
 ┃ ┃ ┗ Show_train.py
 ┃ ┣ create_account.py
 ┃ ┣ login_admin.py
 ┃ ┣ login_user.py
 ┃ ┗ file_function.py
 ┣ main.py
 ┗ DATA (JSON files)
⚙️ How It Works
🔐 Authentication System
Users create accounts with validation (age, email, password rules) 


Passwords are stored using SHA-256 hashing for security

Admin access requires special credentials

💾 Data Management
All data is stored in JSON files:

accounts.json

train_details.json

ticket_history.json

Ticket_boocked.json

Centralized file handling ensures safe read/write operations 


🎫 Booking System
User selects train and stations

Distance is calculated dynamically (excluding starting station) 


Fare is computed using:

fare = distance × 0.14
Unique PNR is generated for each booking 


🚉 Train Management (Admin)
Add train with:

Stations

Distance between stations

Travel time

Automatic calculation of:

Total distance

Journey time

Fare 


▶️ How to Run
Clone the repository:

git clone https://github.com/your-username/train-ticket-booking.git
cd train-ticket-booking
Run the main file:

python main.py
🧪 Example Workflow
Create account

Login as user/admin

View trains

Book ticket

Check booking history

🔑 Key Concepts Used
Object-Oriented Programming (OOP)

File Handling (JSON)

Password Hashing (Security)

Modular Programming

Input Validation

Error Handling

🚀 Future Improvements
GUI using Tkinter / PyQt

Database integration (MySQL / SQLite)

Online payment integration

Seat selection system

API-based real-time train data

👨‍💻 Author
Abdullah

Python Developer

Interested in AI & Software Development

⭐ Support
If you like this project:

⭐ Star the repository

🍴 Fork it

🧑‍💻 Contribute

