from audioop import reverse
from ib_insync import * 

import pandas as pd

# connect to IBKR (requires open TWS instance)
ibkr = IB() 
ibkr.connect('127.0.0.1', 7496, clientId = 10)

# set the contract to look for
contract = Stock('AAPL', 'SMART', 'USD')
endDate = ''

# grab history from IBKR 
contractHistory = ibkr.reqHistoricalData(
    contract, 
    endDateTime = endDate,
    durationStr='10 D',
    barSizeSetting='1 min',
    whatToShow='MIDPOINT',
    useRTH=True,
    formatDate=1)

# converting to dataframe for ease of use 
contractHistory_df = util.df(contractHistory)

# print to csv
contractHistory_df.to_csv(contract.symbol+'.csv', index=False)
print(contractHistory_df)