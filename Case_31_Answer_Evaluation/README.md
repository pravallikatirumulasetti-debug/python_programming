
# Case Study 31 – String-Based Examination Answer Evaluation

## 1. Problem Statement

Develop a Python program to evaluate students' examination answers by comparing their answer strings with a given answer key. The program calculates correct, incorrect, and unanswered responses, applies negative marking, and displays student-wise results.

## 2. Objectives

- To compare student answers with the answer key.
- To identify correct, incorrect, and unanswered questions.
- To apply negative marking for incorrect answers.
- To calculate the final score of each student.
- To display student-wise examination results.
- To understand strings, loops, lists, tuples, and conditional statements in Python.

## 3. Assumptions

- The answer key contains only A, B, C, and D.
- Students can enter A, B, C, D, or - for unanswered questions.
- Each correct answer carries 1 mark.
- Each incorrect answer carries a negative mark of 0.25.
- Unanswered questions carry 0 marks.
- Every student must provide the same number of answers as the answer key.

## 4. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Concepts: Strings, Lists, Tuples, Loops, Conditional Statements, and Operators

## 5. Algorithm

1. Start the program.
2. Enter the answer key.
3. Validate the answer key.
4. Calculate the total number of questions.
5. Enter the number of students.
6. For each student:
   - Enter the student's name.
   - Enter the student's answers.
   - Validate the answers.
   - Compare each answer with the answer key.
   - Count correct, incorrect, and unanswered responses.
   - Calculate the final score using negative marking.
   - Store the result in a tuple.
7. Display the results of all students.
8. Stop the program.

## 6. Flowchart

```text
       START
         |
         v
   Enter Answer Key
         |
         v
   Validate Answer Key
         |
         v
   Enter Number of Students
         |
         v
   Enter Student Details
         |
         v
   Enter Student Answers
         |
         v
   Compare with Answer Key
         |
         v
   Count Correct, Incorrect
   and Unanswered Answers
         |
         v
   Calculate Final Score
         |
         v
   Store Student Result
         |
         v
   More Students?
      /       \
    Yes        No
     |          |
     v          v
 Repeat     Display Results
                |
                v
               STOP
```

## 7. Pseudocode

```text
START

INPUT answer_key
total_questions = LENGTH(answer_key)

SET correct_mark = 1
SET negative_mark = 0.25

INPUT student_count
CREATE empty results list

FOR each student:

    INPUT student_name
    INPUT student_answers

    SET correct = 0
    SET incorrect = 0
    SET unanswered = 0

    FOR each question:

        IF answer is "-":
            unanswered = unanswered + 1

        ELSE IF answer matches answer_key:
            correct = correct + 1

        ELSE:
            incorrect = incorrect + 1

    END FOR

    score = (correct * correct_mark)
            - (incorrect * negative_mark)

    STORE student result in a tuple
    ADD tuple to results list

END FOR

DISPLAY all student results

STOP
```

## 8. Python Source Code

The complete source code is available in `case31.py`.

## 9. Test Cases

| Test Case | Answer Key | Student Answers | Expected Result |
|---|---|---|---|
| 1 | ABCDAB | ABCDAB | 6 correct, 0 incorrect, 0 unanswered |
| 2 | ABCDAB | AB-DXB | 4 correct, 1 incorrect, 1 unanswered |
| 3 | ABCDAB | DDDDAB | 3 correct, 3 incorrect, 0 unanswered |
| 4 | ABCDAB | ------ | 0 correct, 0 incorrect, 6 unanswered |

## 10. Sample Input

```text
Enter the answer key (A, B, C, D): ABCDAB
Enter number of students: 2

Student 1
Enter student name: Rahul
Enter answers: ABCDAB

Student 2
Enter student name: Priya
Enter answers: AB-DXB
```

## 11. Sample Output

```text
EXAMINATION RESULT REPORT
-------------------------

Student Name: Rahul
Correct Answers: 6
Incorrect Answers: 0
Unanswered Questions: 0
Final Score: 6.0 / 6
Result: Positive Score

Student Name: Priya
Correct Answers: 4
Incorrect Answers: 1
Unanswered Questions: 1
Final Score: 3.75 / 6
Result: Positive Score

Evaluation Completed!
```

## 12. Screenshots

The screenshots of the program execution are saved in the `screenshots` folder.

## 13. Conclusion

This project successfully evaluates student examination answers using Python. It compares answer strings, calculates correct, incorrect, and unanswered responses, and applies negative marking to calculate final scores.

Through this project, we learned how to use strings, lists, tuples, loops, and conditional statements to solve a real-world examination evaluation problem.

## 14. Author

**Name:** Pravallika  
**Project:** Python Activity-Based Learning  
**Case Study:** 31 – String-Based Examination Answer Evaluation
