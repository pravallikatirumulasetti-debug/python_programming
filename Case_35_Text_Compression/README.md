
# Case 35 – Text Compression Using Character Runs

## 1. Problem Statement

The aim of this project is to compress a given text string by grouping consecutive repeated characters and representing each group with the character followed by its count.

The program compares the original string length with the compressed string length and determines whether compression is beneficial.

## 2. Objectives

- To understand string manipulation in Python.
- To identify consecutive repeated characters.
- To use loops and conditional statements.
- To generate a compressed string using character counts.
- To compare original and compressed string lengths.

## 3. Assumptions

- The input is a text string.
- Consecutive repeated characters are grouped together.
- Each character is followed by its repetition count.
- The program is case-sensitive.
- If the input is empty, the program displays a message.
- Compression is beneficial only when the compressed string is shorter than the original string.

## 4. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code

## 5. Algorithm

1. Start the program.
2. Read a text string from the user.
3. Check whether the string is empty.
4. If empty, display a message.
5. Otherwise, initialize an empty compressed string and set the count to 1.
6. Traverse the string character by character.
7. If the current character matches the previous character, increase the count.
8. Otherwise, add the previous character and its count to the compressed string.
9. Reset the count to 1.
10. Add the final character group to the compressed string.
11. Calculate the original and compressed string lengths.
12. Compare both lengths.
13. Display whether compression is beneficial.
14. Stop the program.

## 6. Flowchart

```text
          START
            |
       Input String
            |
       Is String Empty?
         /       \
       Yes        No
       |           |
 Display Message  Initialize
       |          Variables
       |             |
       |       Process Characters
       |             |
       |       Same as Previous?
       |          /       \
       |        Yes        No
       |         |          |
       |    Increase     Append Character
       |      Count       and Count
       |         |          |
       |         +----------+
       |             |
       |       Append Final Group
       |             |
       |       Compare Lengths
       |             |
       |       Display Result
       |             |
       +-------------+
             |
            END
```

## 7. Pseudocode

```text
START

INPUT text

IF text is empty:
    DISPLAY "Please enter a non-empty string"
ELSE:
    compressed = ""
    count = 1

    FOR each character from index 1:
        IF current character equals previous character:
            count = count + 1
        ELSE:
            ADD previous character and count to compressed
            count = 1

    ADD final character and count to compressed

    original_length = length of text
    compressed_length = length of compressed

    DISPLAY original text
    DISPLAY compressed text
    DISPLAY both lengths

    IF compressed_length < original_length:
        DISPLAY "Compression is beneficial"
    ELSE:
        DISPLAY "Compression is not beneficial"

END IF

STOP
```

## 8. Source Code

The Python implementation is available in:

`case35.py`

## 9. Test Cases

| Test Case | Input | Expected Compressed Text | Result |
|---|---|---|---|
| 1 | `aaabb` | `a3b2` | Beneficial |
| 2 | `abc` | `a1b1c1` | Not Beneficial |
| 3 | `aaaaaabbbb` | `a6b4` | Beneficial |
| 4 | Empty input | No compressed text | Message displayed |

## 10. Sample Input and Output

### Test Case 1

**Input:**
```text
aaabb
```

**Output:**
```text
Original Text: aaabb
Compressed Text: a3b2
Original Length: 5
Compressed Length: 4
Compression Status: BENEFICIAL
Characters Saved: 1
```

### Test Case 2

**Input:**
```text
abc
```

**Output:**
```text
Original Text: abc
Compressed Text: a1b1c1
Original Length: 3
Compressed Length: 6
Compression Status: NOT BENEFICIAL
No space was saved.
```

### Test Case 3

**Input:**
```text
aaaaaabbbb
```

**Output:**
```text
Original Text: aaaaaabbbb
Compressed Text: a6b4
Original Length: 10
Compressed Length: 4
Compression Status: BENEFICIAL
Characters Saved: 6
```

## 11. Screenshots

The program output screenshots are stored in the `screenshots` folder.

## 12. Conclusion

This project demonstrates a simple text compression technique using consecutive character counting. It helps understand strings, loops, conditional statements, and length comparison in Python.

The program also identifies situations where compression does not reduce the text length.
