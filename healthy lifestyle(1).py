def calculate_calorie_goal(age, weight, activity_level):
    base_calories = 1500
    activity_levels = {"sedentary": 0, "moderate": 300, "active": 500}
    total_calories = base_calories + weight * 30

    return total_calories + activity_levels.get(activity_level.lower(), 0)

try:
    age, weight = int(input("Age: ")), float(input("Weight (kg): "))
    activity_level = input("Activity level: ")
    daily_calories = calculate_calorie_goal(age, weight, activity_level)
    print(f"Daily calorie goal: {daily_calories:.2f} calories")
except ValueError:
    print("Invalid input. Please enter valid numeric values.")