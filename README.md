# Smart Event Management System

The Smart Event Management System is a Python-based application designed to manage college events efficiently. It allows administrators to create and manage events while enabling students to register for them. The system includes intelligent features like conflict detection, registration limits, and automatic ticket generation to simulate real-world event scheduling.

## Objectives
-To develop a structured system for managing college events
-To implement database operations using SQLite
-To provide a user-friendly interface for event registration
-To prevent scheduling conflicts between events
-To simulate real-world event management scenarios

## Features
- Add, view, and delete events
- Add and manage students
- Event registration system
- Automatic ticket ID generation
- Registration limit (max 3 events per student)
- Smart event scheduling logic
- Organized database structure

## Unique Features
- Smart registration limit system
- Auto ticket generation
- Modular Python structure
- Real-world simulation logic

## Technologies / Tools Used
- Programming Language: Python
- Database: SQLite (built-in)
- Tools: VS Code / Any Python IDE
- Version Control: Git & GitHub

## Installation and Setup
Step 1: Install Python
Download and install Python 3 on your computer.

After installation, open Command Prompt / Terminal and check whether Python is installed:

python --version
If required, use:

python3 --version
You should see the installed Python version.


1. Clone the repository
git clone <https://github.com/saisubhav8002-dotcom/smart-event-management-system>
cd smart-event-management-system
2. Run the project
python main.py

✔ No additional installations required
✔ Database will be created automatically

## Login Details

This system currently does not require login authentication.

All operations are menu-driven through the terminal.

(Optional upgrade: Admin/Student login system can be added later)

## Instructions for Testing
Step 1: Add Events
Choose option 1
Enter event details (name, date, time, etc.)

Step 2: Add Students
Choose option 4
Enter student name and email

Step 3: Register for Events
Choose option 5
Enter student ID and event ID
System will generate a ticket ID

Step 4: View Registrations
Choose option 6
Displays all registered students with event details

Step 5: Test Constraints        
Try registering more than 3 events → blocked
Try multiple registrations → observe ticket generation


## Run
```bash
python main.py
python gui.py
