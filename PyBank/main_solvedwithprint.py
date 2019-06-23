# Create Imports 
import os 
import csv 
import numpy as np
import pandas as pd 

# Load File 
budget = "../python-challenge/Resources/budget_data.csv"

# Read File              
# budget_df = pd.read_csv(budget)
# budget_df.head()

# changed column header budget_df.columns = ['Date', 'Profit_Losses']

# Total number of months included in the dataset (Total Months: 86)
total_months = len(budget_df.index)


# Net total amount of "Profit/Losses" over the entire period (Answer: $38382578)
net_pl = budget_df['Profit_Losses'].sum()


# The average of the changes in "Profit/Losses" over the entire period  (Answer: Average Change: $-2315.12)
change = budget_df['Profit_Losses'].diff()
pl_change = change.mean()


# The greatest increase in profits (date and amount) over the entire period (Answer: Feb-2012 ($1926159))
maxProf_date = budget_df.loc[budget_df['Profit_Losses'].idxmax(), 'Date']
maxProf = change.max()


# The greatest decrease in losses (date and amount) over the entire period (Answer: Sep-2013 ($-2196167))

maxLoss_date = budget_df.loc[budget_df['Profit_Losses'].idxmin(), 'Date']
maxLoss = change.min()

print('Financial Analysis')
print('Total Months: ' , total_months)
print('Total: $',net_pl)
print ('Average Change: $',round(pl_change,2))
print('Greatest Increase in Profits:', maxProf_date, "$",maxProf)
print('Greatest Decrease in Profits:', maxLoss_date, "$", maxLoss)

f = open('PyBank_Solvedwithprint.py', 'a')
f.write('PyBank_Solvedwithprint.txt')
f.close()
