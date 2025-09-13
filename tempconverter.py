def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

print("Temperature Converter")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

while True:
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
    elif choice == '2':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
    else:
        print("Invalid choice. Please enter 1 or 2.")
