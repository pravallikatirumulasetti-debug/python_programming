
print("REPEATED WORD AND PHRASE DETECTION")
print("-----------------------------------")

# Get paragraph from user
paragraph = input("Enter a paragraph: ")

# Convert text to lowercase
paragraph = paragraph.lower()

# Remove common punctuation marks
for symbol in ".,!?;:":
    paragraph = paragraph.replace(symbol, "")

# Split paragraph into words
words = paragraph.split()

# Store unique words and their positions
unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

# Display word counts and positions
print("\nWORD OCCURRENCE REPORT")
print("----------------------")

repeated_words = 0

for word in unique_words:
    count = words.count(word)

    if count > 1:
        repeated_words += 1
        positions = []

        for i in range(len(words)):
            if words[i] == word:
                positions.append(i + 1)

        print("\nWord:", word)
        print("Occurrences:", count)
        print("Positions:", positions)

# Display summary
print("\n========== SUMMARY ==========")
print("Total Words:", len(words))
print("Unique Words:", len(unique_words))
print("Repeated Words:", repeated_words)

if repeated_words == 0:
    print("No repeated words found.")

print("\nWord Analysis Completed!")
