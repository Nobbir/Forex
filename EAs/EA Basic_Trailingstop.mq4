//+------------------------------------------------------------------+
//|                                        EA Basic_Trailingstop.mq4 |
//|                             Copyright 2019, DKP Sweden,CS Robots |
//|                             https://www.mql5.com/en/users/kenpar |
//+------------------------------------------------------------------+
#property copyright   "Copyright 2019, DKP Sweden,CS Robots"
#property description "Expert adviser with trailing stop"
#property link        "https://www.mql5.com/en/users/kenpar"
#property version     "1.00"
#property strict
//////////////////////////////////////////////////////////////////////
//Fully functional expert adviser with Buy/Sell and trailing stop.
//Should not be used for trading as there are no enty rules or
//anything else.
//Basic template, do what ever you want with it. Have fun ;)
//////////////////////////////////////////////////////////////////////
//--Enum
enum OT {_buy,_sell,};
//--Externals
extern int    MagicNumber  = 1234567;
input OT      Ordertype    = _buy;
extern double FixedLot     = 0.01;
extern double TakeProfit   = 50.0;//Take profit in pips
extern double StopLoss     = 50.0;//Stop loss in pips
extern double TrailingStop = 15.0;//Trailing stop in pips
//--Internals
int    Ticket = 0,Sell,Buy,_mode;
double _stoploss,_takeprofit,Lots,_point,pricemode;
color col;
bool rv=false;
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//---Set digits
   if((Digits==5)||(Digits==3))
     { _point=Point*10;}
   else
      _point=Point;
//---
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//---

  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//---
   if(Position()==0)//If no open orders on current chart continue
     {
      SendOrder(StopLoss,TakeProfit);//send Buy or Sell
     }
//--
   Trailing(TrailingStop);
   return;
  }
//--
int SendOrder(double _stop,double _take)
  {
   switch(Ordertype)
     {
      case _buy: //Buy order
         _mode =OP_BUY;
         pricemode = Ask;
         col = Green;
         _stoploss  = Bid-_stop*_point;
         _takeprofit  = Ask+_take*_point;
         break;
      case _sell://Sell order
         _mode = OP_SELL;
         pricemode = Bid;
         col = Red;
         _stoploss = Ask+_stop*_point;
         _takeprofit = Bid-_take*_point;
         break;
     }
   if(CheckMoneyForTrade(Symbol(),_mode,LotSize()))
      Ticket=OrderSend(Symbol(),_mode,LotSize(),pricemode,5,0,0,WindowExpertName(),MagicNumber,0,col);
   if(OrderSelect(Ticket, SELECT_BY_TICKET, MODE_TRADES))
     {
      Print("Bid : " + (string)Bid + ", SL : " + (string)_stoploss + ", TP : " + (string)_takeprofit);
      rv=OrderModify(OrderTicket(), OrderOpenPrice(), _stoploss, _takeprofit, 0);
     }
   if(!rv)
     {
      Print("OrderModify SELL error - code : ", GetLastError());
      Print("WARNING: ORDER #", Ticket, " Failed to set TP/SL");
     }
   return(Ticket);
  }
//--
int Position()
  {
   int dir=0;
   for(int i = OrdersTotal() - 1; i >= 0; i--)
     {
      if(!OrderSelect(i, SELECT_BY_POS))
        {
         Print("Position selector failed - code: ",GetLastError());
        }
      if(OrderSymbol()!=Symbol()&&OrderMagicNumber()!= MagicNumber)
        {
         continue;
        }
      if(OrderCloseTime() == 0 && OrderSymbol()==Symbol() && OrderMagicNumber()==MagicNumber)
        {
         if(OrderType() == OP_SELL)
            dir = -1; //Short positon
         if(OrderType() == OP_BUY)
            dir = 1; //Long positon
        }
     }
   return(dir);
  }
//--
void Trailing(double _tstop)
  {
   double  ND;
//--
   for(int i=0; i<OrdersTotal(); i++)
     {
      if(!OrderSelect(i,SELECT_BY_POS,MODE_TRADES)){
      Print("Order trailing select failed - code : ",GetLastError());}
      if(OrderSymbol()!=Symbol() && OrderMagicNumber()!=MagicNumber)continue;
      if(OrderSymbol()==Symbol() && OrderMagicNumber()==MagicNumber)
        {
         if(OrderType()==OP_BUY)
           {
            if(_tstop>0)
              {
               if((Bid-OrderOpenPrice())>_tstop*_point)
                 {
                  if(((Bid-_tstop*_point)-OrderStopLoss())>_point)
                    {
                     ND=NormalizeDouble(Bid-_tstop*_point,Digits);
                     if(!OrderModify(OrderTicket(),OrderOpenPrice(),ND,OrderTakeProfit(),0,Yellow)){
                     Print("Order modify error - code : ",GetLastError());}
                    }
                 }
              }
           }
         if(OrderType()==OP_SELL)
           {
            if(_tstop>0)
              {
               if((OrderOpenPrice()-Ask)>_tstop*_point)
                 {
                  if((OrderStopLoss()-(Ask+_tstop*_point))>_point)
                    {
                     ND=NormalizeDouble(Ask+_tstop*_point,Digits);
                     if(!OrderModify(OrderTicket(),OrderOpenPrice(),ND,OrderTakeProfit(),0,DarkOrange)){
                     Print("Order modify error - code : ",GetLastError());}
                    }
                 }
              }
           }
        }
     }
   return;
  }
//--
double LotSize()
  {

   Lots = MathMin(MathMax((MathRound(FixedLot/MarketInfo(Symbol(),MODE_LOTSTEP))*MarketInfo(Symbol(),MODE_LOTSTEP)),
                          MarketInfo(Symbol(),MODE_MINLOT)),MarketInfo(Symbol(),MODE_MAXLOT));
   return(Lots);
  }
//--Money check
bool CheckMoneyForTrade(string symb,int type,double lots)
  {
   double free_margin=AccountFreeMarginCheck(symb,type,lots);
   if(free_margin<0)
     {
      string oper=(type==OP_BUY)? "Buy":"Sell";
      Print("Not enough money for ",oper," ",lots," ",symb," Error code=",GetLastError());
      return(false);
     }
//--- checking successful
   return(true);
  }
//+------------------------------------------------------------------+
