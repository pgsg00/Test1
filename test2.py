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
import bs4 as bs

import matplotlib.dates as mdates

import pickle
import requests
import fix_yahoo_finance


#sauce = urllib.urlopen('https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC').read()
#soup = bs.BeautifulSoup(sauce, 'lxml')

#table = soup.table
#table = soup.find('table')

#table_rows = table.find_all('tr')

#for tr in table_rows:
  #  td = tr.find_all('td')
   # row = [i.text for i in td]
   # print (row)
    
dfs = pd.read_html('https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC')
for df in dfs:
    print (df.head())
    
    
