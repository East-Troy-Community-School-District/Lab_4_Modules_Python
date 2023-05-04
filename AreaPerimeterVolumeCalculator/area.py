'''
Implements all the area calculations.
'''

import math

def select_shape():
    '''
    Asks the user to select a shape for the calculation.
    '''
    shape = input("Square, triangle, rectangle, or circle >> ")
    if shape == "square":
        side_length = float(input("Enter the side length of the square >> "))
        print("Area:", square(side_length))
    elif shape == "triangle":
        height = float(input("Enter the height of the triangle >> "))
        base = float(input("Enter the base of the triangle >> "))
        print("Area:", triangle(height, base))
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle >> "))
        width = float(input("Enter the width of the rectangle >> "))
        print("Area:", rectangle(length, width))
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle >> "))
        print("Area:", circle(radius))
    else:
        print("Invalid shape!")

def square(side_length):
    '''
    Returns the area of a square with the given side length.
    '''
    return side_length**2

def triangle(height, base):
    '''
    Returns the area of a triangle with the given base and height.
    '''
    return 0.5 * height * base

def rectangle(length, width):
    '''
    Returns the area of a rectangle with the given length and width.
    '''
    return length * width

def circle(radius):
    '''
    Returns the area of a circle with the given radius.
    '''
    return math.pi * radius**2