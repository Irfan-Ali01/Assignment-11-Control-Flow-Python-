import calendar

def main():
    try:
        month_number = int(input("Enter the month (1-12): "))
        if 1 <= month_number <= 12:
            _, num_days = calendar.monthrange(2024, month_number)
            print(f"Number of days in month {month_number}: {num_days}")
        else:
            print("Invalid month number. Please enter a value between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a valid month number (1-12).")

if __name__ == "__main__":
    main()