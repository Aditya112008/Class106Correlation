import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="SizeofTv", y="AverageTimeSpentWatchingTvInAWeekHours")
        fig.show()

def getDataSource(data_path):
    size_of_Tv = []
    Average_Time_Spent_Watching_Tv_In_A_Week_Hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_Tv.append(float(row["SizeofTv"]))
            Average_Time_Spent_Watching_Tv_In_A_Week_Hours.append(float(row["AverageTimeSpentWatchingTvInAWeekHours"]))

    return {"x" : size_of_Tv , "y": Average_Time_Spent_Watching_Tv_In_A_Week_Hours }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size Of TV and Average Time Spent Watching TV In A Week (Hours) :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./SizeofTv.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()