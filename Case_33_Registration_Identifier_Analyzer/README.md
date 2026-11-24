
# Case 33 – Campus Registration Identifier Analyzer

## 1. Problem Statement

Examine student identification strings, validate their structure, extract specified components, and classify records according to branch and admission year codes.

## 2. Objectives

- To accept student registration IDs.
- To validate the structure of registration IDs.
- To extract admission year, branch code, and student number.
- To classify valid and invalid student records.
- To display a summary of registration records.

## 3. Assumptions

The following registration ID format is assumed for this project:

`YYYY-BR-NNN`

Where:
- YYYY represents the four-digit admission year.
- BR represents the branch code.
- NNN represents the three-digit student number.

Accepted branch codes:
- CSE
- AIML
- ECE
- EEE
- MECH

The admission year must be between 2000 and 2099.

## 4. Technologies Used

- Programming Language: Python
- Editor: Visual Studio Code
- Concepts: Strings, Lists, Tuples, Conditional Statements, Loops

## 5. Algorithm

1. Start the program.
2. Read the number of student records.
3. Create two empty lists for valid and invalid records.
4. Accept a registration ID for each student.
5. Split the ID using the hyphen separator.
6. Check whether the ID contains exactly three components.
7. Extract the admission year, branch code, and student number.
8. Validate the admission year.
9. Validate the branch code.
10. Validate the student number.
11. If all conditions are satisfied, store the record in the valid list.
12. Otherwise, store it in the invalid list.
13. Display all valid and invalid records.
14. Display the total number of records.
15. Stop the program.

## 6. Flowchart

```text
        START
          |
          v
  Enter number of records
          |
          v
   Accept Registration ID
          |
          v
    Split the ID into
       3 components
          |
          v
    Validate year,
    branch and number
          |
          v
     Are all valid?
       /       \
     Yes        No
      |          |
      v          v
 Store in     Store in
 valid list   invalid list
      |          |
      +----+-----+
           |
           v
   More records?
      /      \
    Yes       No
     |         |
     v         v
  Repeat    Display Summary
                |
                v
               STOP
```

## 7. Pseudocode

```text
BEGIN

INPUT number of records

CREATE valid_records list
CREATE invalid_records list

FOR each student

    INPUT registration ID
    SPLIT ID using "-"

    IF number of components is not 3
        ADD ID to invalid_records
        CONTINUE
    END IF

    EXTRACT year, branch, number

    VALIDATE year
    VALIDATE branch
    VALIDATE student number

    IF all components are valid
        STORE record in valid_records
        DISPLAY extracted details
    ELSE
        STORE ID in invalid_records
        DISPLAY error messages
    END IF

END FOR

DISPLAY valid records
DISPLAY invalid records
DISPLAY summary

END
```

## 8. Python Source Code

The complete Python program is available in `case33.py`.

## 9. Test Cases

| Test Input | Expected Result | Reason |
|---|---|---|
| 2026-CSE-101 | Valid | All components are correct |
| 2026-AIML-102 | Valid | Accepted branch code |
| 2026-XYZ-103 | Invalid | Invalid branch code |
| 25-CSE-101 | Invalid | Incorrect year format |
| 2026-CSE-AB1 | Invalid | Student number is not numeric |
| 2026-CSE | Invalid | Missing component |

## 10. Sample Input

```text
Enter number of student records: 3

Student 1
Enter registration ID: 2026-CSE-101

Student 2
Enter registration ID: 2026-AIML-102

Student 3
Enter registration ID: 2026-XYZ-103
```

## 11. Sample Output

```text
CAMPUS REGISTRATION IDENTIFIER ANALYZER
----------------------------------------

Registration ID: VALID
Admission Year: 2026
Branch: CSE
Student Number: 101

Registration ID: VALID
Admission Year: 2026
Branch: AIML
Student Number: 102

Registration ID: INVALID
Error: Invalid branch code.

========== REGISTRATION SUMMARY ==========

Total Records: 3
Valid Records: 2
Invalid Records: 1

Registration Analysis Completed!
```

## 12. Screenshots

The screenshots of the program execution are stored in the `screenshots` folder.

## 13. Conclusion

The Campus Registration Identifier Analyzer successfully validates student registration IDs and extracts important information such as admission year, branch code, and student number.

This project helped me understand string operations, lists, tuples, loops, and conditional statements in Python.

---

**Project:** Python Activity-Based Learning  
**Case Number:** 33  
**Case Name:** Campus Registration Identifier Analyzer  
**Language:** Python
