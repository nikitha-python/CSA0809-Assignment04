# Sample daily attendance files
files = {
    "day1.txt": """192311001,2026-10-08,P 192311002,2026-10-08,A 192311003,2026-10-08,P""",

    "day2.txt": """192311001,2026-10-09,P 192311002,2026-10-09,P 192311003,2026-10-09""",

    "day3.txt": """192311001,2026-10-10,A 192311002,2026-10-10,A 192311003,2026-10-10,P"""
}

attendance = {}
damaged_records = []

# Process each daily file
for filename, content in files.items():

    lines = content.splitlines()

    for line_number, line in enumerate(lines, start=1):

        parts = line.strip().split(",")

        if len(parts) != 3 or parts[2] not in ("P", "A"):
            damaged_records.append(
                filename + ", Line " + str(line_number) +
                ": " + line
            )
            continue

        register_no, date, status = parts

        if register_no not in attendance:
            attendance[register_no] = [0, 0]

        if status == "P":
            attendance[register_no][0] += 1

        attendance[register_no][1] += 1


# Display attendance report
print("===== ATTENDANCE REPORT =====")

print("Register No. | Present | Total | Percentage")

for student, counts in attendance.items():

    present = counts[0]
    total = counts[1]

    percentage = (present / total) * 100

    print(
        student, "|",
        present, "|",
        total, "|",
        round(percentage, 2), "%"
    )


# Display students below 75%
print("\n===== STUDENTS BELOW 75% =====")

for student, counts in attendance.items():

    percentage = (counts[0] / counts[1]) * 100

    if percentage < 75:
        print(student)


# Display damaged records
print("\n===== DAMAGED RECORDS =====")

for record in damaged_records:
    print(record)

print("\nProcessing completed.")
