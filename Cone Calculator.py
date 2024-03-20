# An Algorithm to Calculate the Volume and Surface Area of a Cone
pi = 3.14159265358979323846264338327950288419716939937510
radius = r = float(input("Enter the value of the radius. (Press the enter button after inputting the value)."))
height = h = float(input("Enter the value of the height. (Press the enter button after inputting the value)."))
volume_cone = vc = pi * (r ** 2) * (h / 3)
surface_area_cone = sac = pi * r * (r + (((h ** 2) + (r ** 2)) ** (1 / 2)))
print(f'The volume of the cone is {vc}')
print(f'The surface area of the cone is {sac}')
