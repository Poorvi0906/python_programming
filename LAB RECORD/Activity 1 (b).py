def temperature_converter():
    print("Temperature Converter: Celsius, Fahrenheit, Kelvin")
    print("Enter your choice:")
    print("1. Convert from Celsius")
    print("2. Convert from Fahrenheit")
    print("3. Convert from Kelvin")

    choice = int(input("Choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {fahrenheit}°F")
        print(f"{celsius}°C = {kelvin}K")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{fahrenheit}°F = {celsius}°C")
        print(f"{fahrenheit}°F = {kelvin}K")

    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{kelvin}K = {celsius}°C")
        print(f"{kelvin}K = {fahrenheit}°F")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

temperature_converter()
