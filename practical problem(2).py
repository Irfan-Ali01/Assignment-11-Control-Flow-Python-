def main():
    try:
        temperature = eval(input("Enter the temperature in Celsius: "))
        rain = input("Is it raining? (yes/no): ").lower()

        if temperature < 5:
            print("Wear warm clothing. It's very cold out!")
        elif temperature < 10:
            print("Consider wearing a jacket or sweater.")
        elif temperature < 20:
            print("A light jacket should suffice.")
        else:
            print("No need for a jacket. Enjoy the weather!")

        if rain == "yes":
            print("ENjoy KrOOoo....")

    except ValueError:
        print("Invalid input. Please enter a valid temperature .")

if __name__ == "__main__":
    main()