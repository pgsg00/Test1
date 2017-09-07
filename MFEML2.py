#/Users/abelardma/.local
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import datetime as dt
import matplotlib

import plotly.plotly as py
import plotly.graph_objs as go

import pandas_datareader.data as web
from datetime import datetime

import re
import socket

import xml.etree.ElementTree
import urllib
import csv
from bs4 import BeautifulSoup


df = pd.read_csv('amzn.csv', parse_dates = True, index_col = 0)
#print df.dtypes

#Change data type
data = df.replace(r'-', np.nan, regex=True)
data["Open"] = pd.to_numeric(data["Open"])
data["High"] = pd.to_numeric(data["High"])
data["Low"] = pd.to_numeric(data["Low"])
data["Close"] = pd.to_numeric(data["Close"])

print (data.describe())


#Weekly return
weekly = df.resample('W').max()
print weekly
weekly.Close.plot()
plt.title("AMZN Weekly Returns")
plt.ylabel("Price")plt.xlabel("Date")
plt.xlabel("Date")
plt.legend(loc = 'upper right')


#Monthly return
monthly = df.resample('M').sum()
print monthly
weekly.Close.plot()
plt.title("AMZN Monthly Returns")
plt.ylabel("Price")
plt.xlabel("Date")
plt.legend(loc = 'upper right')

#Monthly growth
data = data.sort_index(ascending=True)
print data.head(3)
stock_change = data.apply(lambda x: np.log(x) - np.log(x.shift(1)))
print stock_change.head(3)
stock_change.Close.plot(grid = True).axhline(y = 0, color = "black", lw = 2)
plt.title("AMZN Monthly Growth")
plt.ylabel("Price")
plt.xlabel("Date")
plt.legend(loc = 'upper right')










