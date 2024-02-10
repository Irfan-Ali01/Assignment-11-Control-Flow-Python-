import calendar

def main():
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))

        if 1 <= month <= 12:
            num_days = calendar.monthrange(year, month)[1]
            print(f"Number of days in {calendar.month_name[month]} {year}: {num_days}")
        else:
            print("Invalid month number. Please enter a value between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for year and month.")

if __name__ == "__main__":
    main()