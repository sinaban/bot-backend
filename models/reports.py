
from models.trades import ClosedTrades
from models.bot_prop import Bot_propModel
import pandas as pd
from datetime import datetime
from models import bot_config
import json

class BotReport(ClosedTrades):
    
    def __init__(self, o_exchange, o_pair, o_symbol, o_side, o_order_id, o_id, o_price, o_amount, o_status, o_type, o_oid_close, o_oid_open, o_open_date, o_close_date, o_open_price, o_close_price, o_take_profit, o_dynamic_stoploss, o_profit, o_profit_percent, o_strategy, o_close_reason):
        super().__init__(o_exchange, o_pair, o_symbol, o_side, o_order_id, o_id, o_price, o_amount, o_status, o_type, o_oid_close, o_oid_open, o_open_date, o_close_date, o_open_price, o_close_price, o_take_profit, o_dynamic_stoploss, o_profit, o_profit_percent, o_strategy, o_close_reason)
        

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

    def return_per_day(self,data) -> dict:
        res=[]
        fee=0
        self.exchange_fee=0.0006
        df = data.sort_values(by= "close_date")
        starttime=df['close_date'].iloc[0].replace(hour=00, minute=00)
        priods= pd.date_range(start=starttime,end= df['close_date'].iloc[-1],freq='D')
        # print(len(priods))
        for i in range (len(priods)-1):
            # print(priods[i])
            # print(priods[i+1])
            if not df.loc[(df['close_date']>=priods[i]) & (df['close_date']<priods[(i+1)])].empty :
                df1=df.loc[(df['close_date']>=priods[i]) & (df['close_date']<priods[(i+1)])]
                profit=df1['profit'].cumsum().iloc[-1]
                win = len(df1[df1['profit']>0])
                lose= len(df1[df1['profit']<0])
                for j in range(len(df1)):
                    if j==0:
                        fee=0
                    fee += df1['amount'].iloc[j]*(self.exchange_fee)*2#+ df1['close_price'].iloc[j]*(self.exchange_fee)
                # print(profit)
                # print(fee)
            else: 
                profit=0
                win=0
                lose=0
                fee=0
            temp={
                "date": json.dumps(priods[i],indent=4, sort_keys=True, default=str),
                "profit": profit,
                "win": win,
                "lose": lose,
                "exchange_fee": fee,
                "realized_profit": profit-fee
                }
            
            res.append(temp)
        # print(df.iloc[0])
        # print(res)
        return res

    def get_klines(pair,bot,botid):
        config = json.loads(bot_config.get_bot_config(botid))

        if bot.exchange_name=='kucoin':
            if bot.market_type == 'futures':            
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_kline(pair,config['timeframe'])
                    return response
                except Exception as e:
                    return {}
        return {}
    def get_balance(self,bot,botid):
        config = json.loads(bot_config.get_bot_config(botid))
        if config['dryrun_config']['dryrun_enable'] == False:
            if bot.exchange_name=='kucoin':
                if bot.market_type == 'futures':            
                    from exchanges.kucoin_lib import kucoin_futures_ex
                    try:
                        ex = kucoin_futures_ex(apikey=bot.apikey,apisecret= bot.apisecret,apipass= bot.apipass,drydrun=False)
                        response = ex.get_overall_account(config['currency'])
                        return response
                    except Exception as e:
                        print(f"exception in get balance: {e}")
                        return {}
            return {}
        elif config['dryrun_config']['dryrun_enable'] == True:
            response=bot_config.get_bot_balanceWallet(botid)
            return json.loads(response)

    @classmethod
    def get_bot_reports(cls,botid,perday=True):
        pair_whitelist_dict=[]
        try:
            bot= Bot_propModel.find_by_id(botid)
            if bot:
                cls.name = bot.json()['name']
                cls.id = botid
                res = cls.find_by_id_all(botid)
                df = pd.DataFrame(res)
                cls.overall_profit = df['profit'].cumsum().iloc[-1]
                cls.win = len(df[df['profit']>0])
                cls.loss= len(df[df['profit']<0])
                
                cls.BotTotalProfitPerDay = cls.return_per_day(cls,data=df)
                cls.balance= cls.get_balance(cls,bot,botid)
                if perday == True: 
                    pair_whitelist = bot_config.get_pair_whitelist(botid)
                    if pair_whitelist:
                        i=0
                        for pair in pair_whitelist.keys():
                            df_pair=df[df['pair']==pair]
                            temp={
                                "formal_name" : pair_whitelist[pair]['formal_name'],
                                "PairTotalProfitPerDay" : cls.return_per_day(cls,df_pair),
                                "klines" : cls.get_klines(pair,bot,botid)
                            }
                            
                            pair_whitelist_dict.append(temp)
                            i +=1
                        cls.pair_whitelist=pair_whitelist_dict
                    else:
                        cls.pair_whitelist={}
                    return cls.final_result(cls)
                return cls.final_result_overall(cls)


            # print(cls.final_result(cls))
                
            # print('s')
        except Exception as e:
            print(f'exception in get_bot_reports : {e}')

