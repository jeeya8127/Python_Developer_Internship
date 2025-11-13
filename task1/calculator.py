def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Invalid operation."

def interactive_calculator():
    print("\n--- Simple Interactive Calculator ---")
    print("Available operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input. Please ensure both operands are numbers.")
            continue

        result = calculator(num1, num2, operation)
        print(f"\nResult: {num1} {operation} {num2} = {result}")

        while True:
            choice = input("\nDo you want to continue calculating? (yes/no): ").lower()
            
            if choice == 'no':
                print("Exiting the calculator. Goodbye!")
                return
            elif choice == 'yes':
                print("Starting new calculation...")
                break
            else:
                print("Invalid choice. Please type 'yes' or 'no'.")

interactive_calculator()
