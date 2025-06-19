# smart_calculator.py

import time

# History list to store calculations
history = []

# Function to perform calculation
def calculate():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        # Save to history
        entry = f"{num1} {operator} {num2} = {round(result, 2)}"
        history.append(entry)
        print("Result:", round(result, 2))
        
    except ValueError:
        print("Please enter valid numbers.")

# Function to show history
def show_history():
    if not history:
        print("No history yet.")
    else:
        print("\n--- Calculation History ---")
        for entry in history:
            print(entry)
        print("---------------------------\n")

# Main loop
def main():
    print("🧠 Welcome to Smart Calculator with History")
    while True:
        print("\nChoose an option:")
        print("1. New Calculation")
        print("2. View History")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            calculate()
        elif choice == '2':
            show_history()
        elif choice == '3':
            print("Thank you for using the Smart Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
