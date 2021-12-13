import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df2 = pd.read_csv('scandiNew.csv')

#Illustrate observation of trade volumes round number effect
update = [1]
df3 = df2[df2['Update Type'].isin(update)]

#drop update column
round_num= df3.drop(['Update Type'], axis = 1)
round_num2 = [ticker for _, ticker in round_num.groupby('Ticker')]

#Extracting AlFA SS Equity to give an example of the round number effect
round_num_company = round_num2[3]

#Take data from one day
date=[20150420]

day_data_ALFA = round_num_company[round_num_company['Date'].isin(date)]
        
#plotting graph 
ax = plt.gca()

fig = day_data_ALFA.plot(kind='line', x = 'Time', y = 'Trade Price', ax=ax)
plt.rcParams["figure.figsize"] = (20,10)
plt.xlabel('Time (s)', fontsize=14)
# plt.ylabel('Price (SEK)'), fontsize=14)
plt.text(44000, 168.7, 'ALFA SS Equity, Date:20.04.2015')
fig = plt.show()
fig
