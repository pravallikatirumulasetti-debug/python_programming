
# Case Study 27 – Advanced Numeric Pattern Generator

## 1. Problem Statement
Develop a Python program to generate a hollow diamond pattern based on the number of rows entered by the user. The program uses loops and conditional statements to create a properly aligned pattern and validates invalid dimensions.

## 2. Objectives
- To understand nested loops in Python.
- To generate a hollow diamond pattern.
- To use conditional statements.
- To accept input from the user.
- To validate invalid dimensions.
- To improve logical and problem-solving skills.

## 3. Technologies Used
- Python
- Visual Studio Code

## 4. How to Run
1. Open the project folder in VS Code.
2. Open `case27.py`.
3. Run the Python program.
4. Enter the number of rows.

## 5. Expected Output
The program displays a hollow diamond pattern based on the user's input.

## 6. Author
Pravallika

## 7. Conclusion
This project helps understand nested loops, conditional statements, user input, and input validation in Python.
## 3. Assumptions
- The user enters an integer value.
- The number of rows must be positive.
- The program generates a hollow diamond using stars.
- The pattern is symmetrical.
- Zero and negative values are considered invalid.
## 4. Algorithm
1. Start the program.
2. Display the program title.
3. Read the number of rows from the user.
4. Check whether the entered number is positive.
5. If the number is invalid, display an error message.
6. Otherwise, generate the upper half of the hollow diamond using nested loops.
7. Generate the lower half using reverse loops.
8. Display the complete hollow diamond.
9. Stop the program.
## 5. Flowchart

Start
  |
  v
Display Program Title
  |
  v
Enter Number of Rows
  |
  v
Is rows > 0?
  |
  +---- No ----> Display Invalid Input
  |                       |
  |                       v
  |                      Stop
  |
  Yes
  |
  v
Generate Upper Half
  |
  v
Generate Lower Half
  |
  v
Display Hollow Diamond
  |
  v
Stop
## 6. Pseudocode

BEGIN

    DISPLAY program title

    INPUT rows

    IF rows <= 0 THEN
        DISPLAY "Invalid input"

    ELSE
        FOR i = 1 TO rows
            PRINT spaces
            PRINT hollow upper pattern
        END FOR

        FOR i = rows-1 DOWN TO 1
            PRINT spaces
            PRINT hollow lower pattern
        END FOR

    END IF

END
## 7. Test Cases

| Test Case | Input | Expected Output |
|---|---|---|
| 1 | 5 | Hollow diamond with 5 rows in upper half |
| 2 | 3 | Hollow diamond with 3 rows in upper half |
| 3 | 1 | Single star |
| 4 | 0 | Invalid input message |
| 5 | -2 | Invalid input message |