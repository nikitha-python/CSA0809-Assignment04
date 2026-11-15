class InvalidRecord(Exception):
    """Raised when an attendance record is invalid."""


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    if parts[2] not in ("P", "A"):
        raise InvalidRecord(
            f"invalid status '{parts[2]}'"
        )

    return tuple(parts)


def summarise(data):
    present = 0
    absent = 0
    errors = []

    for line_number, line in enumerate(data.splitlines(), start=1):
        try:
            register_no, date, status = parse_line(line)

            if status == "P":
                present += 1
            else:
                absent += 1

        except InvalidRecord as error:
            errors.append((line_number, str(error)))

    return present, absent, errors


# Sample attendance data
data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

# Process attendance
print("Attendance Processing Result:")
print(summarise(data))


# Demonstrate missing file exception
print("\nTesting FileNotFoundError:")

try:
    with open("missing_file.csv", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: File not found")
