
print("STUDENT FEEDBACK SENTIMENT SCORING")
print("-----------------------------------")

# Define positive and negative keywords
positive_words = [
    "good", "excellent", "helpful", "great",
    "amazing", "interesting", "clear", "nice"
]

negative_words = [
    "bad", "boring", "poor", "confusing",
    "difficult", "slow", "worst", "unclear"
]

# Get number of feedback sentences
count = int(input("Enter number of feedback sentences: "))

positive_feedback = 0
negative_feedback = 0
neutral_feedback = 0

# Process each feedback sentence
for i in range(count):

    print("\nFeedback", i + 1)

    feedback = input("Enter your feedback: ").lower()

    positive_count = 0
    negative_count = 0

    # Count positive and negative keywords
    words = feedback.split()

    for word in words:

        word = word.strip(".,!?;:")

        if word in positive_words:
            positive_count += 1

        if word in negative_words:
            negative_count += 1

    # Calculate sentiment score
    score = positive_count - negative_count

    print("\nPositive Indicators:", positive_count)
    print("Negative Indicators:", negative_count)
    print("Sentiment Score:", score)

    # Classify feedback
    if score > 0:
        print("Feedback Category: POSITIVE")
        positive_feedback += 1

    elif score < 0:
        print("Feedback Category: NEGATIVE")
        negative_feedback += 1

    else:
        print("Feedback Category: NEUTRAL")
        neutral_feedback += 1

# Display final summary
print("\n========== FEEDBACK SUMMARY ==========")

print("Total Feedback:", count)
print("Positive Feedback:", positive_feedback)
print("Negative Feedback:", negative_feedback)
print("Neutral Feedback:", neutral_feedback)

print("\nFeedback Analysis Completed!")
