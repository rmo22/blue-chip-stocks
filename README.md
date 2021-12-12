# blue-chip-stocks

Task details
Complete the following analysis:

*1 Mean time between trades
To work out mean time between trade…?
* 2. Median time between trades
Repeat above with median function
* 3. Mean time between tick changes
This is crucial as tick changes are done on a volume bases rather than time bases, so relating the two indicates periods of rest in the market.
Mean time between tick changes will surely depend on tick volume that you use (e.g. fibonaci number, I think I will set my number to 2000 as apparently this is good for intra day trading.
* 4. Median time between tick changes
Repeat above with median function
*5. Longest time between trades
Look at the trade volume and calculate the number of 0’s in a row in the seconds past midnight for each ticker.
* 6 Longest time between tick changes
Work out the time between each tick (i.e. the time taken between 2000 vol being reached) then determine the largest time window across the ticks. You might be able to work this out by using the opening category (column 13) i.e. when an opening price changes this is the start of a new tick so you can work out the time taken for that to happen

Q7 and Q8 only requires the columns bid price, ask price, update type and ticker
* 7 Mean bid ask spread
Probably I can ignore points of the day when there are no bids I.e. closed market hours or this would skew the data
Calculate the mean bid ask price
* 8 Median bid ask spread
Calculate the median bid ask spread which I think is = median [(bid-ask)]. The spread as a % is ((bid-ask)/ask)*100. Not sure if they want % or value. To compare across all tickers probably a % is more valuable. 
* Q9 Examples of the round number effect - (both in traded values and traded volumes - i.e. is there an increased probability of the last digit on prices being a 0 compared to other last digits)
I.e. what happens to values around round numbers, what happens to volumes around round numbers (the numbers increase because people set their open bids and stop losses at round numbers generally. So I need to filter for prices with 0 at the end and then show the volume at each of these. Maybe also do the last 2 0’s to see if those have an even higher volume. It depends on the number of DP in the data set I guess. The stock price may be in pennies in which case we would just be looking at the last 0 rather than the decimal places? I can find an example from one company and do a tick chart to show the volume at a round number.
The CSV has the following fields / columns:

1 = Bloomberg Code/Stock identifier
3 = Bid Price
4 = Ask Price
5 = Trade Price
6 = Bid Volume 
7 = Ask Volume
8 = Trade Volume
9 = Update type => 1=Trade; 2= Change to Bid (Px or Vol); 3=Change to Ask (Px or Vol) -Where Px is price
11 = Date
12 = Time in seconds past midnight
13 = Opening price
15 = Condition codes


This data is over several days and so when no trading occurs there are large time gaps to take into account so as not to skew the figures. – The way to account for this is only to look at the data with the ticks – i.e. this will weed out the time periods when there is no trading. So if consolidating data into 2000 ticks something like this might work. 

Please also exclude auctions from your analysis. There should be c. 2 auctions a day - morning and afternoon. During this period you will see crossed spreads (i.e. bid price is larger than ask price) along with specific condition codes. Please only include the XT condition code (along with no condition code).

A tick chart gives a much better view of the price action. A tick chart has four different signals including open, close, high and low.
Benefits of tick charts
Noise reduction, smart money coming in, simplify trading, trend changes, works well with Wolfe Waves
A 2000 tick chart is used for shorter scalps intraday. This is probably something I should look at.
