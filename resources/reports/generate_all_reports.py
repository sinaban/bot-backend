
from models.trades import ClosedTrades
from models.bot_prop import BotPropModel
import pandas as pd
from models import bot_config
from models.bot_validation import NoBotError,check_bot_exists
from models.trades import ClosedTrades 

from resources.exchange.get_klines import Klines
from resources.exchange.get_balances import LastBalance

import json


class NoWhiteListError(ValueError):
    pass


class BotReport():

    zero_values={
        "profit": 0,
        "win": 0,
        "lose": 0,
        "fee": 0
    }

    def __init__(self) -> None:
        self.exchange_fee=0.0006
    
    def final_result(self):
        return {
            "name": self.name,
            "id" : self.id,
            "overallProfit" : self.overall_profit,
            "win": self.win,
            "lose": self.loss,
            "BotTotalProfitPerDay" : self.BotTotalProfitPerDay,
            "pair_whitelist" : self.pair_whitelist
        }

    def final_result_overall(self):
        return {
            "name": self.name,
            "id" : self.id,
            "overallProfit" : self.overall_profit,
            "win": self.win,
            "lose": self.loss,
            "BotTotalProfitPerDay" : self.BotTotalProfitPerDay,
            "balance" : self.balance
        }

    def get_win_number(self,df:pd.DataFrame):
        return len(df[df['profit']>0])

    def get_lose_number(self,df:pd.DataFrame):
        return len(df[df['profit']<0])

    def is_dataframe_empty(self, df:pd.DataFrame, period, iternum):
        return df.loc[(df['close_date']>=period[iternum]) & (df['close_date']<period[(iternum+1)])].empty

    def get_data_in_periods(self,df:pd.DataFrame):        
        starttime=df['close_date'].iloc[0].replace(hour=00, minute=00)
        return pd.date_range(start=starttime,end= df['close_date'].iloc[-1],freq='D')        

    def return_per_day(self,data) -> dict:
        res=[]
        fee=0
        df = data.sort_values(by= "close_date")
        priods= self.get_data_in_periods(df)

        for i in range (len(priods)-1):
            if not self.is_dataframe_empty(df, priods, i) :                
                df1=df.loc[(df['close_date']>=priods[i]) & (df['close_date']<priods[(i+1)])]
                profit=df1['profit'].cumsum().iloc[-1]
                win = self.get_win_number(df1)
                lose= self.get_lose_number(df1)
                for j in range(len(df1)):
                    if j==0:
                        fee=0
                    fee += df1['amount'].iloc[j]*(self.exchange_fee)*2

            else: 
                temp = BotReport.zero_values

            temp={
                "date": json.dumps(priods[i],indent=4, sort_keys=True, default=str),
                "profit": profit,
                "win": win,
                "lose": lose,
                "exchange_fee": fee,
                "realized_profit": profit-fee
                }  

            res.append(temp)

        return res

    def get_config(self,botid):
        return json.loads(bot_config.get_bot_config(botid))

    def get_klines(self,pair,bot,botid):
        config = self.get_config(botid)
        data = {
            'pair': pair,
            'timeframe': config['timeframe'],
            'start_time': "",
            'end_time': "",
        }
        response = Klines.collect_klines(botid=botid, data=data)
        return response

    def get_balance(self,bot,botid):        
        config = self.get_config(botid)
        return LastBalance.get_balance(botid,{'currency':config['currency']})
    
    def check_is_pair_whitelist_empty(self,pair_whitelist):
        if not pair_whitelist:
            raise NoWhiteListError("pair white list is empty")
 

    def get_trades_data_from_db_convert(self,botid):     
        return pd.DataFrame(ClosedTrades.find_by_id_all(botid))

    def get_profit_win_lose(self,df: pd.DataFrame):
        self.overall_profit = df['profit'].cumsum().iloc[-1]
        self.win = self.get_win_number(df)
        self.loss= self.get_lose_number(df)

    def get_botname_and_botid(self,bot,botid):
        self.name = bot.json()['name']
        self.id = botid  

    def collect_periodic_data(self,pair_whitelist, df, bot, botid):
        pair_whitelist_dict=[]
        for pair in pair_whitelist.keys():
            df_pair=df[df['pair']==pair]
            temp={
                "formal_name" : pair_whitelist[pair]['formal_name'],
                "PairTotalProfitPerDay" : self.return_per_day(self,df_pair),
                "klines" : self.get_klines(pair,bot,botid)
            }
            
            pair_whitelist_dict.append(temp)
            
        self.pair_whitelist=pair_whitelist_dict

    def calculate_profit_balance(self, df, bot, botid):
        self.get_profit_win_lose(df)            
        self.BotTotalProfitPerDay = self.return_per_day(self,data=df)
        self.balance= self.get_balance(self,bot,botid)

    @classmethod
    def get_bot_reports(cls,botid,perday=True):
        try:
            bot= BotPropModel.find_by_id(botid)
            check_bot_exists(bot)
            cls.get_botname_and_botid(bot,botid)
            df = cls.get_trades_data_from_db_convert(botid)
            cls.calculate_profit_balance(df, bot, botid)

            if perday == True: 
                pair_whitelist = bot_config.get_pair_whitelist(botid)
                cls.check_is_pair_whitelist_empty(pair_whitelist)                
                cls.collect_periodic_data(pair_whitelist=pair_whitelist, df=df, bot=bot, botid=botid)
            else:
                cls.pair_whitelist={}
            return cls.final_result(cls)
            
        except NoWhiteListError as e:
            return {"message" : "No valid whitelist"}, 501
        except NoBotError as e :
            return cls.final_result_overall(cls)
        except Exception as e:
            print(f'exception in get_bot_reports : {e}') , 501

