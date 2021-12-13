# Trade volume illustration of the round number effect
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df2 = pd.read_csv('scandiNew.csv')

# filter for update type 1

update = [1]

df2 = df2[df2['Update Type'].isin(update)]

# Drop update type column
df2 = df2.drop(['Update Type'], axis = 1)

# creating a histogram
plt.figure(1)
plt.rcParams["figure.figsize"] = (20,10)

company = ['ALFA SS Equity']

df3 = df2[df2['Ticker'].isin(company)]
fig1 = plt.hist(df3['Trade Price'], bins = 1000,)
plt.tick_params(axis="x", labelsize=12)
plt.tick_params(axis="y", labelsize=12)
plt.xlabel('Price (SEK)', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
fig1 = plt.show()
fig1