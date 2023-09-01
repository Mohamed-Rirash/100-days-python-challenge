import math
def paintcan(height,width,coverage_per_can ):
# formula
    num_of_cans= (wall_height * wall_width) / coverage_per_can

    print(f"{math.ceil(num_of_cans)}  cans  paint covers {height} X {width}")



wall_height = int(input("enter the wall height in metes: "))
wall_width = int(input("Enter the wall width in meters: "))
cover = 5
paintcan(wall_height,wall_width,cover)
