# TASK 4: FILE AND EXCEPTION FORENSICS

# Function to save returned books
def save_returns(books):
    try:
        with open("returns.log", "a") as log:
            for book in books:
                log.write(book + "\n")

    except PermissionError:
        print("Permission denied while writing file")

    except OSError as error:
        print("File error:", error)


# Function to process daily return files
def process(day_file):
    try:
        with open(day_file, "r") as file:
            books = file.read().splitlines()

        save_returns(books)
        print(day_file, "processed successfully")

    except FileNotFoundError:
        print("Missing file:", day_file)

    except PermissionError:
        print("Permission denied:", day_file)

    except OSError as error:
        print("File error:", error)


# Create sample daily files
daily_files = {
    "day1.txt": "Python\nDigital Electronics\n",
    "day2.txt": "Communication Systems\nMicroprocessors\n",
    "day3.txt": "Embedded Systems\nIoT\n"
}

# Create daily files and process them
for filename, content in daily_files.items():

    try:
        with open(filename, "w") as file:
            file.write(content)

        process(filename)

    except PermissionError:
        print("Cannot create:", filename)


# Display final returns log
print("\n===== FINAL RETURNS LOG =====")

try:
    with open("returns.log", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Returns log not found")


# Demonstrate missing file exception
print("===== EXCEPTION TEST =====")

process("missing_day.txt")
