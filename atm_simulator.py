# Simple ATM Simulator

balance = 5000
correct_pin = "1234"


# Function to check balance
def check_balance():
    print("Current Balance: ₹", balance)


# Function to deposit money
def deposit():
    global balance

    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance += amount
        print("₹", amount, "deposited successfully.")
    else:
        print("Invalid deposit amount.")


# Function to withdraw money
def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount
        print("₹", amount, "withdrawn successfully.")


# PIN-based login
print("===== SIMPLE ATM =====")

pin = input("Enter your PIN: ")

if pin == correct_pin:

    print("\nLogin Successful!")

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access Denied.")
