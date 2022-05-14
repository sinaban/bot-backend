from urllib import response
import ccxt 
import pandas as pd
import time 
from kucoin_futures.client import Trade,Market
from models import bot_config as myRedis  
import logging
import ccxt.base.exchange
from exchanges import kucoin_pairs


class kucoin_futures_ex():
    def __init__(self,apikey,apisecret,apipass,drydrun) -> None:
        self.apikey=apikey
        self.apisecret=apisecret
        self.apipass=apipass
        self.dryrun=drydrun
        self.exchange= ccxt.kucoin()
        self.exchange.options['defaultType']='futures'
        self.timeframe = [1,5,15,30,60,120,240,480,720,1440,10080]
    def get_client(self):
        client = Trade(key=self.apikey, secret=self.apisecret, passphrase=self.apipass, is_sandbox=False, url='')
        return client
    def get_timefrmaes(self):
        return self.timeframe


    def get_realtimeticker(self,pair):
        price=myRedis.getPrice(pair)
        
        return price ,  kucoin_pairs.futures_pairs[pair]
        # try:
        #     return client.get_ticker(pair).get('price')
        # except:
        #     print('get price error')
    def get_realtimeticker_ASK(self,pair):
        price=myRedis.getAskPrice(pair)
        return price,kucoin_pairs.futures_pairs[pair]

    def create_orderid(self,price,pair,size,side,lever):
        return "under structure"

        if module=='up':
            deal_value=((float)(size)*(float)(price)/(float)(trading_data.pair_dict_long[pair]['lotRatio']))
        elif module=='down':
            deal_value=((float)(size)*(float)(price)/(float)(trading_data.pair_dict_short[pair]['lotRatio']))
        order_id= dbMgr.generate_order_id() 
        dict_temp={
            order_id:{
                'openTime':time.time()*1000,
                'closeTime':time.time()*1000,
                'price':price,
                'size':size,
                'dealValue':deal_value,
                'status':'done',
                'side':side,
                'symbol': pair,
                'leverage':lever
            }
        }
        trading_data.order_data.update(dict_temp)
        return order_id



    def open_market_order(self,pair,side,lever,size):
        


        if self.dryrun==False:
            # client = get_client(side)
            client = self.get_client()
            order_id = client.create_market_order(symbol=pair,side=side,lever=lever,size=size)
            order_id=order_id.get('orderId')
        else:
            price=self.m_get_realtimeticker(pair=pair)
            order_id = self.create_orderid(price=price,pair=pair,size=size,side=side,lever=lever)    
        print('order id : %s'%order_id)
        return order_id

    def cancel_orderId(self,orderId):
        client = self.get_client()
        response=client.cancel_order(orderId)  
        return response 

    def cancel_all_order(self,pair):
        client = self.get_client()
        response=client.cancel_all_limit_order(pair)  
        return response 

    def open_limit_order(self,pair,side,lever,size,price):
        
        if self.dryrun==False:
            # client = get_client(side)
            client = self.get_client()
            if price <0.001:
                price=float("{:.8f}".format(price))
            elif price<100:
                price=float("{:.3f}".format(price))
            else:
                price=float("{:.2f}".format(price))
            order_id = client.create_limit_order(symbol=pair,side=side,lever=lever,size=size,price=(price))
            order_id=order_id.get('orderId')
        else:
            price=self.get_realtimeticker(pair=pair)
            order_id = self.create_orderid(price=price,pair=pair,size=size,side=side,lever=lever)    
        print('order id : %s'%order_id)
        return order_id



    def get_kline(self,pair,timeframe,begin_t=None, end_t=None):
        # exchange_long.set_sandbox_mode(True)
        client = Market(url='https://api-futures.kucoin.com')
        klines = client.get_kline_data(pair,timeframe,begin_t,end_t)

        return kucoin_pairs.futures_pairs[pair], klines
    


    def get_balance(self,refrence) -> float:
        # exchange_long.set_sandbox_mode(True)
        print('Fetching your balance:')
        response = self.exchange.fetch_balance({'type': 'futures', 'currency': refrence})#we must always call this function like this
        # pprint(response) 
        return response['total'].get(refrence)

    
    def get_order_state(self,Oid,lotRatio):
        # 
        if self.dryrun==False:
            client = self.get_client()
            response=client.get_order_details(Oid)   
            return response
        else:
            
            # Response=trading_data.order_data[Oid]
            response = None
            print(response)
    
            return response

    def get_open_positions(self):
        # response=get_keys(side)
        client = self.get_client()
        Response=client.get_all_position()
        for i in range(len(Response)):
            Response[i]['FormalName'] = kucoin_pairs.futures_pairs[Response[i]['symbol']]
        return Response

    def get_ohlc(self,pair,timeframe):
        client = Market(url='https://api-futures.kucoin.com')
        klines = client.get_kline_data(pair,granularity=timeframe)
        ohlc_df=pd.DataFrame(klines,columns=['timestamp','open','high','low','close','volume'])
        ohlc_df['timestamp']=pd.to_datetime(ohlc_df['timestamp'], unit= 'ms')
        return ohlc_df

    def get_overall_account(self,currency):
        client = self.get_client()
        Response=client.get_acount_overview(currency)
        return Response
    
    
    

#debug
# if __name__ == "__main__":
    
#     # print(m_get_ticker('ADAUSDTM',timeframe=15,limit=50))
#     # print( get_overall_account("USDT")[0])
