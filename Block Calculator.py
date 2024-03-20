# An Algorithm to Calculate the Volume and Surface Area of a Block
length = l = float(input("Enter the value of the length. (Press enter after inputting the value)."))
width = w = float(input("Enter the value of the width. (Press enter after inputting the value)."))
height = h = float(input("Enter the value of the height. (Press enter after inputting the value)."))
volume_block = vb = l * w * h
surface_area_block = sab = (l * w * 2) + (w * h * 2) + (h * l *2)
print(f'The volume of the block is {vb}')
print(f'The surface area of the block is {sab}')
