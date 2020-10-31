#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import all libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
import statsmodels
import os
import binance
import calendar
import dateparser
import datetime as dt
from binance.websockets import BinanceSocketManager
from binance.client import Client
from pandas import Timestamp
from twisted.internet import reactor
from dateutil import parser
from datetime import timedelta, datetime
from tqdm import tqdm_notebook
import datetime as dt


# In[2]:


#Set up connections to TestNet
api_key=os.environ.get('05f7b263c58b55b8bb0c81915b7c034ec80724a52469a150105a63b80fd51f2e')
api_secret=os.environ.get('116d6ba7a9292b5f846df59a5b1855bb3901032f591a9c47c45b890b346f82d6')


# In[3]:


#Re-initate the Client
client = Client(api_key, api_secret)


# In[4]:


#Check if client is working
client.ping()


# In[5]:


#Check timed connection to server
time_res = client.get_server_time()


# In[6]:


#Check status of client
status = client.get_system_status()


# In[7]:


#Check any additional information about the client connection
info = client.get_exchange_info()


# In[8]:


#Check the information regarding the intended currency 
infoB = client.get_symbol_info('BTCUSDT')
infoE= client.get_symbol_info('ETHUSDT')


# In[9]:


#See the recent trades with BTC and ETH
tradesB = client.get_recent_trades(symbol='BTCUSDT')
tradesE= client.get_recent_trades(symbol='ETHUSDT')


# In[10]:


#Unhash to print the trades
print(tradesB)
print(tradesE)


# In[11]:


#Startt the connection to Websocket
bm = BinanceSocketManager(client)
# then start the socket manager
bm.start()


# In[12]:


#Once the connections are initated, retrive weekly, daily and minutely data for BTC.
KlinesBW = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1WEEK, limit=7)
KlinesBD= client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1DAY)
KlinesBM = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE)


# In[13]:


#Once the connections are initated, retrive weekly, daily and minutely data for ETH.
KlinesEW = client.get_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_1WEEK)
KlinesED= client.get_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_1DAY)
KlinesEM = client.get_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_1MINUTE)


# In[14]:


#convert desired information to a suitable data frame
df=pd.DataFrame(KlinesBM)
#Rename the columns
dfBM=df.rename(columns={0:'TimeStamp', 1:'Open', 2:'High', 3:'Low', 4:'Close' , 5:'Volumne'})
#Print the new days
print(dfBM)
dfBM['samay']=pd.to_datetime(dfBM['TimeStamp'], unit='ms')
print(dfBM)


# In[15]:


#Finally Let us extract the hour/day/minute
dfBM['hour']=dfBM['samay'].dt.hour
dfBM['minute']=dfBM['samay'].dt.minute
print(dfBM)


# In[16]:


dfBM.index


# In[18]:


dfBM.columns


# In[36]:


dfNew=pd.concat(dfBM['Close'], dfBM['hour'], keys=['dfBM'])


# In[38]:


ax = dfBM.plot.bar(x='hour', y='Close')


# In[22]:


import matplotlib.pyplot as plt
plt.imshow(dfBM, cmap='coolwarm', interpolation='None')
plt.colorbar()
plt.yticks[range(len(dfBM['Close'])),dfBW['Close'], rotation]
plt.xticks[range(len(dfBM['hour'])),dfBW['hour'], rotation]
plt.gcf.set_size_inches(8,8)


# In[39]:


#error correction
dfBM=pd.DataFrame(dtype=float)
# create pivot table, days will be columns, hours will be rows
painting = dfBM.pivot(index=["hour"], columns=["minute"], values='Close')
#plot pivot table as heatmap using seaborn
ax = sns.heatmap(painting, square=True)


# In[ ]:


btc['day']=btc['samay'].dt.day_name()
btc['hour']=btc['samay'].dt.hour
btc['minute']=btc['samay'].dt.minute
print(btc)


# In[ ]:


#Check the first value of timestamped KlinesBW
d1=dateparser.parse('1596412800000')
print(d1)
#Check the last value of timestamped KlineBW
d2=dateparser.parse('1600041600000')
print(d2)


# In[ ]:


#Convert the data to day values
days=pd.to_datetime(df[0])
daysnames=days.dt.day_name(locale='English')
print(daysnames)


# In[ ]:


row_labels=dfBW['TimeStamp']
dfBW=df.astype({'Volumne': float})
col_labels=dfBW['Volumne']


# In[ ]:


#We will now plot the Dataframe as a heatmap for weeklydata
data=pd.DataFrame(np.random.rand(35,1), columns=['close'], index=range(0, 35, 1))
ax=sns.heatmap(data, linewidth=0.5)
ax.set_axis_labels('Week', 'Value')
#Save the figure
plt.savefig('Weekly.jpeg', dpi=100)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
#Show the figure
plt.show()


# In[ ]:


plt.pcolor(new)
plt.yticks(np.arange(0.5, len(new.index), 1), new.index)
plt.xticks(np.arange(0.5, len(new.columns), 1), new.Close)
plt.show()


# In[ ]:


#Dateparser commands to check some dates
sr=dateparser.parse('1600041600000')
print(sr)


# In[ ]:


#Dateparser commands to check some dates
sr=dateparser.parse('1600646399999')
print(sr)


# In[ ]:


#Dateparser commands to check some dates
sr=dateparser.parse('1502668800000')
print(sr)


# In[ ]:


#Return the day name in English 
result=sr.dt.day_name(locale='English')


# In[ ]:


#Timestamp Command
import date
z=date.fromtimestamp(1600041600000)
print(z)


# In[ ]:


#######
sns.heatmap(x='dfBW.hour', y='dfBW.minute', C='Close', 
            ax.set_ylim([y.min()-0.05, y.max()+0.05])
        except ValueError:  #raised if `y` is empty.
                    pass
                  height=500, width=500, colorbar=False, data=dfBM)


# In[ ]:


# set a timeout of 60 seconds
bm = BinanceSocketManager(client, user_timeout=60)
#Command to timeout websocket
bm.stop_socket(conn_key)
# when you need to exit
reactor.stop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




