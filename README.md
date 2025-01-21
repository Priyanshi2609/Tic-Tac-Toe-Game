# Tic-Tac-Toe Game with Flask and Socket.IO

This is a multiplayer Tic-Tac-Toe game built using Python Flask, Flask-SocketIO, and Flask-Login. It features user authentication, real-time gameplay, and a responsive interface created with HTML, CSS, and JavaScript.

---

## Features

- **User Registration & Login**:  
  Secure user authentication system with session management.
  
- **Real-Time Gameplay**:  
  Players can compete in real-time with live updates using WebSockets.
  
- **Game Logic**:  
  Turn-based gameplay, win/draw detection, and invalid move prevention.

- **Technology Stack**:  
  Backend: Flask, Flask-SQLAlchemy, Flask-SocketIO, Flask-Login  
  Frontend: HTML, CSS, JavaScript  
  Database: SQLite  

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Priyanshi2609/Tic-Tac-Toe-Game.git
cd Tic-Tac-Toe-Game
## Setup Instructions

### Step 1: Clone the Repository
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/Priyanshi2609/Tic-Tac-Toe-Game.git
cd Tic-Tac-Toe-Game
Step 2: Install Dependencies
Install the required Python packages:

bash
Copy
Edit
pip install flask flask-sqlalchemy flask-login flask-socketio
Step 3: Initialize the Database
Create the SQLite database:

bash
Copy
Edit
python
>>> from app import db
>>> db.create_all()
>>> exit()
Step 4: Run the Application
Start the development server:

bash
Copy
Edit
python app.py
