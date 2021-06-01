#find the correlation coefficient 
#corrcoef() is in numpy library
#pip3 install numpy
#convert temperature data and the ice cream sale data into arrays
#convert each dataset to float values (by defalut each dataset is string)
#use corrcoef() and pass two datasets to it
#store the output in a variable
#print the correlation coefficient on the screen 

import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Temperature", y="Ice-creamSales")
        fig.show()

def getDataSource(data_path):
    temperature = []
    ice_cream_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-creamSales"]))

    return {"x" : temperature, "y": ice_cream_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature and Ice-creamSales:-  \n--->",correlation[0,1])

def setup():
    data_path  = "./Ice-Creamtemperature.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()

