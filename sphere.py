#####################################################################
#                                                                   #
# Name: Jake Cermak                                                 #
#                                                                   #
# Program Name: Finding Volume and Surface Area of a Sphere         #
#                                                                   #                                    
# Program Description: A simple program that asks for the radius to #
# find the surface area and volume of a sphere.                     #
#                                                                   #
#####################################################################

import math

def volume(radius):
    volume = (4/3) * (math.pi) * (radius)**3
    return volume

def surfArea(radius):
    surfArea = 4 * (math.pi) * (radius)**2
    return surfArea

def prompt():
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A SPHERE")
    print("----------------------------------------------------------")
    radius = eval(input("Please Enter the Radius: "))
    print("The Surface Area of a Sphere =", round(surfArea(radius),2 ))
    print("The Volume of a Sphere =", round(volume(radius), 2))
    print("----------------------------------------------------------")

if __name__ == '__main__':
    prompt()