try:
    from oanda_backtest import Backtest
    #print("Okay ...")
    bt = Backtest(access_token='595225022d3cc629ba460b1269437522-1e76b548494195b2b97c9495c2aab644',
              environment='practice'
    bt.candles("EUR_USD")
    fast_ma = bt.sma(period=5)
    slow_ma = bt.sma(period=25)
    bt.sell_exit = bt.buy_entry = (fast_ma > slow_ma) & (fast_ma.shift() <= slow_ma.shift())
    bt.buy_exit = bt.sell_entry = (fast_ma < slow_ma) & (fast_ma.shift() >= slow_ma.shift())
    bt.run()
    bt.plot()
    
except Exception as ex:
    #print(ex.args[0])
    print("Exception ...")
    

