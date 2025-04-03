def calculator():
    print("Welcome to the Extended Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Modulus (%)")
    print("5. Exponentiation (**)")
    print("6. Floor Division (//)")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} % {num2} = {num1 % num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            print(f"{num1} ** {num2} = {num1 ** num2}")
        elif choice == '6':
            if num2 != 0:
                print(f"{num1} // {num2} = {num1 // num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please select a valid operation.")

# Call the calculator function
calculator()
