
import tushare as ts
data=ts.get_hist_data('300274')
print(data)

import pandas_datareader as pdr
info=pdr.get_data_yahoo('DPZ')


