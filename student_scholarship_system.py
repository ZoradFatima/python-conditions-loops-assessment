"""
Task 1: Student Scholarship Eligibility System
Topic: Conditional Statements (if, elif, else)
Description: Evaluates university scholarship eligibility based on academic marks,
             attendance percentage, and monthly family income with input validation.
"""

def get_valid_string(prompt):
    """Validates and returns a non-empty string input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")

def get_valid_float(prompt, min_val, max_val):
    """Validates numeric input within a specific range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Error: Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid number.")

def evaluate_scholarship():
    print("=" * 60)
    print("      UNIVERSITY SCHOLARSHIP ELIGIBILITY EVALUATION SYSTEM")
    print("=" * 60)
    
    # 1. Collect student details with input validation
    student_name = get_valid_string("Enter Student's Full Name: ")
    marks = get_valid_float("Enter Academic Marks (0 - 100%): ", 0.0, 100.0)
    attendance = get_valid_float("Enter Attendance Percentage (0 - 100%): ", 0.0, 100.0)
    
    while True:
        try:
            income = float(input("Enter Monthly Family Income (Rs.): "))
            if income >= 0:
                break
            print("Error: Income cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid numeric amount for income.")
            
    print("\n" + "-" * 60)
    print("Evaluating Eligibility Criteria...")
    print("-" * 60)
    
    # 3. Eligibility Criteria Flags & Reasons
    min_marks_req = 80.0
    min_attendance_req = 85.0
    max_income_req = 50000.0
    
    reasons = []
    is_eligible = True
    
    if marks < min_marks_req:
        is_eligible = False
        reasons.append(f"- Academic marks ({marks}%) are below the minimum required {min_marks_req}%.")
    
    if attendance < min_attendance_req:
        is_eligible = False
        reasons.append(f"- Attendance ({attendance}%) is below the minimum required {min_attendance_req}%.")
        
    if income > max_income_req:
        is_eligible = False
        reasons.append(f"- Monthly family income (Rs. {income:,.2f}) exceeds the maximum limit of Rs. {max_income_req:,.2f}.")
        
    # 4 & 5 & 6. Final Evaluation Report Display
    print("\n" + "=" * 60)
    print("                 SCHOLARSHIP EVALUATION REPORT")
    print("=" * 60)
    print(f"Student Name            : {student_name}")
    print(f"Academic Marks          : {marks}%")
    print(f"Attendance Percentage   : {attendance}%")
    print(f"Monthly Family Income   : Rs. {income:,.2f}")
    print("-" * 60)
    
    if is_eligible:
        print("Status                  : ELIGIBLE FOR SCHOLARSHIP")
        if marks >= 90.0:
            scholarship_type = "Full Scholarship (100% Tuition Waiver)"
        else:
            scholarship_type = "Partial Scholarship (50% Tuition Waiver)"
        print(f"Scholarship Award       : {scholarship_type}")
        print("Remarks                 : Congratulations! All criteria successfully met.")
    else:
        print("Status                  : NOT ELIGIBLE")
        print("Reason(s) for Rejection :")
        for reason in reasons:
            print(f"  {reason}")
        print("Remarks                 : We encourage you to improve your academic standing/attendance.")
    print("=" * 60)

if __name__ == "__main__":
    evaluate_scholarship()
