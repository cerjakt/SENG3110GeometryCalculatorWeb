######################################################################
#                                                                    #
# Name: Jake Cermak                                                  #
#                                                                    #
# Program Name: Finding Volume and Surface Area of a Cylinder        #
#                                                                    #
# Program Description: A simple program that asks for the radius     #
# and height to find the surface area, volume, lateral surface area, #
# and top or bottom surface area of a cylinder.                      #
#                                                                    #
######################################################################

import math

def surfArea(radius, height):
    surfArea = (2 * (math.pi) * (radius) * (height)) + (2 * (math.pi) * (radius)**2)
    return surfArea

def volume(radius, height):
    volume = math.pi * radius * radius * height
    return volume

def latSurfArea(radius, height):
    latSurfArea = 2 * (math.pi) * (radius) * (height)
    return latSurfArea

def topBotArea(radius, height):
    topBotArea = (math.pi) * (radius)**2
    return topBotArea

def prompt():
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CYLINDER")
    print("------------------------------------------------------------")
    radius = eval(input("Please Enter the Radius: "))
    height = eval(input("Please Enter the Height: "))
    print()
    print("The Surface Area of a Cylinder =", round(surfArea(radius, height),2 ))
    print("The Volume of a Cylinder =", round(volume(radius, height), 2))
    print("Lateral Surface Area of a Cylinder =", round(latSurfArea(radius, height),2 ))
    print("Top or Bottom Surface Area of a Cylinder =", round(topBotArea(radius, height), 2))
    print("------------------------------------------------------------")

if __name__ == '__main__':
    prompt()