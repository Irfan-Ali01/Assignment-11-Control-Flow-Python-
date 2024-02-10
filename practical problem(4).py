def verify_pin(pin):
    """
    Verifies the user's PIN.
    """
    return pin == "5678"  

def main():
    balance = 5000  

    print("Welcome to Simple ATM Machine")
    chances = 3

    while chances > 0:
        pin = input("Please enter your 4-digit PIN: ")

        if verify_pin(pin):
            print("PIN accepted!\n")
            while True:
                print("1. Check Balance")
                print("2. Withdraw Money")
                print("3. Quit")
                option = input("Select an option (1/2/3): ")

                if option == "1":
                    print(f"Your balance is ${balance}")
                elif option == "2":
                    withdraw_amount = float(input("Enter the amount to withdraw: $"))
                    if withdraw_amount <= balance:
                        balance -= withdraw_amount
                        print(f"Withdrawal successful. Your remaining balance is ${balance:}")
                    else:
                        print("Insufficient balance. Please enter a valid amount.")
                elif option == "3":
                    print("Thank you for using our ATM. Have a great day!")
                    break
                else:
                    print("Invalid option. Please select 1, 2, or 3.\n")
        else:
            print("Incorrect PIN. Please try again.")
            chances -= 1

        if chances == 0:
            print("\nNo more tries. Your card is blocked.")
            break

if __name__ == "__main__":
    main()