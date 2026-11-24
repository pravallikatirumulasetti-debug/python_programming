
print("STRING-BASED EXAMINATION ANSWER EVALUATION")
print("-------------------------------------------")

# Get the answer key
answer_key = input("Enter the answer key (A, B, C, D): ").upper().strip()

# Validate answer key
while len(answer_key) == 0 or not all(ch in "ABCD" for ch in answer_key):
    print("Invalid answer key! Use only A, B, C, D.")
    answer_key = input("Enter the answer key again: ").upper().strip()

total_questions = len(answer_key)

# Marking rules
correct_mark = 1
negative_mark = 0.25

# Get number of students
student_count = int(input("Enter number of students: "))

results = []

# Evaluate each student
for i in range(student_count):

    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    answers = input(
        "Enter answers (use A, B, C, D or - for unanswered): "
    ).upper().strip()

    # Validate answer length and characters
    while (len(answers) != total_questions
           or not all(ch in "ABCD-" for ch in answers)):
        print("Invalid answers! Check the number of answers and characters.")
        answers = input("Enter answers again: ").upper().strip()

    correct = 0
    incorrect = 0
    unanswered = 0

    # Compare student answers with answer key
    for j in range(total_questions):

        if answers[j] == "-":
            unanswered += 1

        elif answers[j] == answer_key[j]:
            correct += 1

        else:
            incorrect += 1

    # Calculate final score
    score = (correct * correct_mark) - (incorrect * negative_mark)

    # Store student result as a tuple
    result = (name, correct, incorrect, unanswered, score)
    results.append(result)

# Display final report
print("\nEXAMINATION RESULT REPORT")
print("-------------------------")

for result in results:

    name, correct, incorrect, unanswered, score = result

    print("\nStudent Name:", name)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Unanswered Questions:", unanswered)
    print("Final Score:", round(score, 2), "/", total_questions)

    if score >= 0:
        print("Result: Positive Score")
    else:
        print("Result: Negative Score")

print("\nEvaluation Completed!")
