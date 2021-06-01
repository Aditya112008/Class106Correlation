import plotly.express as px
import csv
with open("./Ice-Creamtemperature.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Temperature",y="Ice-creamSales")
    fig.show()
#data is highly correlated when the temperature increases the sales of the ice cream increases 

#whereas, temperature vs sale of warm clothes in a store are inversely correlated 