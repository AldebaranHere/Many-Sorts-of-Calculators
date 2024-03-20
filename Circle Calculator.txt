# An Algorithm to Calculate the Area and Circumference of a Circle
pi = 3.14159265358979323846264338327950288419716939937510
r = float(input("Enter the value of the radius. (Press the enter button after inputting the value)."))
area_of_the_circle = pi * (r ** 2)
circumference_of_the_circle = pi * 2 * r
print(f'The area is equal to {area_of_the_circle}')
print(f'The circumference is equal to {circumference_of_the_circle}')
