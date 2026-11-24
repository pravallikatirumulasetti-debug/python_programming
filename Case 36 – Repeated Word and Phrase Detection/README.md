
# Case 36 – Repeated Word and Phrase Detection

## 1. Problem Statement

The aim of this project is to process a paragraph, convert all words into lowercase, count word occurrences, and identify repeated words along with their positions.

The program generates a report showing repeated words, their occurrence counts, and their positions in the paragraph.

## 2. Objectives

- To understand string manipulation in Python.
- To convert text into lowercase.
- To split a paragraph into individual words.
- To count repeated word occurrences.
- To identify the positions of repeated words.
- To use lists, loops, and conditional statements.

## 3. Assumptions

- The user enters a paragraph as input.
- Uppercase and lowercase versions of a word are treated equally.
- Common punctuation marks such as commas, periods, and question marks are removed.
- Word positions start from 1.
- Words are separated by spaces.
- The program identifies repeated individual words.

## 4. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code

## 5. Algorithm

1. Start the program.
2. Read a paragraph from the user.
3. Convert the paragraph into lowercase.
4. Remove common punctuation marks.
5. Split the paragraph into individual words.
6. Create an empty list to store unique words.
7. Traverse each word in the paragraph.
8. Add the word to the unique words list if it is not already present.
9. Traverse the unique words list.
10. Count the occurrences of each word.
11. If a word occurs more than once, identify its positions.
12. Display the repeated word, occurrence count, and positions.
13. Display the total number of words, unique words, and repeated words.
14. Stop the program.

## 6. Flowchart

```text
             START
               |
         Input Paragraph
               |
        Convert to Lowercase
               |
       Remove Punctuation
               |
         Split into Words
               |
       Create Unique Word List
               |
       Traverse Unique Words
               |
       Count Word Occurrences
               |
        Is Count Greater Than 1?
             /       \
           Yes        No
            |          |
      Find Positions   Skip
            |
      Display Word Details
            |
       More Words Left?
          /       \
        Yes        No
         |          |
      Repeat    Display Summary
                    |
                   END
```

## 7. Pseudocode

```text
START

INPUT paragraph

CONVERT paragraph to lowercase

REMOVE common punctuation marks

SPLIT paragraph into words

CREATE empty unique_words list

FOR each word in words:
    IF word is not in unique_words:
        ADD word to unique_words

INITIALIZE repeated_words = 0

FOR each word in unique_words:
    COUNT occurrences of word

    IF count > 1:
        INCREASE repeated_words

        CREATE empty positions list

        FOR each position in words:
            IF word matches current word:
                ADD position to positions

        DISPLAY word
        DISPLAY occurrence count
        DISPLAY positions

DISPLAY total words
DISPLAY unique words
DISPLAY repeated words

STOP
```

## 8. Source Code

The Python implementation is available in:

`case36.py`

## 9. Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| 1 | Python is easy and Python is interesting. | python and is are repeated |
| 2 | Hello world | No repeated words |
| 3 | Apple apple APPLE | apple occurs 3 times |
| 4 | Good good morning morning | good and morning are repeated |

## 10. Sample Input and Output

### Test Case 1

**Input:**

```text
Python is easy and Python is interesting.
```

**Output:**

```text
WORD OCCURRENCE REPORT

Word: python
Occurrences: 2
Positions: [1, 5]

Word: is
Occurrences: 2
Positions: [2, 6]

========== SUMMARY ==========
Total Words: 7
Unique Words: 5
Repeated Words: 2

Word Analysis Completed!
```

### Test Case 2

**Input:**

```text
Hello world
```

**Expected Output:**

```text
Total Words: 2
Unique Words: 2
Repeated Words: 0
No repeated words found.
```

## 11. Screenshots

The output screenshots of the program are stored in the `screenshots` folder.

## 12. Conclusion

This project demonstrates how to analyse a paragraph using Python string operations and lists.

It helps understand lowercase conversion, word splitting, counting occurrences, list operations, loops, and conditional statements.

The program successfully identifies repeated words and displays their positions in the paragraph.
