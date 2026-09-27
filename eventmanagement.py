# DATA STORAGE
events = []
students = []
registrations = []

event_id_counter = 1
student_id_counter = 1


# GENERATE TICKET
def generate_ticket(event_id, student_id):
    return f"EVT2026-{event_id:03d}-{student_id:03d}"

# TIME CONFLICT CHECK
def time_conflict(start1, end1, start2, end2):
    return not (end1 <= start2 or start1 >= end2)


# EVENT FUNCTIONS
def add_event():
    global event_id_counter

    name = input("Event Name: ")
    date = input("Date: ")
    start = input("Start Time: ")
    end = input("End Time: ")
    location = input("Location: ")
    desc = input("Description: ")

    event = {
        "id": event_id_counter,
        "name": name,
        "date": date,
        "start": start,
        "end": end,
        "location": location,
        "desc": desc
    }

    events.append(event)
    event_id_counter += 1

    print("Event Added!")


def view_events():
    print("\n--- EVENTS ---")
    for e in events:
        print(e)


def delete_event():
    eid = int(input("Enter Event ID: "))
    global events
    events = [e for e in events if e["id"] != eid]
    print("Event Deleted")


# STUDENT FUNCTIONS
def add_student():
    global student_id_counter

    name = input("Student Name: ")
    email = input("Email: ")

    student = {
        "id": student_id_counter,
        "name": name,
        "email": email
    }

    students.append(student)
    student_id_counter += 1

    print("Student Added!")


# REGISTRATION 
def register():
    sid = int(input("Student ID: "))
    eid = int(input("Event ID: "))

    # LIMIT CHECK
    count = sum(1 for r in registrations if r["student_id"] == sid)
    if count >= 3:
        print("Limit reached (max 3 events)")
        return

    # CONFLICT CHECK
    student_events = [r["event_id"] for r in registrations if r["student_id"] == sid]

    new_event = next((e for e in events if e["id"] == eid), None)

    for ev_id in student_events:
        old_event = next((e for e in events if e["id"] == ev_id), None)

        if old_event and new_event:
            if old_event["date"] == new_event["date"]:
                if time_conflict(old_event["start"], old_event["end"],
                                 new_event["start"], new_event["end"]):
                    print("Time conflict with another event!")
                    return

    ticket = generate_ticket(eid, sid)

    registrations.append({
        "student_id": sid,
        "event_id": eid,
        "ticket": ticket
    })

    print("Registered Successfully!")
    print("Ticket:", ticket)


def view_registrations():
    print("\n--- REGISTRATIONS ---")
    for r in registrations:
        print(r)


# MENU
def menu():
    print("\n===== EVENT MANAGEMENT SYSTEM =====")
    print("1. Add Event")
    print("2. View Events")
    print("3. Delete Event")
    print("4. Add Student")
    print("5. Register for Event")
    print("6. View Registrations")
    print("7. Exit")


# MAIN LOOP
while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_event()

    elif choice == "2":
        view_events()

    elif choice == "3":
        delete_event()

    elif choice == "4":
        add_student()

    elif choice == "5":
        register()

    elif choice == "6":
        view_registrations()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
