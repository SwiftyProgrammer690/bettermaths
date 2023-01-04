import math as m

def area2D_circle(radius):
    return m.pi * radius * radius

def area2D_square(length):
    return length * length

def area2D_rectangle(width, length):
    return width * length

def area2D_triangle(base, perpendicular_height):
    return 0.5 * base * perpendicular_height

def area2D_trapezoid(top_base, bottom_base, length):
    base = top_base + bottom_base / 2
    return base * length
