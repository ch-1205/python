# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:58:17 2021

@author: chira
"""

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

key_path = "C:\\Users\\chira\\.spyder-py3\\api.txt"

# extracting data for a single ticker
ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
data = ts.get_intraday(symbol='INFY',interval='5min', outputsize='full')[0]
data.columns = ["open","high","low","close","volume"]
data = data.iloc[::-1]