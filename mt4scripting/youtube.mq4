void onTick()
{

  double movingAverage = iMA(NULL, 0, 15, 0, MODE_SMA, PRICE_MEDIAN, 0);
  double currentPrice = Open[0];
  double lastPrice = Open[1];
  
  if ( (currentPrice > movingAverage) && (currentPrice < lastPrice) ) {
    // sell
    order = OrderSend(NULL,OP_SELL,1,currentPrice,0,NULL,NULL,NULL,0,0,NULL); 
  } else if ( (currentPrice < movingAverage) && (currentPrice > lastPrice) ) {
    // buy
    order = OrderSend(NULL,OP_BUY,1,currentPrice,0,NULL,NULL,NULL,0,0,NULL); 
  }
  
  Alert("Last Price: "+lastPrice+" Current Price: "+currentPrice);
}