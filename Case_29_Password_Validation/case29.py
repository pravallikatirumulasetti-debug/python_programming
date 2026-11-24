print("PASSWORD POLICY VALIDATION ENGINE")
print("---------------------------------")

sample = input("Enter a sample password to check: ")

print("\nChecking password policy...")
print("Password length:", len(sample))
uppercase = False
lowercase = False

for ch in sample:
    if ch.isupper():
        uppercase = True

    if ch.islower():
        lowercase = True

if uppercase:
    print("Uppercase letter: Passed")
else:
    print("Uppercase letter: Failed")

if lowercase:
    print("Lowercase letter: Passed")
else:
    print("Lowercase letter: Failed")
    digit = False
special = False

for ch in sample:
    if ch.isdigit():
        digit = True

    elif not ch.isalnum():
        special = True

if digit:
    print("Digit: Passed")
else:
    print("Digit: Failed")

if special:
    print("Special character: Passed")
else:
    print("Special character: Failed")
    # Final password validation

if (len(sample) >= 8 and uppercase and lowercase
        and digit and special and not repeated
        and "password" not in sample.lower()):

    print("\nPassword Status: VALID")
    print("All password rules are satisfied.")

else:
    print("\nPassword Status: INVALID")
    print("Please follow all password rules.")

print("PASSWORD POLICY VALIDATION ENGINE")
print("---------------------------------")

sample = input("Enter a sample password to check: ")

print("\nChecking password policy...")

# Check minimum length
length_valid = len(sample) >= 8

# Check character categories
uppercase = False
lowercase = False
digit = False
special = False

for ch in sample:
    if ch.isupper():
        uppercase = True
    elif ch.islower():
        lowercase = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

# Check repeated characters
repeated = False

for i in range(len(sample) - 2):
    if sample[i] == sample[i + 1] == sample[i + 2]:
        repeated = True

# Check prohibited word
prohibited = "password" in sample.lower()

# Display individual results
print("Minimum length:", "Passed" if length_valid else "Failed")
print("Uppercase letter:", "Passed" if uppercase else "Failed")
print("Lowercase letter:", "Passed" if lowercase else "Failed")
print("Digit:", "Passed" if digit else "Failed")
print("Special character:", "Passed" if special else "Failed")
print("Repeated characters:", "Failed" if repeated else "Passed")
print("Prohibited word:", "Failed" if prohibited else "Passed")

# Final result
if (length_valid and uppercase and lowercase and digit
        and special and not repeated and not prohibited):
    print("\nPassword Status: VALID")
else:
    print("\nPassword Status: INVALID")
    # Check repeated characters
repeated = False

for i in range(len(sample) - 2):
    if sample[i] == sample[i + 1] == sample[i + 2]:
        repeated = True
