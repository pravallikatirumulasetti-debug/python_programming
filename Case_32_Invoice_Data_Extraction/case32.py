
print("TEXT-BASED INVOICE DATA EXTRACTION")
print("-----------------------------------")

# Get number of invoice records
count = int(input("Enter number of invoice records: "))

valid_records = []
invalid_records = []

# Process each invoice
for i in range(count):

    print("\nInvoice", i + 1)

    record = input(
        "Enter invoice (CODE,QUANTITY,AMOUNT): "
    ).strip()

    # Split invoice into fields
    parts = record.split(",")

    # Validate number of fields
    if len(parts) != 3:
        print("Invalid Invoice: Incorrect number of fields.")
        invalid_records.append(record)
        continue

    # Extract invoice details
    code = parts[0].strip()
    quantity_text = parts[1].strip()
    amount_text = parts[2].strip()

    # Validate product code
    code_valid = (
        len(code) >= 2
        and code.isalnum()
    )

    # Validate quantity
    quantity_valid = quantity_text.isdigit()

    # Validate amount
    amount_valid = False

    try:
        amount = float(amount_text)
        if amount >= 0:
            amount_valid = True
    except ValueError:
        amount_valid = False

    # Check all conditions
    if code_valid and quantity_valid and amount_valid:

        quantity = int(quantity_text)

        invoice = (code, quantity, amount)
        valid_records.append(invoice)

        print("Invoice Status: VALID")
        print("Product Code:", code)
        print("Quantity:", quantity)
        print("Amount: Rs.", amount)

    else:
        invalid_records.append(record)
        print("Invoice Status: INVALID")

        if not code_valid:
            print("Error: Invalid product code.")

        if not quantity_valid:
            print("Error: Invalid quantity.")

        if not amount_valid:
            print("Error: Invalid amount.")

# Display final report
print("\n========== INVOICE SUMMARY ==========")

print("\nTotal Records:", count)
print("Valid Records:", len(valid_records))
print("Invalid Records:", len(invalid_records))

print("\nVALID INVOICES")

for invoice in valid_records:
    code, quantity, amount = invoice

    print(
        "Product:", code,
        "| Quantity:", quantity,
        "| Amount: Rs.", amount
    )

print("\nINVALID INVOICES")

for record in invalid_records:
    print(record)

print("\nInvoice Processing Completed!")
