#Dockerfile for flask geometry web app
#Name this file "Dockerfile" and put into your source code directory
#use the python 3.8 "buster" container as the base container
FROM python:3.8-slim-buster

#update the container
RUN apt-get update -y

#when running, expose port 5000
EXPOSE 5000

#copy commands
COPY . /SENG3110GeometryCalculatorWeb
COPY templates /SENG3110GeometryCalculatorWeb

#specify to Docker build that /app is the "working directory"
WORKDIR /SENG3110GeometryCalculatorWeb

#run pip3 to install all requirements into the container
RUN pip3 install -r requirements.txt

#finally run the application
CMD ["python3", "GeometryCalcWeb.py"]
