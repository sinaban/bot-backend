

status={}

commands={
    "start": False,
    "stop": False,
    "stop_buy": False,
    "restart": False
}

config ={
    "pair_whitelist": {

        "SOLUSDTM":{
            "formal_name":"SOL/USDT",
            "lotRatio": 10,
            "size":2,
            "long_sl":1,
            "short_sl":1,
            "volatility_ratio":10,
            "atr_slope_ratio":0.1
		
        }
     
    },
 
"indicators": {},

"buy_open_conditions":{},

"sell_open_conditions":{},

"buy_close_conditions":{},

"sell_close_conditions":{},

"blacklist":{}, 

"oldPair":{},

"statice_size":True,

"currency":"USDT",

"dryrun_config" :{
    "dryrun_enable":True,
    "dryrun_wallet":1000
},

"timeframe" : 15, 

"dynamic_stoploss_ratio": 8,
"dynamic_take_profit_ratio" : 1.5,
"dynamic_trailing_number" : 0.3,
"trailing_stop_loss_params":{     

    "stopLoss":0.016,
    "stoploss_enable":True,
    "trailing_stop_enable": True,
    "trainling_number": 0.0001,
    "offset_enable": True,
    "offset_number": 0.001,

    "dynamic_stoploss_enable":False,
    "take_profit_enable":False,
    "dynamic_trailing_stoploss_offset_enable":True,
    "dynamic_trainling_number_enable":False
},

"telegram": {
    "telegram_enable" : False,
    "bot_token": "",
    "chat_id": ""
},

"run_bot_with_webapp":True,

"strategy":"testdb", 

"leverage":
{
    "leverage_number":"3"
},

"orders":{
    "open":"market",
    "close":"market",
    "stoploss":"market"
},

}