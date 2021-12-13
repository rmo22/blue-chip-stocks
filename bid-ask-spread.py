### QUESTIONS ###

# Question 7 - Mean and Median Bid Ask Spread
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df2 = pd.read_csv('scandiNew.csv')

#new column with bid-ask spread calculated for each row
df2['Bid-Ask Spread']=df2['Ask Price']-df2['Bid Price']

#keeping spread values that are positive
df2 = df2[df2['Bid-Ask Spread'] >0]

#filter to 'Update Type' with a value of 2,3, where 2 is a change to bid and 3 is a change to ask
updateType=[2, 3]
bidAskSpread=df2[df2['Update Type'].isin(updateType)]

#calculating the mean bid-ask spread for each ticker
df3 = bidAskSpread[['Bid-Ask Spread', 'Ticker']].groupby('Ticker').mean() 

#calculating the median bid-ask spread for each ticker
df4 = bidAskSpread[['Bid-Ask Spread', 'Ticker']].groupby('Ticker').median()

#join data frames df3 and df4
df_bidAsk_avgs = pd.merge(df3, df4, right_index=True, left_index=True)

# rename data frame columns
df_bidAsk_avgs.columns= ['Mean Bid-Ask Spread', 'Median Bid-Ask Spread']

# round decimals
df_bidAsk_avgs.round(decimals=2)

#export csv
df_bidAsk_avgs.to_csv('bidAsk_avgs.csv')
