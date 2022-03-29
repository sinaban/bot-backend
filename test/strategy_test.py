
from pandas import DataFrame
import talib
import ta
import trading_data
import numpy as np

radians_to_degrees=180/3.14159265359
def intial_indicator(df)->DataFrame:
    
    df["UPPERBAND5"], df["MIDDLEBAND5"], df["LOWERBAND5"] = talib.BBANDS(df["close"], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    df["DEMA14"] =  talib.DEMA(df["close"], timeperiod=12)
    df["EMA12"] =  talib.EMA(df["close"], timeperiod=20)
    return df
def open_buy_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    if ((df['SLOPE_ATR'][last_row_index - 1] > trading_data.pair_dict_long[pair]['atr_slope_ratio'] and df['SLOWK'][last_row_index - 3] < 40) or (df['SLOWD'][last_row_index - 2] < df['SLOWD'][last_row_index - 1] and df['SLOPE_SLOWK'][last_row_index] > 5.67) or (df['SLOPE_SLOWD'][last_row_index] > 2.75)):
        return True
    else:
        return False
def open_sell_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    if df['rsi']<50 :
        return True
    else:
        return False
def close_buy_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    return False #if no condition for close
    if df['rsi']>100 :
        return True
    else:
        return False
def close_sell_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    return False #if no condition for close
    if df['rsi']>100 :
        return True
    else:
        return False


