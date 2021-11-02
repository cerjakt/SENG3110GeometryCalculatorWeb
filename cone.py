###################
#
# Name: Jake Cermak
#
# Program Name: Finding Volume and Surface Area of a Cone
#
# Program Description: A simple program that asks for the radius
# and height to find the surface area, slant, lateral surface area,
# and volume of a cone.
#
###################
import math
def prompt():
    print("--------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A CONE")
    print("--------------------------------------------------------")
    radius = eval(input("Please Enter the Radius of a Cone: "))
    height = eval(input("Please Enter the Height of a Cone: "))
    print()
    slant = math.sqrt(radius**2 + height**2)
    surfarea = ((math.pi) * (radius)) * ((radius) + math.sqrt((height)**2 + (radius)**2))
    #volume = (math.pi) * (radius)**2 * (height/3)
    latsurfarea = ((math.pi) * (radius)) * math.sqrt((height)**2 + (radius)**2)
    print("Length of a Side (Slant) of a Cone =",round(slant,2))
    print("The Surface Area of a Cone =",round(surfarea,2))
    print("The Volume of a Cone = ", volume(radius, height))
    print("The Lateral Surface Area of a Cone =",round(latsurfarea,2))
    print("--------------------------------------------------------")

def volume(radius, height):
    volume = (math.pi) * (radius)**2 * (height/3)
    return volume

if __name__ == '__main__':
    prompt()