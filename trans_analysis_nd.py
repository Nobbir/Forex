import os
import sys
import csv
"""
1  : Ticket
2  : Date
3  : Timezone
4  : Transaction
5  : Details
6  : Instrument
7  : Price
8  : Units
9  : Direction
10  : Spread Cost
11  : Stop Loss
12  : Take Profit
13  : Trailing Stop
14  : Financing
15  : Commission
16  : Conversion Rate
17  : P/L
18  : Amount
19  : Balance
"""
total = 0.0
negs = 0.0
poss = 0.0

#with open("transactions_2017sept21_2018oct21.csv") as csvfile:
#with open("transactions_001-001-1968170-001_afterloss.csv") as csvfile:#("transactions_001-001-1968170-001_afterloss.csv") as csvfile:
#with open(r"C:\github\Forex\transactions_1968170_Aug6_2019.csv") as csvfile:

csvfile = r"C:\github\Forex\transactions_shapla_jan4.csv"
#csvfile = r"C:\github\Forex\nd_primary" transactions_shapla_jan4.csv
csvfile = r"C:\github\Forex\transactions_farn.csv"

with open(csvfile, mode='r') as fxfile:

    total_financing = 0

    try:
        csv_reader = csv.reader(fxfile)
        #print(reader)
        total_profit = 0.0
        profit = 0.0
        profit_loss = None

        for i, row in enumerate(csv_reader):

            if i == 0: continue
            """ for i, r in enumerate(row):
                    print("{}  : {}".format(i+1, r)) """
            # ignore until row# 1208
            # start from row# 1209
            try:
                #profit_loss = row['PL']
                #financing = row[13]
                financing = float(row[13])
                if financing:
                    #print(type(financing))
                    total_financing += financing
                    #print(float(total_financing))
            except:
                continue

            if profit_loss:
                profit = float(profit_loss)
                total_profit += profit
    except Exception as ex:
        print(ex.args[0])
        
    print(round(float(total_financing), 2))


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
