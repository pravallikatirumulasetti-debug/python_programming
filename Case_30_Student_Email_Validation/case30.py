
print("STUDENT EMAIL AND IDENTIFIER VALIDATION")
print("----------------------------------------")

# Get student details
name = input("Enter student name: ")
email = input("Enter student email: ")
student_id = input("Enter student ID: ")

# Check student name
name_valid = len(name.strip()) > 0

# Check email format
email = email.strip()

email_valid = (
    email.count("@") == 1
    and email.index("@") > 0
    and "." in email.split("@")[1]
    and not email.endswith(".")
    and " " not in email
)

# Check student ID
student_id = student_id.strip()

id_valid = (
    student_id.startswith("STU")
    and len(student_id) == 8
    and student_id[3:].isdigit()
)

# Display validation results
print("\nVALIDATION RESULTS")
print("------------------")

print("Student Name:", "Passed" if name_valid else "Failed")
print("Email Address:", "Passed" if email_valid else "Failed")
print("Student ID:", "Passed" if id_valid else "Failed")

# Final result
if name_valid and email_valid and id_valid:
    print("\nStudent Details: VALID")
else:
    print("\nStudent Details: INVALID")

print("\nValidation Completed!")
