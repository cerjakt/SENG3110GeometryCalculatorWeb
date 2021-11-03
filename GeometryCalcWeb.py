# SENG3110 Software Testing
# 
# Project: Geometry Calculator Web App
#
# Sample Code for the Python Flask Web App Implementation of the Geometry Calculator
#
# Author: Joe Axberg
# Orig Date: 9/22/2021
#
# imports
from flask import Flask, request, render_template, redirect, url_for
import cylinder #we need to import the cylinder so we can instantiate it and invoke the methods
import sphere #we need to import the sphere so we can instantiate it and invoke the methods
import cone #we need to import the cone so we can instantiate it and invoke the methods

#flask plumbing
app = Flask(__name__)

#flask route for the index page
#uses html template for user selection
@app.route("/", methods = ["GET", "POST"])
def mainForm():
   if request.method == "POST":
      sphere = request.form.get("sphere")
      cylinder = request.form.get("cylinder")
      cone = request.form.get("cone")
      print("Selection was: ", sphere, cylinder, cone) #prints to command line for trouble shooting
      if sphere == "on":
         print("User selected sphere") #prints to command line for trouble shooting
         return redirect(url_for('sphereForm'))
      elif cylinder == "on":
         print("User selected cylinder") #prints to command line for trouble shooting
         return redirect(url_for('cylinderForm'))
      elif cone == "on":
         print("User selected cone") #prints to command line for trouble shooting
         return redirect(url_for('coneForm'))     
   return render_template("index.html")

#flask route for the cylinder calculations page
@app.route("/cylinder", methods = ["GET", "POST"])
def cylinderForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       height = request.form.get("hgt") 
       # calculation methods
       surfArea = cylinder.surfArea(int(radius), int(height))
       vol = cylinder.volume(int(radius), int(height))
       latSurfArea = cylinder.latSurfArea(int(radius), int(height))
       topBotArea = cylinder.topBotArea(int(radius), int(height))
       return "User entered:" + "<p>Radius: "+ str(radius) + "<p>Height: " + str(height) + "<p>Surface Area: " + str(surfArea) + "<p>Volume: " + str(vol) + "<p>Lateral Surface Area: " + str(latSurfArea) + "<p>Top or Bottom Surface Area: " + str(topBotArea)
   return render_template("cylinder.html")

#flask route for the cone calculations page
@app.route("/cone", methods = ["GET", "POST"])
def coneForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # getting input with name = lname in HTML form 
       height = request.form.get("hgt") 
       # calculation methods
       slant = cone.slant(int(radius), int(height))
       surfArea = cone.surfArea(int(radius), int(height))
       volume = cone.volume(int(radius), int(height))
       latSurfArea = cone.latSurfArea(int(radius), int(height))
       return "User entered:" + "<p>Radius: "+ str(radius) + "<p>Height: " + str(height) + "<p>Slant: " + str(slant) + "<p>Surface Area: " + str(surfArea) + "<p>Volume: " + str(volume) + "<p>Lateral Surface Area: " + str(latSurfArea)
   return render_template("cone.html")
  
#flask route for the sphere calculations page
@app.route("/sphere", methods = ["GET", "POST"])
def sphereForm():
   if request.method == "POST":
       # getting input with name = fname in HTML form
       radius = request.form.get("rad")
       # calculation methods
       surfArea = sphere.surfArea(int(radius))
       volume = sphere.volume(int(radius))
       return "User entered:" + "<p>Radius: "+ str(radius) + "<p>Surface Area: " + str(surfArea) + "<p>Volume: " + str(volume)
   return render_template("sphere.html")

if __name__=='__main__':   #more flask plumbing so the environment starts correctly
   app.run(host='0.0.0.0')
