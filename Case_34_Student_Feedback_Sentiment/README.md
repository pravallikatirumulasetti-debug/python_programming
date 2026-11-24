
# Case 34 – Student Feedback Sentiment Scoring

## 1. Problem Statement

Analyse multiple feedback sentences using a supplied keyword list, count positive and negative indicators, calculate scores, and classify feedback using predefined thresholds.

## 2. Objectives

- To accept multiple feedback sentences from users.
- To identify positive and negative keywords.
- To count positive and negative indicators.
- To calculate sentiment scores.
- To classify feedback as Positive, Negative, or Neutral.
- To generate a final feedback summary.

## 3. Assumptions

- Feedback is entered as text sentences.
- Positive and negative keywords are predefined.
- The program ignores uppercase and lowercase differences.
- Each matching keyword contributes one point.
- Sentiment score is calculated by subtracting negative indicators from positive indicators.
- A positive score indicates Positive feedback.
- A negative score indicates Negative feedback.
- A zero score indicates Neutral feedback.

## 4. Technologies Used

- Programming Language: Python
- Editor: Visual Studio Code
- Concepts:
  - Strings
  - Lists
  - Loops
  - Conditional Statements
  - String Operations

## 5. Algorithm

1. Start the program.
2. Create lists containing positive and negative keywords.
3. Accept the number of feedback sentences.
4. Initialize positive, negative, and neutral feedback counters.
5. Accept a feedback sentence.
6. Convert the sentence into lowercase.
7. Split the sentence into individual words.
8. Compare each word with the positive and negative keyword lists.
9. Count positive and negative indicators.
10. Calculate the sentiment score.
11. Classify the feedback based on its score.
12. Repeat the process for all feedback sentences.
13. Display the total positive, negative, and neutral feedback.
14. Stop the program.

## 6. Flowchart

```text
             START
               |
               v
       Define keyword lists
               |
               v
     Enter number of feedbacks
               |
               v
       Accept feedback sentence
               |
               v
       Convert to lowercase
               |
               v
       Split into individual words
               |
               v
      Count positive and negative
             keywords
               |
               v
       Calculate sentiment score
               |
               v
         Is score positive?
          /           \
        Yes            No
         |              |
         v              v
      POSITIVE     Is score negative?
                    /          \
                  Yes           No
                   |             |
                   v             v
                NEGATIVE       NEUTRAL
                   \             /
                    \           /
                     v         v
                  More feedback?
                    /       \
                  Yes        No
                   |          |
                   v          v
                 Repeat    Display Summary
                                |
                                v
                               STOP
```

## 7. Pseudocode

```text
BEGIN

CREATE positive keyword list
CREATE negative keyword list

INPUT number of feedback sentences

INITIALIZE positive, negative, neutral counters

FOR each feedback sentence

    INPUT feedback
    CONVERT feedback to lowercase
    SPLIT feedback into words

    SET positive_count = 0
    SET negative_count = 0

    FOR each word

        IF word is in positive list
            INCREMENT positive_count
        END IF

        IF word is in negative list
            INCREMENT negative_count
        END IF

    END FOR

    CALCULATE score
    score = positive_count - negative_count

    IF score > 0
        CLASSIFY as POSITIVE
    ELSE IF score < 0
        CLASSIFY as NEGATIVE
    ELSE
        CLASSIFY as NEUTRAL
    END IF

END FOR

DISPLAY feedback summary

END
```

## 8. Python Source Code

The complete Python program is available in `case34.py`.

## 9. Test Cases

| Feedback Input | Expected Score | Expected Result |
|---|---:|---|
| Excellent and helpful | 2 | Positive |
| Boring and confusing | -2 | Negative |
| Class is okay | 0 | Neutral |
| Good and amazing | 2 | Positive |
| Poor and worst | -2 | Negative |

## 10. Sample Input

```text
Enter number of feedback sentences: 3

Feedback 1
Enter your feedback: The teaching is excellent and helpful.

Feedback 2
Enter your feedback: The class is boring and confusing.

Feedback 3
Enter your feedback: The class is okay.
```

## 11. Sample Output

```text
STUDENT FEEDBACK SENTIMENT SCORING
-----------------------------------

Positive Indicators: 2
Negative Indicators: 0
Sentiment Score: 2
Feedback Category: POSITIVE

Positive Indicators: 0
Negative Indicators: 2
Sentiment Score: -2
Feedback Category: NEGATIVE

Positive Indicators: 0
Negative Indicators: 0
Sentiment Score: 0
Feedback Category: NEUTRAL

========== FEEDBACK SUMMARY ==========

Total Feedback: 3
Positive Feedback: 1
Negative Feedback: 1
Neutral Feedback: 1

Feedback Analysis Completed!
```

## 12. Screenshots

The screenshots of the program execution are stored in the `screenshots` folder.

## 13. Conclusion

The Student Feedback Sentiment Scoring program successfully analyses feedback sentences using predefined positive and negative keywords.

It calculates sentiment scores and classifies feedback into Positive, Negative, and Neutral categories.

This project helped me understand strings, lists, loops, conditional statements, and basic text analysis using Python.

---

**Project:** Python Activity-Based Learning  
**Case Number:** 34  
**Case Name:** Student Feedback Sentiment Scoring  
**Language:** Python
