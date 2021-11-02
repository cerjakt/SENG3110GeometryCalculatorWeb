###################
#
# Name: Jake Cermak
#
# Program Name: Finding Volume and Surface Area of a Sphere
#
# Program Description: A simple program that asks for the radius to
# find the surface area and volume of a sphere.
#
###################
import math
def prompt():
    print("----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME AND SURFACE AREA OF A SPHERE")
    print("----------------------------------------------------------")
    radius = eval(input("Please Enter the Radius: "))
    surfarea = 4 * (math.pi) * (radius)**2
    print("The Surface Area of a Sphere =", round(surfarea,2))
    print("The Volume of a Sphere = ", volume(radius))
    print("----------------------------------------------------------")

def volume(radius):
    volume = (4/3) * (math.pi) * (radius)**3
    return volume

if __name__ == '__main__':
    prompt()