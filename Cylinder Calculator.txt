# An Algorithm to Calculate the Volume and Surface Area of a Cylinder
pi = 3.14159265358979323846264338327950288419716939937510
radius = r = int(input("Enter the radius of the circle of the cylinder. (Press enter after inputting the value)."))
height = h = int(input("Enter the height of the cylinder. (Press enter after inputting the value)."))
volume_cylinder = vc = pi * (r ** 2) * h
surface_area_cylinder = sac = 2 * pi * r * (h + r)
print(f'The volume of the cylinder is {vc}')
print(f'The surface of the cylinder is {sac}')
