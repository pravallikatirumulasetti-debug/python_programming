
# Case Study 29: Password Policy Validation Engine

## 1. Problem Statement

Develop a Python program that evaluates sample passwords based on predefined password policy rules. The program checks minimum length, uppercase letters, lowercase letters, digits, special characters, repeated characters, and prohibited words. It displays the result of each condition and determines whether the password is VALID or INVALID.

## 2. Objectives

- To understand string operations in Python.
- To use conditional statements and loops.
- To check uppercase and lowercase letters.
- To identify digits and special characters.
- To validate minimum password length.
- To detect repeated consecutive characters.
- To identify prohibited words.
- To display clear validation results.

## 3. Assumptions

- The user enters a sample password as a string.
- The minimum password length is 8 characters.
- At least one uppercase letter is required.
- At least one lowercase letter is required.
- At least one digit is required.
- At least one special character is required.
- Three or more identical consecutive characters are not allowed.
- The word "password" is prohibited, regardless of letter case.
- This is an educational password validation program, not a real authentication system.

## 4. Technologies Used

- Programming Language: Python
- Code Editor: Visual Studio Code
- Concepts: Variables, Strings, Loops, Conditional Statements and Operators.

## 5. Algorithm

1. Start the program.
2. Display the program title.
3. Get a sample password from the user.
4. Check whether the password contains at least 8 characters.
5. Check for uppercase letters.
6. Check for lowercase letters.
7. Check for digits.
8. Check for special characters.
9. Check for three consecutive identical characters.
10. Check whether the password contains the prohibited word "password".
11. Display the result of each validation condition.
12. If all conditions are satisfied, display "VALID".
13. Otherwise, display "INVALID".
14. Stop the program.

## 6. Flowchart

```text
        START
          |
          v
    Enter Password
          |
          v
    Check Password Rules
          |
          v
    Check All Conditions
          |
          v
     Are All Rules Passed?
        /          \
      YES           NO
       |             |
       v             v
  Display VALID  Display INVALID
       |             |
       v             v
        STOP
```

## 7. Pseudocode

```text
START

DISPLAY program title
INPUT sample password

CHECK minimum length
CHECK uppercase letter
CHECK lowercase letter
CHECK digit
CHECK special character
CHECK repeated consecutive characters
CHECK prohibited word

DISPLAY individual validation results

IF all conditions are satisfied THEN
    DISPLAY "Password Status: VALID"
ELSE
    DISPLAY "Password Status: INVALID"
END IF

STOP
```

## 8. Python Source Code

```python
print("PASSWORD POLICY VALIDATION ENGINE")
print("---------------------------------")

sample = input("Enter a sample password to check: ")

print("\nChecking password policy...")

# Check minimum length
length_valid = len(sample) >= 8

# Check character categories
uppercase = False
lowercase = False
digit = False
special = False

for ch in sample:
    if ch.isupper():
        uppercase = True
    elif ch.islower():
        lowercase = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

# Check repeated characters
repeated = False

for i in range(len(sample) - 2):
    if sample[i] == sample[i + 1] == sample[i + 2]:
        repeated = True

# Check prohibited word
prohibited = "password" in sample.lower()

# Display individual results
print("Minimum length:", "Passed" if length_valid else "Failed")
print("Uppercase letter:", "Passed" if uppercase else "Failed")
print("Lowercase letter:", "Passed" if lowercase else "Failed")
print("Digit:", "Passed" if digit else "Failed")
print("Special character:", "Passed" if special else "Failed")
print("Repeated characters:", "Failed" if repeated else "Passed")
print("Prohibited word:", "Failed" if prohibited else "Passed")

# Final result
if (length_valid and uppercase and lowercase and digit
        and special and not repeated and not prohibited):
    print("\nPassword Status: VALID")
else:
    print("\nPassword Status: INVALID")
```

## 9. Test Cases

| Test Input | Expected Result | Reason |
|---|---|---|
| Hello123@ | VALID | All conditions passed |
| hello123@ | INVALID | Uppercase missing |
| HELLO123@ | INVALID | Lowercase missing |
| Hello@@@@ | INVALID | Repeated characters |
| Abc111@xy | INVALID | Repeated digits |
| password123@A | INVALID | Prohibited word |
| Hi1@ | INVALID | Minimum length not satisfied |

## 10. Sample Output

### Valid Password

```text
PASSWORD POLICY VALIDATION ENGINE
---------------------------------
Enter a sample password to check: Hello123@

Checking password policy...
Minimum length: Passed
Uppercase letter: Passed
Lowercase letter: Passed
Digit: Passed
Special character: Passed
Repeated characters: Passed
Prohibited word: Passed

Password Status: VALID
```

### Invalid Password

```text
PASSWORD POLICY VALIDATION ENGINE
---------------------------------
Enter a sample password to check: hello123@

Checking password policy...
Minimum length: Passed
Uppercase letter: Failed
Lowercase letter: Passed
Digit: Passed
Special character: Passed
Repeated characters: Passed
Prohibited word: Passed

Password Status: INVALID
```

## 11. Output Screenshots

Screenshots of the program execution are saved in the `screenshots` folder.

## 12. Conclusion

This project demonstrates how Python can be used to validate sample passwords using strings, loops, conditional statements, and logical operators. It checks multiple password policy conditions and displays whether the entered sample password is valid or invalid. This activity improved my understanding of Python programming and logical problem-solving.

## 13. Author

**Name:** Pravallika  
**Course:** B.Tech - First Year  
**Programming Language:** Python  
**Case Study Number:** 29
