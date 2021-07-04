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
            'PL',
            'Amount',
            'Balance'])

transactions = set()
# transactions_001-001-1968170-001-1
#with open("transactions_10172020.csv") as csvfile:
with open(r"C:\\github\\Forex\\transactions_001-001-1968170-001-1.csv") as csvfile:
    # csv.DictReader(csvfile)
    csv_reader = csv.DictReader(csvfile)#csv.reader(csvfile)
    total_P_L = 0.0
    total_financing = 0.0
    
    funds = 0.0
    deposits = 0.0
    withdrawals = 0.0

    for i, row in enumerate(csv_reader):
        if i == 0: continue
        
        # transaction = row[3]   # Transactions TRANSFER_FUNDS, TAKE_PROFIT, DAILY_FINANCING
        # if transaction == 'TRANSFER_FUNDS':
        #     trans = int(transaction)

        if not row[17]:
            continue
        else:
            amount = float(row[17])
            if amount < 0:
                withdrawals += amount
            else:
                #amount = float(amount.strip())
                deposits += amount

        if not row[16]:
            continue
        else:
            pl = float(row[16])
            if pl > 0.01:
                #print("PL = ".format(pl))#format(float(row[16])))
                total_P_L = total_P_L + float(row[16])  # Profit-Loss
                #total += transaction
                
        if row[13]:#['Financing']:
            financing = float(row[13])   # Financing
            total_financing += financing

    print("Deposits    = {}".format(deposits))
    print("Withdrawals = {}".format(withdrawals))
    print("***************************************")
    print("Total financing: {}".format(total_financing))
    print("Overall deposit: {}".format(deposits))
    print("Total PL       : {}".format(total_P_L))
    
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
