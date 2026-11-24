
print("NESTED LOOP CALENDAR GENERATOR")
print("--------------------------------")

# Get starting weekday
print("\nWeekday Numbers:")
print("0 - Sunday")
print("1 - Monday")
print("2 - Tuesday")
print("3 - Wednesday")
print("4 - Thursday")
print("5 - Friday")
print("6 - Saturday")

start_day = int(input("\nEnter starting weekday number (0-6): "))
total_days = int(input("Enter number of days in the month (28-31): "))

# Validate input
if start_day < 0 or start_day > 6:
    print("\nInvalid weekday! Enter a number from 0 to 6.")

elif total_days < 28 or total_days > 31:
    print("\nInvalid number of days! Enter 28, 29, 30, or 31.")

else:
    weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    print("\n========== MONTHLY CALENDAR ==========")

    # Display weekday headings
    for day in weekdays:
        print(day, end="  ")

    print()

    # Calculate number of required weeks
    total_weeks = (start_day + total_days + 6) // 7

    current_date = 1

    # Generate calendar using nested loops
    for week in range(total_weeks):
        for day in range(7):

            position = week * 7 + day

            if position < start_day or current_date > total_days:
                print("    ", end="")

            else:
                print(f"{current_date:3} ", end="")
                current_date += 1

        print()

    print("\nCalendar Generated Successfully!")
