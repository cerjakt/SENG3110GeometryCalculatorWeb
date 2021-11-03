######################################################################
#                                                                    #
# Name: Jake Cermak                                                  #
#                                                                    #
# Program Name: Finding Volume and Surface Area of a Cone            #
#                                                                    #
# Program Description: A simple program that asks for the radius     #
# and height to find the surface area, slant, lateral surface area,  #
# and volume of a cone.                                              #
#                                                                    #
######################################################################

import math

def slant(radius, height):
    slant = math.sqrt(radius**2 + height**2)
    return round(slant, 2)

def surfArea(radius, height):
    surfArea = ((math.pi) * (radius)) * ((radius) + math.sqrt((height)**2 + (radius)**2))
    return round(surfArea, 2)

def volume(radius, height):
    volume = (math.pi) * (radius)**2 * (height/3)
    return round(volume, 2)

def latSurfArea(radius, height):
    latSurfArea = ((math.pi) * (radius)) * math.sqrt((height)**2 + (radius)**2)
    return round(latSurfArea, 2)

def prompt():
    print("--------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CONE")
    print("--------------------------------------------------------")
    radius = eval(input("Please Enter the Radius of a Cone: "))
    height = eval(input("Please Enter the Height of a Cone: "))
    print()
    print("Length of a Side (Slant) of a Cone =", slant(radius, height))
    print("The Surface Area of a Cone =", surfArea(radius, height))
    print("The Volume of a Cone =", volume(radius, height))
    print("The Lateral Surface Area of a Cone =", latSurfArea(radius, height))
    print("--------------------------------------------------------")

if __name__ == '__main__':
    prompt()