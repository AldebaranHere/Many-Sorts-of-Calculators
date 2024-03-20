# An Algorithm to Calculate the Volume and Surface Area of a Sphere
pi = 3.14159265358979323846264338327950288419716939937510
r = int(input("Enter the value of the radius. (Press the enter button after inputting the value)."))
constant_sphere_volume = csv = 4 / 3
constant_sphere_surface_area = cssa = 4
sphere_volume = csv * pi * (r ** 3)
sphere_circumference = cssa * pi * (r ** 2)
print(f'The volume of the sphere is {sphere_volume}')
print(f'The surface area of the sphere is {sphere_circumference}')
