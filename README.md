# Smart Pharmacy Inventory & Sales Management System

## Project Overview

This Python console application helps a pharmacy process daily medicine sales and monitor stock levels. It asks how many different medicines need to be processed, checks stock availability for each requested sale, calculates successful sales, updates remaining stock, and produces a final daily report.

## File

- `pharmacy_inventory_system.py` — complete source code for the pharmacy inventory and sales application.

## Requirements

- Python 3.8 or later
- A terminal, command prompt, or Python IDE
- No third-party libraries are required

## Features

1. Asks how many different medicines will be processed.
2. Uses a `for` loop and `range()` to process each medicine.
3. Collects the medicine name, available stock, price per unit, and quantity to sell.
4. Checks whether the requested quantity is available.
5. Calculates the sales amount for successful sales.
6. Displays the remaining stock after each medicine is processed.
7. Displays a low-stock warning when remaining stock is below 10 units.
8. Uses an accumulator to calculate total pharmacy revenue.
9. Uses a counter to count medicines requiring restocking.
10. Displays a final report with the number of medicines processed, total revenue, and restocking count.

## Python Concepts Used

- Variables and meaningful variable names
- `input()` and `print()`
- Data types: strings, integers, and floating-point numbers
- Type conversion using `int()` and `float()`
- `for` loop and `range()`
- Conditional statements (`if` and `else`)
- Conditions inside loops
- Arithmetic operators (`*`, `-`, `+=`)
- Accumulators (`total_revenue`)
- Counters (`medicines_requiring_restock`)
- Input validation using `while` loops and `try/except`
- Functions and comments

## How to Run

1. Save `pharmacy_inventory_system.py` to your computer.
2. Open Command Prompt or a terminal in the folder containing the file.
3. Run:

```bash
python pharmacy_inventory_system.py
```

If your system uses `python3`, run:

```bash
python3 pharmacy_inventory_system.py
```

## Sample Execution

The following example processes two medicines:

```text
How many different medicines will you process? 2

--- Medicine 1 of 2 ---
Enter medicine name: Panadol
Enter available stock (units): 20
Enter price per unit (Rs.): 25
Enter quantity to sell (units): 15

Sale processed successfully.
Medicine                 : Panadol
Quantity sold            : 15
Price per unit           : Rs. 25.00
Sale amount              : Rs. 375.00
Remaining stock          : 5 units
LOW-STOCK WARNING: Restocking is required.

--- Medicine 2 of 2 ---
Enter medicine name: Calpol
Enter available stock (units): 8
Enter price per unit (Rs.): 100
Enter quantity to sell (units): 10

Sale could not be processed: insufficient stock.
Medicine                 : Calpol
Requested quantity       : 10
Available stock          : 8
Remaining stock          : 8 units
No revenue was added for this medicine.
LOW-STOCK WARNING: Restocking is required.

DAILY PHARMACY REPORT
Total medicines processed       : 2
Total pharmacy revenue          : Rs. 375.00
Medicines requiring restocking  : 2
```

## Input Validation

The application checks that:

- The number of medicines is a positive whole number.
- The medicine name is not blank.
- Stock and quantity values are whole numbers and cannot be negative.
- The unit price is numeric and cannot be negative.
- A sale cannot exceed the available stock.

## Assessment Testing Scenarios

Test the application with these scenarios:

1. **Successful sale:** Available stock is 20 and quantity sold is 12. The remaining stock should be 8.
2. **Exact-stock sale:** Available stock is 10 and quantity sold is 10. The remaining stock should be 0.
3. **Insufficient stock:** Available stock is 5 and quantity requested is 7. The sale should be rejected and revenue should not increase.
4. **Low-stock warning:** Remaining stock is 9 or fewer units. The warning should appear.
5. **No restocking warning:** Remaining stock is 10 or more units. The warning should not appear.
6. **Invalid input:** Enter letters where a number is required or enter a negative value. The program should ask again.

## Assessment Submission

Upload these files to your GitHub repository for the pharmacy task:

```text
pharmacy-inventory-assessment/
├── pharmacy_inventory_system.py
└── README.md
```

The source code and this README document the Smart Pharmacy Inventory & Sales Management System requirements.




# Python Conditions and Loops Assessment

## Project Overview

This repository contains the two compulsory Python applications for the **Python Conditions and Loops Assessment**. The programs are separate, console-based applications and are implemented according to the assessment requirements.

## Project Structure

