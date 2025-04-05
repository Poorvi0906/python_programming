def temperature_converter():
    print("Temperature Converter: ")
    print("Enter your choice:")
    print("1. Convert from Celsius")
    print("2. Convert from Fahrenheit")
    print("3. Convert from Kelvin")

    choice = int(input("Choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print ("Celsius to Fahrenheit")
        print(f"{fahrenheit}°F")
        print ("Celsius to Kelvin")
        print(f"{kelvin}K")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        print ("Fahrenheit to Celsius")
        print(f"{celsius}°C")
        print ("Fahrenheit to Kelvin")
        print(f"{kelvin}K")

    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print ("Kelvin to Celsius")
        print(f"{celsius}°C")
        print ("Kelvin to Fahrenheit")
        print(f"{fahrenheit}°F")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
     

temperature_converter()
