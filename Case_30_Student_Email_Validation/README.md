
# Case Study 30: Student Email and Identifier Validation

## 1. Problem Statement

Develop a Python program to validate student details, including student name, email address, and student ID. The program checks whether the entered information follows predefined validation rules and displays whether the student details are VALID or INVALID.

## 2. Objectives

- To understand string operations in Python.
- To validate student email addresses.
- To check student ID formats.
- To use conditional statements and logical operators.
- To apply string methods such as strip(), count(), split(), and startswith().
- To display validation results clearly.
- To improve logical thinking and problem-solving skills.

## 3. Assumptions

- The user enters the student name as a string.
- The email address must contain exactly one @ symbol.
- The email address must contain a dot after the @ symbol.
- The email address must not contain spaces.
- The email address must not end with a dot.
- The student ID must start with "STU".
- The student ID must contain exactly 8 characters.
- The last five characters of the student ID must be digits.
- These are basic classroom validation rules, not complete real-world email verification.

## 4. Technologies Used

- Programming Language: Python
- Code Editor: Visual Studio Code
- Concepts: Variables, Strings, Conditional Statements, Logical Operators and String Methods.

## 5. Algorithm

1. Start the program.
2. Display the program title.
3. Get the student name, email address, and student ID.
4. Check whether the student name is empty.
5. Remove unnecessary spaces from the email address.
6. Check whether the email contains exactly one @ symbol.
7. Check whether the email contains a dot after the @ symbol.
8. Check whether the email contains spaces or ends with a dot.
9. Check whether the student ID starts with "STU".
10. Check whether the student ID has exactly 8 characters.
11. Check whether the last five characters are digits.
12. Display the individual validation results.
13. If all conditions are satisfied, display "Student Details: VALID".
14. Otherwise, display "Student Details: INVALID".
15. Stop the program.

## 6. Flowchart

```text
             START
               |
               v
       Enter Student Details
               |
               v
       Validate Student Name
               |
               v
       Validate Email Address
               |
               v
       Validate Student ID
               |
               v
       Display Validation Results
               |
               v
       Are All Conditions Passed?
           /           \
         YES            NO
          |              |
          v              v
       Display         Display
        VALID          INVALID
          |              |
          v              v
                STOP
```

## 7. Pseudocode

```text
START

DISPLAY program title

INPUT student name
INPUT email address
INPUT student ID

CHECK whether student name is empty

CHECK email address:
    Exactly one @ symbol
    @ symbol is not at the beginning
    Dot exists after @
    No spaces
    Does not end with a dot

CHECK student ID:
    Starts with "STU"
    Contains exactly 8 characters
    Last five characters are digits

DISPLAY individual validation results

IF all conditions are satisfied THEN
    DISPLAY "Student Details: VALID"
ELSE
    DISPLAY "Student Details: INVALID"
END IF

STOP
```

## 8. Python Source Code

```python
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
```

## 9. Test Cases

| Student Name | Email Address | Student ID | Expected Result |
|---|---|---|---|
| Rahul | rahul@gmail.com | STU12345 | VALID |
| Rahul | rahulgmail.com | STU12345 | INVALID |
| Rahul | rahul@gmail.com | STU12AB5 | INVALID |
| Empty | rahul@gmail.com | STU12345 | INVALID |
| Rahul | rahul@gmail.com | STU1234 | INVALID |
| Rahul | rahul @gmail.com | STU12345 | INVALID |

## 10. Sample Output

### Valid Student Details

```text
STUDENT EMAIL AND IDENTIFIER VALIDATION
----------------------------------------
Enter student name: Rahul
Enter student email: rahul@gmail.com
Enter student ID: STU12345

VALIDATION RESULTS
------------------
Student Name: Passed
Email Address: Passed
Student ID: Passed

Student Details: VALID

Validation Completed!
```

### Invalid Student Details

```text
STUDENT EMAIL AND IDENTIFIER VALIDATION
----------------------------------------
Enter student name: Rahul
Enter student email: rahulgmail.com
Enter student ID: STU12AB5

VALIDATION RESULTS
------------------
Student Name: Passed
Email Address: Failed
Student ID: Failed

Student Details: INVALID

Validation Completed!
```

## 11. Output Screenshots

Screenshots of the program execution are saved in the screenshots folder.

The folder contains:
- Valid student details output.
- Invalid student details output.

## 12. Conclusion

This project demonstrates how Python can be used to validate student information using strings, conditional statements, logical operators, and string methods. It checks student names, email addresses, and student identifiers based on predefined rules. This activity improved my understanding of Python programming, string manipulation, and logical problem-solving.

## 13. Author

**Name:** Pravallika

**Course:** B.Tech - First Year

**Programming Language:** Python

**Case Study Number:** 30
