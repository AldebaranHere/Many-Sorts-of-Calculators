# An Algorithm for Converting Scales of Temperature between Celsius, Fahrenheit, Kelvin, Rankine, Delisle, Newton, Réaumur, and Rømer (Coded in Python)
# Source of functions: https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature
print("Choose a scale of temperature to convert from.")
convert_from = float(input("Enter 1 for Celsius. 2 for Fahrenheit. 3 For Kelvin. 4 for Rankine. 5 for Delisle. 6 for Newton. 7 for Réaumur. 8 for Rømer. Press enter after inputting the value."))
if convert_from == 1:
    celsius_input = float(input("Enter the value for Celsius: "))
    celsius_to_fahrenheit = ((9 * celsius_input) / 5) + 32
    celsius_to_kelvin = (celsius_input + 273.15)
    celsius_to_rankine = (9 * (celsius_input + 273.15)) / 5
    celsius_to_delisle = (3 * (100 - celsius_input)) / 2
    celsius_to_newton = (33 * celsius_input) / 100
    celsius_to_réaumur = (4 * celsius_input) / 5
    celsius_to_rømer = ((21 * celsius_input) / 40) + 7.5
    print(f'{celsius_input} C is equal to {celsius_to_fahrenheit} F = {celsius_to_kelvin} K = {celsius_to_rankine} Ra = {celsius_to_delisle} D = {celsius_to_newton} N = {celsius_to_réaumur} Ré = {celsius_to_rømer} Rø')
if convert_from == 2:
    fahrenheit_input = float(input("Enter the value for Fahrenheit: "))
    fahrenheit_to_celsius = (5 * (fahrenheit_input - 32) / 9)
    fahrenheit_to_kelvin = (5 * (fahrenheit_input + 459.67) / 9)
    fahrenheit_to_rankine = fahrenheit_input + 459.67
    fahrenheit_to_delisle = (5 * (212 - fahrenheit_input) / 6)
    fahrenheit_to_newton = (11 * (fahrenheit_input - 32) / 60)
    fahrenheit_to_réaumur = ((4 * (fahrenheit_input - 32)) / 9)
    fahrenheit_to_rømer = ((7 * (fahrenheit_input - 32)) / 24) + 7.5
    print(f'{fahrenheit_input} F is equal to {fahrenheit_to_celsius} C = {fahrenheit_to_kelvin} K = {fahrenheit_to_rankine} Ra = {fahrenheit_to_delisle} D = {fahrenheit_to_newton} N = {fahrenheit_to_réaumur} Ré = {fahrenheit_to_rømer} Rø')
if convert_from == 3:
    kelvin_input = float(input("Enter the value for Kelvin: "))
    kelvin_to_celsius = kelvin_input - 273.15
    kelvin_to_fahrenheit = ((9 * kelvin_input) / 5) - 459.67
    kelvin_to_rankine = (9 * kelvin_input) / 5
    kelvin_to_delisle = (3 * (373.15 - kelvin_input)) / 2
    kelvin_to_newton = (33 * (kelvin_input - 273.15)) / 100
    kelvin_to_réaumur = (4 * (kelvin_input - 273.15)) / 5
    kelvin_to_rømer = ((21 * (kelvin_input - 273.15)) / 40) + 7.5
    print(f'{kelvin_input} K is equal to {kelvin_to_celsius} C = {kelvin_to_fahrenheit} F = {kelvin_to_rankine} Ra = {kelvin_to_delisle} D = {kelvin_to_newton} N = {kelvin_to_réaumur} Ré = {kelvin_to_rømer} Rø')
if convert_from == 4:
    rankine_input = float(input("Enter the value for Rankine: "))
    rankine_to_celcius = ((5 * (rankine_input - 491.67)) / 9)
    rankine_to_fahrenheit = rankine_input - 459.67
    rankine_to_kelvin = (5 * rankine_input) / 9
    rankine_to_delisle = ((5 * (671.67 - rankine_input)) / 6)
    rankine_to_newton = ((11 * (rankine_input - 491.67)) / 60)
    rankine_to_réaumur = ((4 * (rankine_input - 491.67)) / 9)
    rankine_to_rømer = ((7 * (rankine_input - 491.67)) / 24) + 7.5
    print(f'{rankine_input} Ra is equal to {rankine_to_celcius} C = {rankine_to_fahrenheit} F = {rankine_to_kelvin} K = {rankine_to_delisle} D = {rankine_to_newton} N = {rankine_to_réaumur} Ré = {rankine_to_rømer} Rø')
