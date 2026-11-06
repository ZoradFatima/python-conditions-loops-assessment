"""
Student Scholarship Eligibility System
Task 1 - Conditional Statements (if, elif, else)

Evaluates a student's scholarship eligibility using academic marks,
attendance percentage, and monthly family income.
"""

def get_non_empty_text(prompt):
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Invalid input: this field cannot be empty.")


def get_percentage(prompt):
    """Read a percentage between 0 and 100."""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Please enter a value from 0 to 100.")
        except ValueError:
            print("Invalid input: enter a number, for example 85 or 92.5.")


def get_non_negative_income(prompt):
    """Read a non-negative monthly family income."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Income cannot be negative.")
        except ValueError:
            print("Invalid input: enter income as a number.")


def main():
    print("=" * 55)
    print("       STUDENT SCHOLARSHIP ELIGIBILITY SYSTEM")
    print("=" * 55)

    # Collect and validate student information.
    student_name = get_non_empty_text("Enter student name: ")
    marks = get_percentage("Enter academic marks percentage: ")
    attendance = get_percentage("Enter attendance percentage: ")
    family_income = get_non_negative_income("Enter monthly family income (Rs.): ")

    # Evaluate each requirement separately so all failure reasons can be shown.
    reasons = []

    if marks < 80:
        reasons.append("Academic marks are below the required 80%.")
    if attendance < 85:
        reasons.append("Attendance is below the required 85%.")
    if family_income > 50000:
        reasons.append("Monthly family income is above Rs. 50,000.")

    # Prepare the scholarship decision.
    if len(reasons) == 0:
        if marks >= 90:
            scholarship_type = "Full Scholarship"
        elif marks >= 80:
            scholarship_type = "Partial Scholarship"
        else:
            # This branch is a safety fallback; eligibility already requires 80%.
            scholarship_type = "No Scholarship"
        status = "ELIGIBLE"
    else:
        scholarship_type = "Not Eligible"
        status = "NOT ELIGIBLE"

    # Display a complete evaluation report.
    print("\n" + "=" * 55)
    print("             SCHOLARSHIP EVALUATION REPORT")
    print("=" * 55)
    print(f"Student Name             : {student_name}")
    print(f"Academic Marks           : {marks:.2f}%")
    print(f"Attendance               : {attendance:.2f}%")
    print(f"Monthly Family Income    : Rs. {family_income:,.2f}")
    print("-" * 55)
    print(f"Eligibility Status       : {status}")
    print(f"Scholarship Decision     : {scholarship_type}")

    if reasons:
        print("\nReason(s) for ineligibility:")
        for reason_number, reason in enumerate(reasons, start=1):
            print(f"{reason_number}. {reason}")
    else:
        print("\nCongratulations! All scholarship requirements are satisfied.")

    print("=" * 55)


if __name__ == "__main__":
    main()
