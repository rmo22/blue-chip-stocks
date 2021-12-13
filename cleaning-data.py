import pandas as pd

#csv file name
tickrData = 'scandi.csv'

#import data #c to speed up import
df = pd.read_csv(tickrData, engine = 'c', usecols = range(0,15))

#adding column names
df.columns = ['Ticker', 'Column2', 'Bid Price','Ask Price','Trade Price', 'Bid Volume', 'Ask Volume', 'Trade Volume', 'Update Type', 'Column10', 'Date', 'Time', 'Opening Price', 'Column14', 'Condition Codes']

#delete columns 
df.drop(['Column2', 'Column10', 'Column14'], axis = 1, inplace = True)

#Condition Codes Column, keep XT and blank rows
#assign blank cells as 'nan'
df['Condition Codes'] = df['Condition Codes'].fillna('nan')

values = ['nan','XT']


df2 = df[df['Condition Codes'].isin(values)]

print (df2.head())

#Condion code drop because data sorted and conditions accounted for
df2.drop(['Condition Codes'], axis = 1, inplace = True)

#export df2 to csv as the overall clean data set

df2.to_csv('scandiNew.csv')