##
# S&P 500 moving average trade 
# Back Testing
# Author : vaidya.nishant@gmail.com 
# Creation Date : 25-Apr-22
##
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

#google_data = web.DataReader('GOOG', data_source='yahoo', start='2019-9-1')
sp500 = web.DataReader('^GSPC', data_source='yahoo', start='2018-4-1', end='2022-4-1' )
sp500_df = pd.DataFrame(sp500)
sp500_df['42d'] = np.round(sp500_df['Close'].rolling(window=42).mean(),2)
sp500_df['252d'] = np.round(sp500_df['Close'].rolling(window=252).mean(),2)
sp500_df['42d-252d'] = sp500_df['42d']- sp500_df['252d']
SD = 50
sp500_df['Regime'] = np.where(sp500_df['42d-252d'] > SD, 1, 0 )
sp500_df['Regime'] = np.where(sp500_df['42d-252d'] < -SD, -1,sp500_df['Regime'])
#sp500_df[['Close','42d','252d']].plot(grid=True)
#sp500_df['Regime'].plot()
#plt.ylim([-1,1])

#sp500_df.info()
sp500_df['Market'] = np.log( sp500_df['Close']/sp500_df['Close'].shift(1))
sp500_df['Strategy'] = sp500_df['Regime'].shift(1) * sp500_df['Market']
sp500_df[['Market','Strategy']].cumsum().apply(np.exp).plot()
plt.show()
print(sp500_df['42d-252d'].tail())