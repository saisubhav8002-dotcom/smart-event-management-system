#  Smart Event Management System


##  Project Overview

The Smart Event Management System is a console-based Python application designed to manage college events efficiently. It allows users to add events, register students, and manage event participation. The system also includes smart features like event clash detection, registration limits, and automatic ticket generation to simulate real-world event handling.

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

## Technologies / Tools Used

* **Programming Language:** Python
* **Concepts Used:** Functions, Lists, Dictionaries, Loops, Conditional Statements
* **Platform:** Any system with Python installed

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

1. Run the program
2. Select option `1` to add events
3. Select option `4` to add students
4. Select option `5` to register students
5. Select option `6` to view registrations
6. Try:

   * Registering more than 3 events → ❌ blocked
   * Registering overlapping events → ⚠ conflict detected

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
✅ Event Added!

Enter choice: 5
Student ID: 1
Event ID: 1
✅ Registered Successfully!
🎫 Ticket: EVT2026-001-001
```

---

## Project File

* `main.py` → Contains the complete program logic

---

## Author

Varanasi Sai Subhaprada
Project = Smart Event Management System
Language : Python

---