```text
python-conditions-loops-assessment/
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## Task 1: Student Scholarship Eligibility System

**File:** `student_scholarship_system.py`

This application collects a student's name, academic marks, attendance percentage, and monthly family income. It validates the entries and evaluates the student against these rules:

- Academic marks must be at least 80%.
- Attendance must be at least 85%.
- Monthly family income must be Rs. 50,000 or less.
- A student who meets all three requirements receives:
  - **Full Scholarship** when marks are 90% or above.
  - **Partial Scholarship** when marks are at least 80% but below 90%.
- Students who do not meet one or more requirements receive a report listing every reason for ineligibility.

### Python concepts used

- `input()` and `print()`
- Variables and descriptive names
- `if`, `elif`, and `else`
- Comparison and logical operators
- `while` loops for input validation
- Lists to collect all ineligibility reasons
- Formatted output

### Sample execution

```text
Enter student name: Ali
Enter academic marks percentage: 92
Enter attendance percentage: 90
Enter monthly family income (Rs.): 45000

SCHOLARSHIP EVALUATION REPORT
Student Name             : Ali
Academic Marks           : 92.00%
Attendance               : 90.00%
Monthly Family Income    : Rs. 45,000.00
Eligibility Status       : ELIGIBLE
Scholarship Decision     : Full Scholarship

Congratulations! All scholarship requirements are satisfied.
```

## Task 2: Smart Pharmacy Inventory & Sales Management System

**File:** `pharmacy_inventory_system.py`

This application asks how many different medicines must be processed and uses a `for` loop with `range()` to process each medicine. For every medicine, it collects the name, available stock, unit price, and requested quantity to sell.

The program checks stock availability before completing a sale. Successful sales contribute to the pharmacy's total revenue and reduce the remaining stock. If the requested quantity is greater than available stock, the sale is rejected and no revenue is added. A low-stock warning is displayed whenever remaining stock is below 10 units.

### Python concepts used

- `input()` and `print()`
- Variables and arithmetic operators
- `for` loops and `range()`
- `if` and `else` conditions inside a loop
- Input validation with `while` loops and `try/except`
- Accumulator (`total_revenue`)
- Counter (`medicines_requiring_restock`)
- Formatted output

### Sample execution

```text
How many different medicines will you process? 2

--- Medicine 1 of 2 ---
Enter medicine name: Panadol
Enter available stock (units): 20
Enter price per unit (Rs.): 25
Enter quantity to sell (units): 15

Sale processed successfully.
Sale amount              : Rs. 375.00
Remaining stock          : 5 units
LOW-STOCK WARNING: Restocking is required.

--- Medicine 2 of 2 ---
Enter medicine name: Calpol
Enter available stock (units): 8
Enter price per unit (Rs.): 100
Enter quantity to sell (units): 10

Sale could not be processed: insufficient stock.
Remaining stock          : 8 units
No revenue was added for this medicine.
LOW-STOCK WARNING: Restocking is required.

DAILY PHARMACY REPORT
Total medicines processed       : 2
Total pharmacy revenue          : Rs. 375.00
Medicines requiring restocking  : 2
```

## Requirements

- Python 3.8 or later
- A terminal, command prompt, or Python IDE

No third-party Python packages are required.

## How to Run the Programs

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run either program separately.

### Run Task 1

```bash
python student_scholarship_system.py
```

### Run Task 2

```bash
python pharmacy_inventory_system.py
```

On some systems, use `python3` instead of `python`.

## Input Validation and Test Scenarios

Both programs reject blank names and invalid numeric input. Percentage values must be between 0 and 100. Income, prices, stock, and quantities cannot be negative.

Suggested scenarios to test:

### Scholarship system

1. Marks 95%, attendance 90%, income Rs. 40,000 — Full Scholarship.
2. Marks 85%, attendance 88%, income Rs. 50,000 — Partial Scholarship.
3. Marks 75%, attendance 90%, income Rs. 40,000 — Ineligible due to marks.
4. Marks 90%, attendance 80%, income Rs. 60,000 — Ineligible due to attendance and income.
5. Enter text instead of a number or a percentage outside 0–100 — validation message appears.

### Pharmacy system

1. Sell a quantity smaller than available stock — sale succeeds and stock decreases.
2. Sell exactly the available stock — sale succeeds and remaining stock becomes zero.
3. Request more units than available — sale is rejected and revenue is unchanged.
4. Finish a sale with fewer than 10 units remaining — low-stock warning appears.
5. Enter a negative number or invalid text — validation message appears.

## GitHub Submission

Create a GitHub repository named:

`python-conditions-loops-assessment`

Upload the three files in the project structure shown above, commit the changes, and push them to GitHub. Then submit the public repository URL and the three required files through the LMS.

**Repository URL:** Add your GitHub repository URL here after publishing the project.

---

**Assessment note:** These are independently implemented applications for the specified scholarship and pharmacy business requirements. Run both files and test the scenarios above before submission.