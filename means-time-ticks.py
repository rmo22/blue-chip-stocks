### QUESTIONS ###

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df2 = pd.read_csv('scandiNew.csv')

# Question - ### work out the mean time between trades ####

#Filter update type = 1
# update = [1]

df3=df2['Ticker', 'Trade Volume'].groupby('Ticker').sum('Trade volume')

df4=[ticker for _, ticker in df2.groupby('Ticker')]


#Dictionary

b={}
maxTimeSeconds={}
minTimeSeconds={}
x={}


#grouping each company into lists of 4 dataframes of Dates
for i in range(0, len(df4)):
    b[i]= [x for _, x in df4[i].groupby('Date')]
             
#finding max and min time for each company every day
    maxTimeSeconds[i] = [df3['Time'].max() for df3 in b[i]]
    minTimeSeconds[i] = [df3['Time'].min() for df3 in b[i]]
print("ello")
#putting the list of dictionaries into a matrix
for i in range(len(maxTimeSeconds)):
    maxTimeMatrix = np.array([maxTimeSeconds[i] for i in b])
    minTimeMatrix = np.array([minTimeSeconds[i] for i in b])
#Subtracting matrices to determine the length of each trading day for each ticker
dayLength = np.subtract(maxTimeMatrix = np.array([maxTimeSeconds[i] for i in b]))
#Total time = list (map(sum,resultantTime)
fourDayLength=np.sum(dayLength, axis = 1)
print("munch")
#mean time between trades
timegapTrades = np.divide(fourDayLength, df4['Update Type'])
timegapTrades = timegapTrades.round(decimals = 3)
timegapTrades

# or report using mean time between trades using trade volume
timegapTrades2 = np.divide(fourDayLength, df4['Trade Volume'])
timegapTrades2 = timegapTrades2.round(decimals = 3)
timegapTrades2


### Question ### Mean time between tick changes ### 
#Assigned a tick equal to 2000

tickSize = 2000
totalTicks = np.divide(df4['Trade Volume'], tickSize)
totalTicks.head(5)

#Calculate the number of seconds per trade
tickGap = np.divide(fourDayLength(), totalTicks)

#series to dataframe
tickGap = tickGap.to_frame()
tickGap.columns=['Mean time between ticks (s)']

tickGap.head(5)
