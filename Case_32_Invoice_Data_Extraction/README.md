
# Case Study 32 – Text-Based Invoice Data Extraction

## 1. Problem Statement

Develop a Python program to process formatted invoice records using basic string operations. The program extracts product codes, quantities, and amounts from invoice strings, validates the records, and identifies malformed invoices.

## 2. Objectives

- To process multiple invoice records.
- To extract product codes, quantities, and amounts.
- To validate invoice information.
- To identify malformed invoice records.
- To display valid and invalid invoices separately.
- To understand string operations, lists, tuples, loops, and conditional statements in Python.

## 3. Assumptions

- Each invoice contains three fields: product code, quantity, and amount.
- Fields are separated by commas.
- Product codes must contain at least two alphanumeric characters.
- Quantity must be a positive whole number or zero.
- Amount must be a non-negative number.
- Invalid records are displayed separately.
- Input amounts are represented in Indian Rupees.

## 4. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Concepts: Strings, String Methods, Lists, Tuples, Loops, Conditional Statements, and Exception Handling

## 5. Algorithm

1. Start the program.
2. Enter the number of invoice records.
3. Create two empty lists for valid and invalid invoices.
4. Repeat the following steps for each invoice:
   - Enter the invoice record.
   - Split the record using commas.
   - Check whether it contains exactly three fields.
   - Extract the product code, quantity, and amount.
   - Validate the product code.
   - Validate the quantity.
   - Validate the amount.
   - If all fields are valid, store the invoice as a tuple in the valid list.
   - Otherwise, store the original record in the invalid list.
5. Display the total number of records.
6. Display valid and invalid invoices separately.
7. Stop the program.

## 6. Flowchart

```text
             START
               |
               v
      Enter Number of Invoices
               |
               v
       Enter Invoice Record
               |
               v
       Split Record by Comma
               |
               v
       Check Number of Fields
               |
               v
       Extract Invoice Details
               |
               v
       Validate Product Code
       Validate Quantity
       Validate Amount
               |
               v
       Are All Fields Valid?
          /          \
        Yes           No
         |             |
         v             v
    Store in        Store in
    Valid List      Invalid List
         |             |
         +------ + ----+
                |
                v
        More Invoices?
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
START

INPUT number_of_records

CREATE empty valid_records list
CREATE empty invalid_records list

FOR each invoice:

    INPUT invoice_record

    SPLIT invoice_record using comma

    IF number of fields is not 3:
        ADD record to invalid_records

    ELSE:

        EXTRACT product_code
        EXTRACT quantity
        EXTRACT amount

        VALIDATE product_code
        VALIDATE quantity
        VALIDATE amount

        IF all fields are valid:

            CREATE invoice tuple
            ADD tuple to valid_records

        ELSE:

            ADD original record to invalid_records

    END IF

END FOR

DISPLAY total records
DISPLAY valid records
DISPLAY invalid records

STOP
```

## 8. Python Source Code

The complete Python implementation is available in `case32.py`.

## 9. Test Cases

| Test Case | Input Record | Expected Result |
|---|---|---|
| 1 | P101,2,500 | Valid |
| 2 | P102,3,750 | Valid |
| 3 | P103,abc,400 | Invalid – Quantity |
| 4 | P104,2,xyz | Invalid – Amount |
| 5 | P105,2 | Invalid – Missing field |
| 6 | P@01,2,500 | Invalid – Product code |

## 10. Sample Input

```text
Enter number of invoice records: 3

Invoice 1
Enter invoice (CODE,QUANTITY,AMOUNT): P101,2,500

Invoice 2
Enter invoice (CODE,QUANTITY,AMOUNT): P102,3,750

Invoice 3
Enter invoice (CODE,QUANTITY,AMOUNT): P103,abc,400
```

## 11. Sample Output

```text
TEXT-BASED INVOICE DATA EXTRACTION
-----------------------------------

Invoice 1
Invoice Status: VALID
Product Code: P101
Quantity: 2
Amount: Rs. 500.0

Invoice 2
Invoice Status: VALID
Product Code: P102
Quantity: 3
Amount: Rs. 750.0

Invoice 3
Invoice Status: INVALID
Error: Invalid quantity.

========== INVOICE SUMMARY ==========

Total Records: 3
Valid Records: 2
Invalid Records: 1

VALID INVOICES
Product: P101 | Quantity: 2 | Amount: Rs. 500.0
Product: P102 | Quantity: 3 | Amount: Rs. 750.0

INVALID INVOICES
P103,abc,400

Invoice Processing Completed!
```

## 12. Screenshots

The screenshots of the program execution are saved in the `screenshots` folder.

## 13. Conclusion

This project successfully extracts and validates invoice information using Python string operations. It identifies valid and malformed records and displays a summary of the invoice data.

Through this project, we learned how to use string methods, lists, tuples, loops, conditional statements, and exception handling to solve a practical invoice-processing problem.

## 14. Author

**Name:** Pravallika  
**Project:** Python Activity-Based Learning  
**Case Study:** 32 – Text-Based Invoice Data Extraction
