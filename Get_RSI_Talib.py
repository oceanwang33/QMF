# #先看10日的移动均线：
#
# import tushare as ts
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import talib
#
# df=ts.get_k_data('600600')
# df['MA10_rolling'] = pd.rolling_mean(df['close'],10)
# close = [float(x) for x in df['close']]
# # 调用talib计算10日移动平均线的值
# df['MA10_talib'] = talib.MA(np.array(close), timeperiod=10)
# df.tail(12)

# #再来看指数移动均线和MACD
#
# import tushare as ts
# import matplotlib.pyplot as plt
# import numpy as np
# import talib
#
# df=ts.get_k_data('600600')
# close = [float(x) for x in df['close']]
# # 调用talib计算指数移动平均线的值
# df['EMA12'] = talib.EMA(np.array(close), timeperiod=6)
# df['EMA26'] = talib.EMA(np.array(close), timeperiod=12)
#  # 调用talib计算MACD指标
# df['MACD'],df['MACDsignal'],df['MACDhist'] = talib.MACD(np.array(close),
#                             fastperiod=6, slowperiod=12, signalperiod=9)
# df.tail(12)

#
# #最后来看动量和RSI的函数
#
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib

df=ts.get_k_data('600600')
close = [float(x) for x in df['close']]
df['RSI']=talib.RSI(np.array(close), timeperiod=12)     #RSI的天数一般是6、12、24
df['MOM']=talib.MOM(np.array(close), timeperiod=5)
df.tail(12)
