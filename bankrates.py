import sys
import os
import re
import operator

try:
    import requests
except Exception as ex:
    print(ex.args[0])
    
from bs4 import BeautifulSoup

web_url = r"https://www.global-rates.com/interest-rates/central-banks/central-banks.aspx"
data = requests.get(web_url)

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

bank_names = ['American', 'Australian', 'British',
             'Canadian', 'European', 'Japanese',
             'New Zealand', 'Swiss']


trs1 = soup.find_all('tr', {'class': 'tabledata1'})
trs2 = soup.find_all('tr', {'class': 'tabledata2'})

trs = trs1 + trs2

banks_analyzed = set()
rate_dict = {}

for tr in trs: #soup.find_all('tr', {'class': 'tabledata1'}):

    bank_name = ''
    curr_rate = -1.0
    prev_rate = -1.0
    date_changed = None
    
    for i, td in enumerate(tr.find_all('td')):
        # i = 0 : central bank's name
        if i == 0:
            bank_name = td.text
            #bank_name = bank_name.strip()
            bank_name = re.sub(r'[^\x00-\x7f]', r'', bank_name)
            bank = bank_name.split()[0]  # American, ....
            if "New" in bank_name.split()[0]:
                bank = "New Zealand"

        if bank in bank_names:

            banks_analyzed.add(bank)
            
            if i == 2:  # interest rate, eg, 1.75 %
                curr_rate = td.text
                curr_rate = re.sub(r'[^\x00-\x7f]', r'', curr_rate)
                curr_rate = float(curr_rate[:-1])

            elif i == 4:   # previous interest rate
                prev_rate = td.text
                prev_rate = re.sub(r'[^\x00-\x7f]', r'', prev_rate)
                prev_rate = float(prev_rate[:-1])
            
            elif i == 5:
                date_changed = td.text
                date_changed = re.sub(r'[^\x00-\x7f]', r'', date_changed)

    d = {"American": "USD", "Canadian": "CAD", "European": "EUR", "Swiss": "CHF", 
    "Australian": "AUD", "British": "GBP", "Japanese": "JPY", "New Zealand": "NZD"}

    
    
    if bank in bank_names and bank in banks_analyzed:
        #print("{}\t: {}".format(d[bank], curr_rate))#, prev_rate))
        rate_dict[d[bank]] = curr_rate
    #print(rate_dict)

sorted_rates = sorted(rate_dict.items(), key=operator.itemgetter(1))
#print(sorted_rates)

for k, v in sorted_rates: #.items():
    print("{}\t: {}".format(k, v))
