import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import csv
import collections
import numpy as np



#Exhaust Yahoo data
style.use('ggplot')

start = dt. datetime(2017,5,28)
end = dt. datetime(2017,9,6)

df = web.DataReader('AMZN', 'yahoo', start, end)
print(df.head())
print(df.tail())

#Create a csv
with open("amzn.csv", 'rb') as file:
    #writer = csv.writer(file, delimiter=',')
    data = list(csv.reader(file))
  
#Export data to csv    
df.to_csv('amzn.csv')



df = pd.read_csv('amzn.csv')
#print df.dtypes

#Change data type
data = df.replace(r'-', np.nan, regex=True)
data["Open"] = pd.to_numeric(data["Open"])
data["High"] = pd.to_numeric(data["High"])
data["Low"] = pd.to_numeric(data["Low"])
data["Close"] = pd.to_numeric(data["Close"])

print (data.describe())

#plot
plt.figure()
data.Open.plot()
data.Close.plot()
plt.title("AMZN Price")
plt.ylabel("Price")
plt.xlabel("Date")
plt.legend(loc = 'lower right')