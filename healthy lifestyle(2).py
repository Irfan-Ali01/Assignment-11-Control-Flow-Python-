def calculate_sleep_duration(bedtime, wakeup_time):
    """
    Calculates sleep duration in hours.
    """
    bedtime_minutes = int(bedtime.split(":")[0]) * 60 + int(bedtime.split(":")[1])
    wakeup_minutes = int(wakeup_time.split(":")[0]) * 60 + int(wakeup_time.split(":")[1])

    sleep_minutes = wakeup_minutes - bedtime_minutes
    sleep_hours = sleep_minutes / 60

    return sleep_hours

def main():
    try:
        bedtime = input("Enter your bedtime (HH:MM): ")
        wakeup_time = input("Enter your wake-up time (HH:MM): ")

        sleep_duration = calculate_sleep_duration(bedtime, wakeup_time)
        recommended_sleep = 7.5  # Recommended duration (sleep) in hours

        print(f"Your sleep duration: {sleep_duration:.2f} hours")

        if sleep_duration >= recommended_sleep:
            print("Great job! You met the recommended sleep amount.")
        else:
            print("Consider getting more rest for better health.")

    except ValueError:
        print("Invalid input. Please enter valid time in HH:MM format.")

if __name__ == "__main__":
    main()