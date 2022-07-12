import ccxt 
import pandas as pd
from kucoin_futures.client import Trade,Market
from models import bot_config as myRedis  
import ccxt.base.exchange
from exchanges.kucoin import kucoin_pairs
from exchanges.exchange import Exchange


class KucoinFutures(Exchange):

    def __init__(self, apikey, apisecret, apipass, drydrun) -> None:
        super().__init__(apikey, apisecret, apipass, drydrun)
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

    def get_realtimeticker_ASK(self,pair):
        price=myRedis.getAskPrice(pair)
        return price,kucoin_pairs.futures_pairs[pair]

    def create_orderid(self,price,pair,size,side,lever):
        pass 

    def cancel_orderId(self,orderId):
        client = self.get_client()
        response=client.cancel_order(orderId)  
        return response 

    def get_kline(self,pair,timeframe,begin_t=None, end_t=None):
        client = Market(url='https://api-futures.kucoin.com')
        klines = client.get_kline_data(pair,timeframe,begin_t,end_t)
        return kucoin_pairs.futures_pairs[pair], klines
    
    def get_balance(self,refrence) -> float:
        print('Fetching your balance:')
        response = self.exchange.fetch_balance({'type': 'futures', 'currency': refrence})
        return response['total'].get(refrence)
    
    def get_order_state(self,Oid,lotRatio):
        if self.dryrun==False:
            client = self.get_client()
            response=client.get_order_details(Oid)   
            return response
        else:            
            response = None
            print(response)
    
            return response

    def get_open_positions(self):
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
    

