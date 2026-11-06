"""
Smart Pharmacy Inventory & Sales Management System
Task 2 - Loop Structures

Processes medicine sales, checks stock availability, calculates revenue,
updates remaining stock, and counts medicines requiring restocking.
"""


def get_positive_integer(prompt):
    """Return a whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_negative_integer(prompt):
    """Return a whole number that is zero or greater."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("The value cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_negative_price(prompt):
    """Return a numeric price that is zero or greater."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("The price cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric price.")


def get_medicine_name(prompt):
    """Return a medicine name that is not blank."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Medicine name cannot be empty.")


def main():
    print("=" * 60)
    print("          SMART PHARMACY INVENTORY & SALES SYSTEM")
    print("=" * 60)

    number_of_medicines = get_positive_integer(
        "How many different medicines will you process? "
    )

    # Accumulator and counter used in the final report.
    total_revenue = 0.0
    medicines_requiring_restock = 0

    # Process each medicine using a for loop and range().
    for medicine_number in range(1, number_of_medicines + 1):
        print(f"\\n--- Medicine {medicine_number} of {number_of_medicines} ---")

        medicine_name = get_medicine_name("Enter medicine name: ")
        available_stock = get_non_negative_integer(
            "Enter available stock (units): "
        )
        price_per_unit = get_non_negative_price(
            "Enter price per unit (Rs.): "
        )
        quantity_sold = get_non_negative_integer(
            "Enter quantity to sell (units): "
        )

        # A sale is completed only when enough stock is available.
        if quantity_sold <= available_stock:
            sale_amount = quantity_sold * price_per_unit
            remaining_stock = available_stock - quantity_sold
            total_revenue += sale_amount

            print("\\nSale processed successfully.")
            print(f"Medicine                 : {medicine_name}")
            print(f"Quantity sold            : {quantity_sold}")
            print(f"Price per unit           : Rs. {price_per_unit:,.2f}")
            print(f"Sale amount              : Rs. {sale_amount:,.2f}")
            print(f"Remaining stock          : {remaining_stock} units")
        else:
            # Reject the sale and leave revenue and stock unchanged.
            remaining_stock = available_stock

            print("\\nSale could not be processed: insufficient stock.")
            print(f"Medicine                 : {medicine_name}")
            print(f"Requested quantity       : {quantity_sold}")
            print(f"Available stock          : {available_stock}")
            print(f"Remaining stock          : {remaining_stock} units")
            print("No revenue was added for this medicine.")

        # Count medicines whose remaining stock is below 10 units.
        if remaining_stock < 10:
            print("LOW-STOCK WARNING: Restocking is required.")
            medicines_requiring_restock += 1
        else:
            print("Stock level is sufficient.")

    # Display the final pharmacy report.
    print("\\n" + "=" * 60)
    print("                 DAILY PHARMACY REPORT")
    print("=" * 60)
    print(f"Total medicines processed       : {number_of_medicines}")
    print(f"Total pharmacy revenue          : Rs. {total_revenue:,.2f}")
    print(f"Medicines requiring restocking  : {medicines_requiring_restock}")
    print("=" * 60)


if __name__ == "__main__":
    main()
