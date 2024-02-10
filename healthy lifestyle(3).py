def calculate_water_intake(weight, activity_level):
    """
    Calculates daily water intake based on weight and activity level.
    """
    if activity_level == "light":
        water_multiplier = 30
    elif activity_level == "moderate":
        water_multiplier = 35
    elif activity_level == "intense":
        water_multiplier = 40
    else:
        print("Invalid activity level. Assuming moderate activity.")
        water_multiplier = 35

    daily_water_intake = weight * water_multiplier
    return daily_water_intake

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        activity_level = input("Enter your activity level (light/moderate/intense): ").lower()

        recommended_water = calculate_water_intake(weight, activity_level)
        print(f"Recommended daily water intake: {recommended_water:.2f} milliliters")

    except ValueError:
        print("Invalid input. Please enter valid numeric values for weight.")

if __name__ == "__main__":
    main()