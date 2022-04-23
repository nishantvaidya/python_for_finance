# Google stock volatility and plot stock price
from pickle import TRUE
from tkinter.tix import COLUMN
from turtle import color
from matplotlib.pyplot import figure, subplot, subplots
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt


google_data = web.DataReader('GOOG', data_source='yahoo', start='2019-9-1')
google_df = pd.DataFrame(google_data)
google_df['Log_Ret'] = np.log(google_df['Close']/google_df['Close'].shift(1))
google_df['Volatility'] = google_df['Log_Ret'].rolling(window=252).std() * np.sqrt(252)
google_df[['Close','Volatility']].plot(subplots=True,color='blue')
#df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=['a','b','c'])
#df.plot()
#panda data frame
plt.show()