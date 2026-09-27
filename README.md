#  Smart Event Management System


##  Project Overview

The Smart Event Management System is a Python based application designed to manage college events efficiently. It allows users to add events, register students, and manage event participation. The system also includes smart features like event clash detection, registration limits, and automatic ticket generation to simulate real-world event handling.

---

## Objectives

- To build a structured event management system using Python
- To understand and implement functions, lists, and dictionaries
- To simulate real-world event registration scenarios
- To implement logic like conflict detection and validation
- To improve programming and problem-solving skills

---

## Features

- Add events
- View all events
- Delete events
- Add students
- Register students for events
- Automatic ticket ID generation
- Event clash detection (no overlapping events)
- Registration limit (max 3 events per student)

---

## Future Improvements

* Add database for persistent storage
* Implement GUI or web interface
* Add login system
* Add analytics and reporting

---

## Technologies / Tools Used

* **Programming Language:** Python
* **Concepts Used:**
  - Functions
  - Lists
  - Dictionaries
  - Loops
  - Conditional
  - Statements
* **Platform:** Visual Studio Code

---

## Installation and Setup

### Step 1: Install Python

Download and install Python from:
 [Python Official Website](https://www.python.org/downloads/?utm_source=chatgpt.com)

---

### Step 2: Download the Project

You can either download manually or clone using Git:

```bash
https://github.com/saisubhav8002-dotcom/smart-event-management-system
```

---

### Step 3: Navigate to the Project Folder

```bash
cd smart-event-management-system
```

---

### Step 4: Verify the Project Files

Make sure you have:

```text
 main.py
 README.md
 eventmanagement.py
```
---

### Step 5: Run the Program

Open Command Prompt or Terminal inside the project folder and run:

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```
---

## Login Details

This project does **not require login credentials**.
All operations are performed through a menu-driven interface.

---

## Instructions for Testing

Run the program using python main.py\
You will see the main menu\
Follow options step-by-step:

### Test Case 1:
Add Event\
Choose option 1\
Enter event details (name, date, time, etc.)\
Verify:\
Message “Event Added!” appears\
Event shows in “View Events”

### Test Case 2:
View Events\
Choose option 2\
Verify:\
All added events are displayed\
IDs are correctly assigned

### Test Case 3: 
Add Student\
Choose option 4\
Enter student name and email\
Verify:\
“Student Added!” message appears

### Test Case 4:
Register Student for Event\
Choose option 5\
Enter valid Student ID and Event ID\
Verify:\
Registration is successful\
Ticket ID is generated (e.g., EVT2026-001-001)

### Test Case 5:
Registration Limit Check\
Register the same student for 3 events\
Try registering for a 4th event\
Expected Result:\
System blocks registration\
Shows “Limit reached” message

### Test Case 6:
Event Time Conflict\
Create 2 events with overlapping time\
Register same student for first event\
Try registering for second event\
Expected Result:\
Conflict message displayed\
Registration blocked

### Test Case 7:
View Registrations\
Choose option 6\
Verify:\
All registrations are displayed\
Ticket IDs are shown correctly

### Test Case 8:
Delete Event\
Choose option 3\
Enter Event ID\
Verify:\
Event is removed from list

### Edge Case Testing
Enter invalid IDs → should not crash\
Enter empty values → observe behavior\
Try registering without adding student/event

---

## Sample Output

```
===== EVENT MANAGEMENT SYSTEM =====
1. Add Event
2. View Events
3. Delete Event
4. Add Student
5. Register for Event
6. View Registrations
7. Exit

Enter choice: 1
Event Name: Hackathon
Date: 2026-10-01
Start Time: 10:00
End Time: 12:00
Location: Auditorium
Description: Coding Event
Event Added!

Enter choice: 5
Student ID: 1
Event ID: 1
Registered Successfully!
Ticket: EVT2026-001-001
```

---

## Project File

Smart-Event-Mangaement-System/\
|\
|-- main.py\
|-- README.md\
|-- eventmanagement.py


---

## Author

Varanasi Sai Subhaprada\
Project = Smart Event Management System\
Language : Python

