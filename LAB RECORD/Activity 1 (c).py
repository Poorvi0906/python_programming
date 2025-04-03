def find_largest_number():
    print("Enter five numbers:")
    numbers = [] 

    for i in range(5):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    largest_number = max(numbers)

    print(f"The largest number among the entered numbers is: {largest_number}")

find_largest_number()

