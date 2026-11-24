
print("CAMPUS REGISTRATION IDENTIFIER ANALYZER")
print("----------------------------------------")

# Get number of student records
count = int(input("Enter number of student records: "))

valid_records = []
invalid_records = []

# Process student IDs
for i in range(count):

    print("\nStudent", i + 1)

    student_id = input(
        "Enter registration ID (YYYY-BR-NNN): "
    ).upper().strip()

    # Split the registration ID
    parts = student_id.split("-")

    # Check the number of components
    if len(parts) != 3:
        print("Invalid ID: Incorrect format.")
        invalid_records.append(student_id)
        continue

    year = parts[0]
    branch = parts[1]
    number = parts[2]

    # Validate admission year
    year_valid = (
        len(year) == 4
        and year.isdigit()
        and 2000 <= int(year) <= 2099
    )

    # Validate branch code
    valid_branches = ["CSE", "AIML", "ECE", "EEE", "MECH"]

    branch_valid = branch in valid_branches

    # Validate student number
    number_valid = (
        len(number) == 3
        and number.isdigit()
    )

    # Check complete ID
    if year_valid and branch_valid and number_valid:

        record = (student_id, year, branch, number)
        valid_records.append(record)

        print("Registration ID: VALID")
        print("Admission Year:", year)
        print("Branch:", branch)
        print("Student Number:", number)

    else:

        invalid_records.append(student_id)

        print("Registration ID: INVALID")

        if not year_valid:
            print("Error: Invalid admission year.")

        if not branch_valid:
            print("Error: Invalid branch code.")

        if not number_valid:
            print("Error: Invalid student number.")

# Display final report
print("\n========== REGISTRATION SUMMARY ==========")

print("Total Records:", count)
print("Valid Records:", len(valid_records))
print("Invalid Records:", len(invalid_records))

print("\nVALID STUDENT RECORDS")

for record in valid_records:

    student_id, year, branch, number = record

    print("\nRegistration ID:", student_id)
    print("Admission Year:", year)
    print("Branch:", branch)
    print("Student Number:", number)

print("\nINVALID STUDENT RECORDS")

for student_id in invalid_records:
    print(student_id)

print("\nRegistration Analysis Completed!")
