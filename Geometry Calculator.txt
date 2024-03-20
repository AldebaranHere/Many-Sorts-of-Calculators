# An Algorithm to Calculate Shapes (Still in progress (I haven't programmed some shapes))
print("Enter: 1 to calculate circles. 2 to calculate spheres. 3 to calculate cylinders. 4 to calculate cones. 5 to calculate cubes. 6 to calculate blocks")
starter = int(input("Enter here: "))
if starter == 1:
    radius_input = r = float(input("Enter the radius of the circle: "))
    pi = 3.14159265358979323846264338327950288419716939937510
    area_of_a_circle = pi * (r ** 2)
    circumference_of_a_circle = 2 * pi * r
    print(f'The area of a circle with a radius of {radius_input} is {area_of_a_circle}')
    print(f'The circumference of a circle with a radius of {radius_input} is {circumference_of_a_circle}')
if starter == 2: 
    radius_input = r = float(input("Enter the radius of the sphere: "))
    pi = 3.14159265358979323846264338327950288419716939937510
    sphere_volume = (4 / 3) * pi * (r ** 3)
    sphere_circumference = 4 * pi * (r ** 2)
    print(f'The volume of the sphere with a radius of {radius_input} is {sphere_volume}')
    print(f'The surface area of the sphere with a radius of {radius_input} is {sphere_circumference}')
if starter == 3: 
    radius_input = r = float(input("Enter the radius of the circle of the cylinder: "))
    height_input = h = float(input("Enter the height of the cylinder: "))
    pi = 3.14159265358979323846264338327950288419716939937510
    volume_cylinder = pi * (r ** 2) * h
    surface_area_cylinder = 2 * pi * r * (h + r)
    print(f'The volume of the cylinder is {volume_cylinder}')
    print(f'The surface of the cylinder is {surface_area_cylinder}')
if starter == 4:
    radius_input = r = float(input("Enter the value of the radius: "))
    height_input = h = float(input("Enter the value of the height: "))
    pi = 3.14159265358979323846264338327950288419716939937510
    volume_cone = pi * (r ** 2) * (h / 3)
    surface_area_cone = pi * r * (r + (((h ** 2) + (r ** 2)) ** (1 / 2)))
    print(f'The volume of the cone is {volume_cone}')
    print(f'The surface area of the cone is {surface_area_cone}')
if starter == 5: 
    length = float(input("Enter the value of the length: "))
    volume_cube = length ** 3
    surface_area_cube = 6 * (length ** 2)
    print(f'The volume of the cube with a length of {length} is {volume_cube}')
    print(f'The surface area of the cube with a length of {length} is {surface_area_cube}')
if starter == 6:
    length = float(input("Enter the value of the length: "))
    width = float(input("Enter the value of the width: "))
    height = float(input("Enter the value of the height: "))
    volume_block = length * width * height
    surface_area_block = (length * width * 2) + (width * height * 2) + (height * length * 2)
    print(f'The volume of the block is {volume_block}')
    print(f'The surface area of the block is {surface_area_block}')
