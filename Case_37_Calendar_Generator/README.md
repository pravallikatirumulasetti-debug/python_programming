
# Case 37 – Nested Loop Calendar Generator

## 1. Problem Statement

The aim of this project is to generate a formatted monthly calendar using the starting weekday and the total number of days in a month.

The program arranges dates correctly into weeks using nested loops and displays a properly aligned calendar.

## 2. Objectives

- To understand nested loops in Python.
- To generate a monthly calendar.
- To use conditional statements for input validation.
- To understand lists and list operations.
- To arrange dates according to weekdays.
- To display formatted output.

## 3. Assumptions

- The starting weekday is entered as a number from 0 to 6.
- Sunday is represented by 0.
- Monday is represented by 1.
- Tuesday is represented by 2.
- Wednesday is represented by 3.
- Thursday is represented by 4.
- Friday is represented by 5.
- Saturday is represented by 6.
- The number of days must be between 28 and 31.
- The program generates a calendar based on the supplied inputs.
- The user is responsible for entering the correct starting weekday and month length.

## 4. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code

## 5. Algorithm

1. Start the program.
2. Display weekday numbers.
3. Read the starting weekday from the user.
4. Read the total number of days in the month.
5. Validate the inputs.
6. If the starting weekday is outside 0 to 6, display an error message.
7. If the number of days is outside 28 to 31, display an error message.
8. Otherwise, create a list containing weekday names.
9. Display the weekday headings.
10. Calculate the number of required weeks.
11. Initialize the current date to 1.
12. Use an outer loop to represent weeks.
13. Use an inner loop to represent weekdays.
14. Calculate the position of each calendar cell.
15. Display blank spaces before the first date and after the final date.
16. Display the dates in their correct positions.
17. Display a success message.
18. Stop the program.

## 6. Flowchart

```text
             START
               |
       Display Weekday Numbers
               |
        Input Starting Day
               |
         Input Total Days
               |
         Validate Inputs
               |
          Are Inputs Valid?
            /       \
          No         Yes
          |           |
     Display Error  Create Weekday List
          |           |
          |       Display Headings
          |           |
          |      Calculate Weeks
          |           |
          |       Outer Loop
          |           |
          |       Inner Loop
          |           |
          |     Calculate Position
          |           |
          |      Display Date
          |           |
          |      More Cells?
          |           |
          |      Display New Line
          |           |
          |     Display Success
          |           |
          +-----------+
                |
               END
```

## 7. Pseudocode

```text
START

DISPLAY weekday numbers

INPUT start_day
INPUT total_days

IF start_day is invalid:
    DISPLAY error message

ELSE IF total_days is invalid:
    DISPLAY error message

ELSE:
    CREATE weekday list

    DISPLAY weekday headings

    CALCULATE total weeks

    SET current_date = 1

    FOR each week:
        FOR each weekday:

            CALCULATE position

            IF position is before starting day
               OR current_date exceeds total days:
                DISPLAY blank space

            ELSE:
                DISPLAY current_date
                INCREASE current_date

        MOVE to next line

    DISPLAY success message

STOP
```

## 8. Source Code

The Python implementation is available in:

`case37.py`

## 9. Test Cases

| Test Case | Starting Day | Total Days | Expected Result |
|---|---:|---:|---|
| 1 | 3 | 30 | Calendar starts on Wednesday |
| 2 | 0 | 31 | Calendar starts on Sunday |
| 3 | 1 | 28 | Calendar starts on Monday |
| 4 | 7 | 30 | Invalid weekday |
| 5 | 2 | 35 | Invalid number of days |

## 10. Sample Input and Output

### Test Case 1

**Input:**

```text
Starting weekday: 3
Number of days: 30
```

**Output:**

```text
Sun  Mon  Tue  Wed  Thu  Fri  Sat
              1    2    3    4
  5    6    7    8    9   10   11
 12   13   14   15   16   17   18
 19   20   21   22   23   24   25
 26   27   28   29   30
```

### Test Case 2

**Input:**

```text
Starting weekday: 7
Number of days: 30
```

**Output:**

```text
Invalid weekday! Enter a number from 0 to 6.
```

## 11. Screenshots

The program output screenshots are stored in the `screenshots` folder.

## 12. Conclusion

This project demonstrates the generation of a monthly calendar using Python nested loops.

It helps understand loops, conditional statements, lists, input validation, and formatted output.

The program successfully arranges dates according to the supplied starting weekday and number of days.
