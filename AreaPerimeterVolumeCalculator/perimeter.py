'''
Implements all the perimeter calculations.
'''

import math

def select_shape():
    '''
    Asks the user to select a shape for the calculation.
    '''
    shape = input("Square, triangle, rectangle, or circle >> ")
    if shape == "square":
        side_length = float(input("Enter the side length of the square >> "))
        print("Perimeter:", square(side_length))
    elif shape == "triangle":
        side1 = float(input("Enter the first side length of the triangle >> "))
        side2 = float(input("Enter the second side length of the triangle >> "))
        side3 = float(input("Enter the third side length of the triangle >> "))
        print("Perimeter:", triangle(side1, side2, side3))
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle >> "))
        width = float(input("Enter the width of the rectangle >> "))
        print("Perimeter:", rectangle(length, width))
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle >> "))
        print("Circumference:", circle(radius))
    else:
        print("Invalid shape!")

def square(side_length):
    '''
    Returns the perimeter of a square with the given side length.
    '''
    return rectangle(side_length, side_length)

def triangle(side1, side2, side3):
    '''
    Returns the perimeter of a triangle with the given sides.
    '''
    return side1 + side2 + side3

def rectangle(length, width):
    '''
    Returns the perimeter of a rectangle with the given length and width.
    '''
    return 2 * length + 2 * width

def circle(radius):
    '''
    Returns the circumference of a circle with the given radius.
    '''
    return 2 * math.pi * radius
