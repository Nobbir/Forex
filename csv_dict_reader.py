import os
import sys
import csv

total = 0.0
negs = 0.0
poss = 0.0

odict_keys = (['Ticket',
            'Date',
            'Timezone',
            'Transaction',
            'Details',
            'Instrument',
            'Price',
            'Units',
            'Direction',
            'Spread Cost',
            'Stop Loss',
            'Take Profit',
            'Trailing Stop',
            'Financing',
            'Commission',
            'P/L',
            'Amount',
            'Balance'])

transactions = set()

with open("transactions_2017sept21_2018oct21.csv") as csvfile:
    
    reader = csv.DictReader(csvfile)
    total_P_L = 0.0
    total_financing = 0.0
    
    for i, row in enumerate(reader):

        if row['P/L']:
            if float(row['P/L']) > 0.0875:
                #print(row['P/L'])
                total_P_L = total_P_L + float(row['P/L'])
                #total += transaction
                
        if row['Financing']:
            financing = float(row['Financing'])
            total_financing += financing

    print(total_financing)
    print(total_P_L)
    
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