if convert_from == 5:
    delisle_input = float(input("Enter the value for Delisle: "))
    delisle_to_celcius = 100 - ((2 * delisle_input) / 3)
    delisle_to_fahrenheit = 212 - ((6 * delisle_input) / 5)
    delisle_to_kelvin = 373.15 - ((2 * delisle_input) / 3)
    delisle_to_rankine = 671.67 - ((6 * delisle_input) / 5)
    delisle_to_newton = 33 - ((11 * delisle_input) / 50)
    delisle_to_réaumur = 80 - ((8 * delisle_input) / 15)
    delisle_to_rømer = 60 - ((7 * delisle_input) / 20)
    print(f'{delisle_input} D is equal to {delisle_to_celcius} C = {delisle_to_fahrenheit} F = {delisle_to_kelvin} K = {delisle_to_rankine} Ra = {delisle_to_newton} N = {delisle_to_réaumur} Ré = {delisle_to_rømer} Rø')
if convert_from == 6:
    newton_input = float(input("Enter the value for Sir Isaac Newton's Degree of Temperature: "))
    newton_to_celsius = ((100 * newton_input) / 33)
    newton_to_fahrenheit = ((60 * newton_input) / 11) + 32
    newton_to_kelvin = ((100 * newton_input) / 33) + 273.15
    newton_to_rankine = ((60 * newton_input) / 11) + 491.67
    newton_to_delisle = ((50 * (33 - newton_input)) / 11)
    newton_to_réaumur = ((80 * newton_input) / 33)
    newton_to_rømer = ((35 * newton_input) / 22) + 7.5
    print(f'{newton_input} N is equal to {newton_to_celsius} C = {newton_to_fahrenheit} F = {newton_to_kelvin} K = {newton_to_rankine} Ra = {newton_to_delisle} D = {newton_to_réaumur} Ré = {newton_to_rømer} Rø')
if convert_from == 7:
    réaumur_input = float(input("Enter the value for Réaumur: "))
    réaumur_to_celsius = ((5 * réaumur_input) / 4)
    réaumur_to_fahrenheit = ((9 * réaumur_input) / 4) + 32
    réaumur_to_kelvin = ((5 * réaumur_input) / 4) + 273.15
    réaumur_to_rankine = ((9 * réaumur_input) / 4) + 491.67
    réaumur_to_delisle = ((15 * (80 - réaumur_input)) / 8)
    réaumur_to_newton = ((33 * réaumur_input) / 80)
    réaumur_to_rømer = ((21 * réaumur_input) / 32) + 7.5
    print(f'{réaumur_input} Ré is equal to {réaumur_to_celsius} C = {réaumur_to_fahrenheit} F = {réaumur_to_kelvin} K = {réaumur_to_rankine} Ra = {réaumur_to_delisle} D = {réaumur_to_newton} N = {réaumur_to_rømer} Rø')
if convert_from == 8:
    rømer_input = float(input("Enter the value for Rømer: "))
    rømer_to_celsius = ((40 * (rømer_input - 7.5)) / 21)
    rømer_to_fahrenheit = ((24 * (rømer_input - 7.5)) / 7) + 32
    rømer_to_kelvin = ((40 * (rømer_input - 7.5)) / 21) + 273.15
    rømer_to_rankine = ((24 * (rømer_input - 7.5)) / 7) + 491.67
    rømer_to_delisle = ((20 * (60 - rømer_input)) / 7)
    rømer_to_newton = ((22 * (rømer_input - 7.5)) / 35)
    rømer_to_réaumur = ((32 * (rømer_input - 7.5)) / 21)
    print(f'{rømer_input} Rø is equal to {rømer_to_celsius} C = {rømer_to_fahrenheit} F = {rømer_to_kelvin} K = {rømer_to_rankine} Ra = {rømer_to_delisle} D = {rømer_to_newton} N = {rømer_to_réaumur} Ré')
