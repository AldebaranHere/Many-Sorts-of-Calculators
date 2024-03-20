# An Algorithm to Convert between Réaumur and Fahrenheit
starter = int(input("Enter 0 to convert from Fahrenheit to Réaumur. Enter 1 to convert from Réaumur to Fahrenheit: "))
if starter == 0:
    fahrenheit_input = int(input("Enter the value for Fahrenheit: "))
    réaumur_result = ((4 * (fahrenheit_input - 32)) / 9)
    print(f'{fahrenheit_input} in Fahrenheit is {réaumur_result} in Réaumur')
if starter == 1:
    réaumur_input = int(input("Enter the value for Réaumur: "))
    fahrenheit_result = ((9 * réaumur_input) / 4) + 32
    print(f'{réaumur_input} in Réaumur is {fahrenheit_result} in Fahrenheit')
if starter != 0 and 1:
    print("Invalid.")
