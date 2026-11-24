
print("TEXT COMPRESSION USING CHARACTER RUNS")
print("--------------------------------------")

# Get input text
text = input("Enter a text string: ")

# Initialize variables
compressed = ""
count = 1

# Check whether input is empty
if len(text) == 0:
    print("Please enter a non-empty string.")

else:
    # Process consecutive characters
    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            count += 1

        else:
            compressed += text[i - 1] + str(count)
            count = 1

    # Add the final character group
    compressed += text[-1] + str(count)

    # Compare original and compressed lengths
    original_length = len(text)
    compressed_length = len(compressed)

    print("\nCOMPRESSION RESULTS")
    print("-------------------")

    print("Original Text:", text)
    print("Compressed Text:", compressed)

    print("Original Length:", original_length)
    print("Compressed Length:", compressed_length)

    # Check whether compression is beneficial
    if compressed_length < original_length:

        saved = original_length - compressed_length

        print("Compression Status: BENEFICIAL")
        print("Characters Saved:", saved)

    else:

        print("Compression Status: NOT BENEFICIAL")
        print("No space was saved.")

print("\nText Compression Completed!")
