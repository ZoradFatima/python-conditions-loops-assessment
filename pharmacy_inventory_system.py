"""
Task 2: Smart Pharmacy Inventory & Sales Management System
Topic: Loop Structures (for loop, range(), conditions inside loops, counters and accumulators)
Description: Manages medicine inventory, processes sales, tracks revenue, and flags low stock.
"""

def get_valid_int(prompt, min_val=0):
    """Validates integer input."""
    while True:
        try:
            value = int(input(prompt))
            if value >= min_val:
                return value
            print(f"Error: Value must be at least {min_val}.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def get_valid_float(prompt, min_val=0.0):
    """Validates float/decimal input."""
    while True:
        try:
            value = float(input(prompt))
            if value >= min_val:
                return value
            print(f"Error: Value must be greater than or equal to {min_val}.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")

def run_pharmacy_system():
    print("=" * 65)
    print("        SMART PHARMACY INVENTORY & SALES MANAGEMENT")
    print("=" * 65)
    
    # 1. Ask how many different medicines need to be processed
    num_medicines = get_valid_int("Enter the number of different medicines to process: ", min_val=1)
    
    # Initialize accumulators and counters
    total_pharmacy_revenue = 0.0
    restock_count = 0
    inventory_summary = []
    
    # 2. Use a for loop to process each medicine
    for i in range(1, num_medicines + 1):
        print(f"\n--- Processing Medicine {i} of {num_medicines} ---")
        med_name = input("Enter Medicine Name: ").strip()
        while not med_name:
            print("Error: Medicine name cannot be empty.")
            med_name = input("Enter Medicine Name: ").strip()
            
        available_stock = get_valid_int("Enter Available Stock (units): ", min_val=0)
        price_per_unit = get_valid_float("Enter Price per Unit (Rs.): ", min_val=0.0)
        
        # 3. Collect requested sales quantity with stock validation
        while True:
            quantity_sold = get_valid_int("Enter Quantity Sold: ", min_val=0)
            # 4. Check whether requested sales quantity is available in stock
            if quantity_sold <= available_stock:
                break
            print(f"Error: Requested quantity ({quantity_sold}) exceeds available stock ({available_stock}). Enter a valid quantity.")
            
        # 5. Calculate total sales amount for each successfully processed medicine
        sale_amount = quantity_sold * price_per_unit
        total_pharmacy_revenue += sale_amount
        
        # 6. Calculate remaining stock after sale
        remaining_stock = available_stock - quantity_sold
        
        # 7 & 9. Check low stock warning and count restocking requirements (< 10 units)
        low_stock_warning = False
        if remaining_stock < 10:
            low_stock_warning = True
            restock_count += 1
            
        # Store summary for final report
        inventory_summary.append({
            "name": med_name,
            "initial": available_stock,
            "sold": quantity_sold,
            "remaining": remaining_stock,
            "revenue": sale_amount,
            "warning": low_stock_warning
        })
        
        # Display transaction summary for this medicine
        print(f"\n[Transaction Receipt: {med_name}]")
        print(f"  - Units Sold     : {quantity_sold}")
        print(f"  - Revenue Generated: Rs. {sale_amount:,.2f}")
        print(f"  - Remaining Stock  : {remaining_stock} units")
        if low_stock_warning:
            print("  *** WARNING: Low stock (< 10 units remaining)! Restocking required. ***")
            
    # 10. Generate Final Comprehensive Report
    print("\n" + "=" * 65)
    print("                 PHARMACY DAILY OPERATIONS FINAL REPORT")
    print("=" * 65)
    print(f"Total Medicines Processed    : {num_medicines}")
    print(f"Total Pharmacy Revenue       : Rs. {total_pharmacy_revenue:,.2f}")
    print(f"Medicines Requiring Restock  : {restock_count}")
    print("-" * 65)
    print(f"{'Medicine Name':<20} | {'Sold':<6} | {'Remaining':<10} | {'Revenue (Rs.)':<12} | {'Status'}")
    print("-" * 65)
    
    for item in inventory_summary:
        status = "RESTOCK" if item["warning"] else "OK"
        print(f"{item['name']:<20} | {item['sold']:<6} | {item['remaining']:<10} | {item['revenue']:<12,.2f} | {status}")
    print("=" * 65)

if __name__ == "__main__":
    run_pharmacy_system()
