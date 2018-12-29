import os
import sys
import csv

total = 0.0
negs = 0.0
poss = 0.0

with open("transactions_2017sept21_2018oct21.csv") as csvfile:
    
    reader = csv.DictReader(csvfile)
    print(reader)
##    total_profit = 0.0
##    profit = 0.0
##    
##    for i, row in enumerate(reader):
##
##        profit_loss = row['P/L']
##        if profit_loss:
##            profit = float(profit_loss)
##            total_profit += profit
##            
##    print(total_profit)


""" each row
OrderedDict([('Transaction ID', '11264189731'),
('Account Id', '617783'), ('Type', 'Interest'), ('Currency Pair', 'NZD/CHF'),
('Units', '66000'), ('Time (UTC)', '2018-07-17 20:00:00'),
('Price', '0.0000000000'), ('Balance', '8622.65'), ('Interest', '1.3490000000'),
('Pl', '0.0000000000'), ('High Order Limit', '0.0000000000'),
('Low Order Limit', '0.0000000000'), ('Amount', '0.6994343939'),
('Stop Loss', '0.0000000000'), ('Limit Order', '0.0000000000'),
('Transaction Link', '0'), ('Trailing Stop (Pipettes)', '0')])
"""
##        if i > 3:
##            
##            break
##        val = row['Financing']
##        if val:
##            f = float(val)
##            if f <= 0.0:
##                negs += f
##            if f > 0.0:
##                poss += f
####                print(f)
##            total += f
##            
####        if i > 1000: break
##    print("Negative total = {}".format(negs))
##    print("Positive total = {}".format(poss))
##    print(total)
        
##try:
##    import pandas as pd
##
##    df = pd.read_csv("fx_trans_nd.csv")
##    included_columns = ["Date", "Currency Pair", "Type", "Price", "Units",
##    "Interest", "Stop Loss", "Take Profit", "Financing", "P/L"]
##
##    interests = df['Financing']
##    total = 0.0
##    print(len(interests))
##    for interest in interests:
##        
##        if interest == 'NaN' or interest == "nan":
##            pass
##        else:
####            print(type(interest))
##            total += interest
##
##    print(total)
####        else:
####            print("Nan")
##        
####    for col_name in included_columns:
####        print(col_name)
##
####    print(total_interest)
##    
##except Exception as ex:
##    print(ex.args[0])
