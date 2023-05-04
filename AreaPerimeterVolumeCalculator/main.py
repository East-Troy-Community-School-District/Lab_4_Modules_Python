'''
UPDATE THIS PROGRAM HEADER
'''

import area
import perimeter

repeat = "y"
while repeat == "y":
    calculation_type = input("Do you need to calculate an area or perimeter? >> ")
    if calculation_type == "area":
        area.select_shape()
    elif calculation_type == "perimeter":
        perimeter.select_shape()
    else:
        print("Invalid operation!")
    repeat = input("Would you like to calculate another area or perimeter? (y/n) >> ")
    print()