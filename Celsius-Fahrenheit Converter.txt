# An Algorithm to Convert between Celsius and Fahrenheit
starter = float(input("Enter 0 to convert from Fahrenheit to Celsius. Enter 1 to convert from Celsius to Fahrenheit: "))
if starter == 0:
    fahrenheit_input = float(input("Enter the value for Fahrenheit: "))
    celsius_result = (5 * (fahrenheit_input - 32) / 9)
    print(f'{fahrenheit_input} in Fahrenheit is {celsius_result} in Celsius')
if starter == 1:
    celsius_input = float(input("Enter the value for Celsius: "))
    fahrenheit_result = ((9 * celsius_input) / 5) + 32
    print(f'{celsius_input} in Celsius is {fahrenheit_result} in Fahrenheit')
if starter != 0 and 1:
    print("Invalid.")
