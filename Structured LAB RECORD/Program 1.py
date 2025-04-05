def calculator():
    print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation:")
print("1. Add")
print("2. Divide")
choice = input("Enter choice (1/2): ")
if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
elif choice == '2':
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1/num2}")
    else: 
     print("Error! Division by zero.")
else:
    print("Invalid Input")
calculator()
