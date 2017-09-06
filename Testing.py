import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import csv
import collections
import numpy as np




df = pd.read_csv('amzn.csv')
#print df.dtypes

#Change data type
data = df.replace(r'-', np.nan, regex=True)
data["Open"] = pd.to_numeric(data["Open"])
data["High"] = pd.to_numeric(data["High"])
data["Low"] = pd.to_numeric(data["Low"])
data["Close"] = pd.to_numeric(data["Close"])

print (data.describe())




#Weekly return
#data.index = pd.to_datetime(data.index, unit='s')

#ticks = data.ix[:, ['Price', 'Volume']]
#bars = ticks.Price.resample('30min', how='ohlc')
#volumes = ticks.Volume.resample('30min', how='sum')

#data.groupby(pd.TimeGrouper(freq = 'M')).count()

weekly = data.resample('W').mean()
weekly




  
        
        
        
        