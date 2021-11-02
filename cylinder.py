###################
#
# Name: Jake Cermak
#
# Program Name: Finding Volume and Surface Area of a Cylinder
#
# Program Description: A simple program that asks for the radius
# and height to find the surface area, volume, lateral surface area,
# and top or bottom surface area of a cylinder.
#
###################
import math
def prompt():
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CYLINDER")
    print("------------------------------------------------------------")
    radius = eval(input("Please Enter the Radius: "))
    height = eval(input("Please Enter the Height: "))
    print()
    surfarea = (2 * (math.pi) * (radius) * (height)) + (2 * (math.pi) * (radius)**2)
    latsurfarea = 2 * (math.pi) * (radius) * (height)
    topbotarea = (math.pi) * (radius)**2
    print("The Surface Area of a Cylinder =",round(surfarea,2))
    print("The Volume of a Cylinder = ", volume(radius, height))
    print("Lateral Surface Area of a Cylinder =",round(latsurfarea,2))
    print("Top or Bottom Surface Area of a Cylinder =",round(topbotarea,2))
    print("------------------------------------------------------------")

def volume(radius, height):
    volume = math.pi * radius * radius * height
    return volume

if __name__ == '__main__':
    prompt()