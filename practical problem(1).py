def calculate_total_cost(unit_price, quantity):
    """
    Calculates the total cost based on unit price and quantity.
    Applies a 10% discount if the total cost exceeds $1000.
    """
    total_cost = unit_price * quantity

    if total_cost > 1000:
        discount = total_cost * 0.10
        total_cost -= discount
        print("Congratulations! You've received a 10% discount.")
    else:
        print("No discount applied.")

    return total_cost

unit_price = float(input("Enter the unit price: "))
quantity = int(input("Enter the quantity: "))

final_cost = calculate_total_cost(unit_price, quantity)
print(f"Total cost after discount: ${final_cost:.2f}")