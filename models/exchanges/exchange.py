import pandas as pd
from models import bot_config as myRedis  
import ccxt.base.exchange


class Exchange():
    
    def __init__(self,apikey,apisecret,apipass,drydrun) -> None:
        self.apikey=apikey
        self.apisecret=apisecret
        self.apipass=apipass
        self.dryrun=drydrun

    def get_client(self):
        pass

    def get_timefrmaes(self):
        pass


    def get_realtimeticker(self,pair):
        pass

    def get_realtimeticker_ASK(self,pair):
        pass

    def create_orderid(self,price,pair,size,side,lever):
        pass 


    def cancel_orderId(self,orderId):
        pass


    def get_kline(self,pair,timeframe,begin_t=None, end_t=None):
        pass
    
    def get_balance(self,refrence) -> float:
        pass
    
    def get_order_state(self,Oid,lotRatio):
        pass

    def get_open_positions(self):
        pass

    def get_ohlc(self,pair,timeframe):
        pass

    def get_overall_account(self,currency):
        pass
    

