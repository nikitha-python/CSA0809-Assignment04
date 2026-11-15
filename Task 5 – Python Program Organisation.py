# TASK 5: SAME UTILITY ORGANISED FOUR WAYS

# Sample attendance data
attendance = {
    "192311001": ["A", "A", "A", "P", "P"],
    "192311002": ["P", "P", "P", "P", "A"],
    "192311003": ["P", "A", "P", "A", "P"],
    "192311004": ["A", "A", "A", "A", "P"]
}


# Common utility functions
def percentage(records):
    present = records.count("P")
    total = len(records)

    return (present / total) * 100


def consecutive_absentees(data):
    result = []

    for student, records in data.items():

        for i in range(len(records) - 2):

            if records[i:i+3] == ["A", "A", "A"]:
                result.append(student)
                break

    return result


# APPROACH 1: SINGLE SCRIPT
print("===== APPROACH 1: SINGLE SCRIPT =====")

for student, records in attendance.items():
    print(student, ":", round(percentage(records), 2), "%")


# APPROACH 2: ONE MODULE IMPORTED BY MAIN SCRIPT
print("\n===== APPROACH 2: ONE MODULE =====")

def attendance_module(data):

    for student, records in data.items():
        print(student, ":", round(percentage(records), 2), "%")


attendance_module(attendance)


# APPROACH 3: THREE LOGICAL MODULES
print("\n===== APPROACH 3: THREE MODULES =====")

# Reader module
def reader_module(data):
    return data


# Statistics module
def stats_module(data):

    result = {}

    for student, records in data.items():
        result[student] = percentage(records)

    return result


# Report module
def report_module(data):

    for student, value in data.items():
        print(student, ":", round(value, 2), "%")


students = reader_module(attendance)
statistics = stats_module(students)
report_module(statistics)


# APPROACH 4: PACKAGE STYLE
print("\n===== APPROACH 4: PACKAGE STYLE =====")

# Simulating package components
def package_reader():
    return attendance


def package_stats(data):
    return stats_module(data)


def package_report(data):
    report_module(data)


package_data = package_reader()
package_result = package_stats(package_data)
package_report(package_result)


# ADDITIONAL REQUIREMENT:
# Students absent for three consecutive days

print("\n===== THREE CONSECUTIVE ABSENTEES =====")

absentees = consecutive_absentees(attendance)

for student in absentees:
    print(student)


print("\nProgram executed successfully.")
