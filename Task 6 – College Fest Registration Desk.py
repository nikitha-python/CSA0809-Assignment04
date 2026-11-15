# TASK 6: COLLEGE FEST REGISTRATION DESK

class InvalidRecord(Exception):
    """Custom exception for invalid registration records."""


# Sample registration data from five departments
department_data = {
    "ECE": [
        "101,Arun,arun@gmail.com,Robotics",
        "102,Bala,bala@gmail.com,AI"
    ],

    "CSE": [
        "103,Charan,charan@gmail.com,AI",
        "104,Divya,divya@gmail.com,Coding"
    ],

    "EEE": [
        "105,Ezhil,ezhil@gmail.com,Robotics",
        "101,Arun,arun@gmail.com,Robotics"
    ],

    "MECH": [
        "106,Kumar,kumar@gmail.com,Design",
        "107,Ravi,invalidemail,Robotics"
    ],

    "CIVIL": [
        "108,Mani,mani@gmail.com,AI",
        "109,John,john@gmail.com"
    ]
}


# Email validation function
def validate_email(email):

    if "@" not in email:
        return False

    if "." not in email:
        return False

    if email.startswith("@") or email.endswith("@"):
        return False

    if " " in email:
        return False

    return True


# Registration processing function
def process_registrations(data):

    registrations = []
    registered_ids = set()
    errors = []

    for department, records in data.items():

        for line_number, line in enumerate(records, start=1):

            try:
                parts = line.strip().split(",")

                # Check number of fields
                if len(parts) != 4:
                    raise InvalidRecord(
                        "Incorrect number of fields"
                    )

                reg_id, name, email, event = parts

                # Validate email
                if not validate_email(email):
                    raise InvalidRecord(
                        "Invalid email address"
                    )

                # Check duplicate registration
                if reg_id in registered_ids:
                    raise InvalidRecord(
                        "Duplicate registration ID"
                    )

                # Store valid registration
                registered_ids.add(reg_id)

                registrations.append({
                    "ID": reg_id,
                    "Name": name,
                    "Email": email,
                    "Event": event,
                    "Department": department
                })

            except InvalidRecord as error:

                errors.append(
                    department + " - Line " +
                    str(line_number) + ": " + str(error)
                )

    return registrations, errors


# Process all department registrations
registrations, errors = process_registrations(department_data)


# Display master registration list
print("========== MASTER REGISTRATION LIST ==========")

for student in registrations:

    print(
        student["ID"], "|",
        student["Name"], "|",
        student["Email"], "|",
        student["Event"], "|",
        student["Department"]
    )


# Generate event-wise summary
print("\n========== EVENT-WISE SUMMARY ==========")

event_count = {}

for student in registrations:

    event = student["Event"]

    event_count[event] = event_count.get(event, 0) + 1

for event, count in event_count.items():

    print(event, ":", count, "participants")


# Display error log
print("\n========== ERROR LOG ==========")

if len(errors) == 0:
    print("No errors found.")

else:
    for error in errors:
        print(error)


# Demonstrate missing department file
print("\n========== MISSING DEPARTMENT FILE TEST ==========")

try:
    if "CIVIL_MISSING" not in department_data:
        raise FileNotFoundError("Department file not found")

except FileNotFoundError as error:
    print(error)


# Final summary
print("\n========== FINAL SUMMARY ==========")

print("Total Valid Registrations:", len(registrations))
print("Total Invalid Records:", len(errors))
print("Total Events:", len(event_count))

print("\nCollege Fest Registration Processing Completed.")
