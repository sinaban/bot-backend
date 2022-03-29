
templ='''
from pandas import DataFrame
import talib
import ta
import trading_data
import numpy as np

radians_to_degrees=180/3.14159265359
def intial_indicator(df)->DataFrame:
    {}
    return df
def open_buy_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    {}
        return True
    else:
        return False
def open_sell_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    {}
        return True
    else:
        return False
def close_buy_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    return False #if no condition for close
    {}
        return True
    else:
        return False
def close_sell_condition(df,pair) -> bool:
    last_row_index= len(df.index)-1
    return False #if no condition for close
    {}
        return True
    else:
        return False


'''
'''
upperband, middleband, lowerband = BBANDS(close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
real = DEMA(close, timeperiod=30)
real = EMA(close, timeperiod=30)
real = HT_TRENDLINE(close)
real = KAMA(close, timeperiod=30)
real = MA(close, timeperiod=30, matype=0)
mama, fama = MAMA(close, fastlimit=0, slowlimit=0)
real = MAVP(close, periods, minperiod=2, maxperiod=30, matype=0)
real = MIDPOINT(close, timeperiod=14)
real = MIDPRICE(high, low, timeperiod=14)
real = SAR(high, low, acceleration=0, maximum=0)
real = SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
real = SMA(close, timeperiod=30)
real = T3(close, timeperiod=5, vfactor=0)
real = TEMA(close, timeperiod=30)
real = TRIMA(close, timeperiod=30)
real = WMA(close, timeperiod=30)

real = ADX(high, low, close, timeperiod=14)
real = ADXR(high, low, close, timeperiod=14)
real = APO(close, fastperiod=12, slowperiod=26, matype=0)
aroondown, aroonup = AROON(high, low, timeperiod=14)
real = AROONOSC(high, low, timeperiod=14)
real = BOP(open, high, low, close)
real = CCI(high, low, close, timeperiod=14)
real = CMO(close, timeperiod=14)
real = DX(high, low, close, timeperiod=14)
macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
macd, macdsignal, macdhist = MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
macd, macdsignal, macdhist = MACDFIX(close, signalperiod=9)
real = MFI(high, low, close, volume, timeperiod=14)
real = MINUS_DI(high, low, close, timeperiod=14)
real = MINUS_DM(high, low, timeperiod=14)
real = MOM(close, timeperiod=10)
real = PLUS_DI(high, low, close, timeperiod=14)
real = PLUS_DM(high, low, timeperiod=14)
real = PPO(close, fastperiod=12, slowperiod=26, matype=0)
real = ROC(close, timeperiod=10)
real = ROCP(close, timeperiod=10)
real = ROCR(close, timeperiod=10)
real = ROCR100(close, timeperiod=10)
real = RSI(close, timeperiod=14)
slowk, slowd = STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
fastk, fastd = STOCHF(high, low, close, fastk_period=5, fastd_period=3, fastd_matype=0)
fastk, fastd = STOCHRSI(close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
real = TRIX(close, timeperiod=30)
real = ULTOSC(high, low, close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
real = WILLR(high, low, close, timeperiod=14)

Volume Indicator Functions
real = AD(high, low, close, volume)
real = ADOSC(high, low, close, volume, fastperiod=3, slowperiod=10)
real = OBV(close, volume)

Volatility Indicator Functions
real = ATR(high, low, close, timeperiod=14)
real = NATR(high, low, close, timeperiod=14)
real = TRANGE(high, low, close)

Price Transform Functions
real = AVGPRICE(open, high, low, close)
real = MEDPRICE(high, low)
real = TYPPRICE(high, low, close)
real = WCLPRICE(high, low, close)

Cycle Indicator Functions
real = HT_DCPERIOD(close)
real = HT_DCPHASE(close)
inphase, quadrature = HT_PHASOR(close)
sine, leadsine = HT_SINE(close)
integer = HT_TRENDMODE(close)

Pattern Recognition Functions
integer = CDL2CROWS(open, high, low, close)
integer = CDL3BLACKCROWS(open, high, low, close)
integer = CDL3INSIDE(open, high, low, close)
integer = CDL3LINESTRIKE(open, high, low, close)
integer = CDL3OUTSIDE(open, high, low, close)
integer = CDL3STARSINSOUTH(open, high, low, close)
integer = CDL3WHITESOLDIERS(open, high, low, close)
integer = CDLABANDONEDBABY(open, high, low, close, penetration=0)
integer = CDLADVANCEBLOCK(open, high, low, close)
integer = CDLBELTHOLD(open, high, low, close)
integer = CDLBREAKAWAY(open, high, low, close)
integer = CDLCLOSINGMARUBOZU(open, high, low, close)
integer = CDLCONCEALBABYSWALL(open, high, low, close)
integer = CDLCOUNTERATTACK(open, high, low, close)
integer = CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
integer = CDLDOJI(open, high, low, close)
integer = CDLDOJISTAR(open, high, low, close)
integer = CDLDRAGONFLYDOJI(open, high, low, close)
integer = CDLENGULFING(open, high, low, close)
integer = CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
integer = CDLEVENINGSTAR(open, high, low, close, penetration=0)
integer = CDLGAPSIDESIDEWHITE(open, high, low, close)
integer = CDLGRAVESTONEDOJI(open, high, low, close)
integer = CDLHAMMER(open, high, low, close)
integer = CDLHANGINGMAN(open, high, low, close)
integer = CDLHARAMI(open, high, low, close)
integer = CDLHARAMICROSS(open, high, low, close)
integer = CDLHIGHWAVE(open, high, low, close)
integer = CDLHIKKAKE(open, high, low, close)
integer = CDLHIKKAKEMOD(open, high, low, close)
integer = CDLHOMINGPIGEON(open, high, low, close)
integer = CDLIDENTICAL3CROWS(open, high, low, close)
integer = CDLINNECK(open, high, low, close)
integer = CDLINVERTEDHAMMER(open, high, low, close)
integer = CDLKICKING(open, high, low, close)
integer = CDLKICKINGBYLENGTH(open, high, low, close)
integer = CDLLADDERBOTTOM(open, high, low, close)
integer = CDLLONGLEGGEDDOJI(open, high, low, close)
integer = CDLLONGLINE(open, high, low, close)
integer = CDLMARUBOZU(open, high, low, close)
integer = CDLMATCHINGLOW(open, high, low, close)
integer = CDLMATHOLD(open, high, low, close, penetration=0)
integer = CDLMORNINGDOJISTAR(open, high, low, close, penetration=0)
integer = CDLMORNINGSTAR(open, high, low, close, penetration=0)
integer = CDLONNECK(open, high, low, close)
integer = CDLPIERCING(open, high, low, close)
integer = CDLRICKSHAWMAN(open, high, low, close)
integer = CDLRISEFALL3METHODS(open, high, low, close)
integer = CDLSEPARATINGLINES(open, high, low, close)
integer = CDLSHOOTINGSTAR(open, high, low, close)
integer = CDLSHORTLINE(open, high, low, close)
integer = CDLSPINNINGTOP(open, high, low, close)
integer = CDLSTALLEDPATTERN(open, high, low, close)
integer = CDLSTICKSANDWICH(open, high, low, close)
integer = CDLTAKURI(open, high, low, close)
integer = CDLTASUKIGAP(open, high, low, close)
integer = CDLTHRUSTING(open, high, low, close)
integer = CDLTRISTAR(open, high, low, close)
integer = CDLUNIQUE3RIVER(open, high, low, close)
integer = CDLUPSIDEGAP2CROWS(open, high, low, close)
integer = CDLXSIDEGAP3METHODS(open, high, low, close)

Statistic Functions
real = BETA(high, low, timeperiod=5)
real = CORREL(high, low, timeperiod=30)
real = LINEARREG(close, timeperiod=14)
real = LINEARREG_ANGLE(close, timeperiod=14)
real = LINEARREG_INTERCEPT(close, timeperiod=14)
real = LINEARREG_SLOPE(close, timeperiod=14)
real = STDDEV(close, timeperiod=5, nbdev=1)
real = TSF(close, timeperiod=14)
real = VAR(close, timeperiod=5, nbdev=1)

Math Transform Functions
real = ACOS(close)
real = ASIN(close)
real = ATAN(close)
real = CEIL(close)
real = COS(close)
real = COSH(close)
real = EXP(close)
real = FLOOR(close)
real = LN(close)
real = LOG10(close)
real = SIN(close)
real = SINH(close)
real = SQRT(close)
real = TAN(close)
real = TANH(close)

Math Operator Functions
real = ADD(high, low)
real = DIV(high, low)
real = MAX(close, timeperiod=30)
integer = MAXINDEX(close, timeperiod=30)
real = MIN(close, timeperiod=30)
integer = MININDEX(close, timeperiod=30)
min, max = MINMAX(close, timeperiod=30)
minidx, maxidx = MINMAXINDEX(close, timeperiod=30)
real = MULT(high, low)
real = SUB(high, low)
real = SUM(close, timeperiod=30)


'''


indicators={
    "ُSTOCHASTIC" : "df['slowk'], df['slowd'] = talib.STOCHF(high=df['high'], low=df['low'], close=df['close'],fastk_period={fastk_period}, fastd_period={}, fastd_matype={})",
    'BBANDS' : "df['upperband'], df['middleband'], df['lowerband'] = talib.BBANDS(df['close'], timeperiod={}, nbdevup={}, nbdevdn={}, matype={})",
    'DEMA' : "df['DEMA'] = talib.DEMA(df['close'] , timeperiod={})",
    'EMA' :  "df['EMA'] = talib.EMA(df['close'],timeperiod={})",
    'HT_TRENDLINE' : "df['HT_TRENDLINE'] = talib.HT_TRENDLINE(df['close'])",
    'KAMA' : "df['KAMA'] = talib.KAMA(df['close'],timeperiod={})",
    'MA' : "df['MA'] = talib.MA(df['close'],timeperiod={}, matype={})",
    'mama' : "df['mama'], df['fama'] = talib.MAMA(df['close'],fastlimit={}, slowlimit={})",
    'MAVP' : "df['MAVP'] = talib.MAVP(df['close'],periods, minperiod={}, maxperiod={}, matype={})",
    'MIDPOINT' : "df['MIDPOINT'] = talib.MIDPOINT(df['close'],timeperiod={})",
    'MIDPRICE' : "df['MIDPRICE'] = talib.MIDPRICE(df['high'], df['low'], timeperiod={})",
    'SAR' : "df['SAR'] = talib.SAR(df['high'], df['low'], acceleration={}, maximum={})",
    'SAREXT' : "df['SAREXT'] = talib.SAREXT(df['high'], df['low'], startvalue={}, offsetonreverse={}, accelerationinitlong={}, accelerationlong={}, accelerationmaxlong={}, accelerationinitshort={}, accelerationshort={}, accelerationmaxshort={})",
    'SMA' : "df['SMA'] = talib.SMA(df['close'],timeperiod={})",
    'T3' : "df['T3'] = talib.T3(df['close'],timeperiod=5, vfactor={})",
    'TEMA' : "df['TEMA'] = talib.TEMA(df['close'],timeperiod={})",
    'TRIMA' : "df['TRIMA'] = talib.TRIMA(df['close'],timeperiod={})",
    'WMA' : "df['WMA'] = talib.WMA(df['close'],timeperiod={})",

    'ADX' : "df['ADX'] = talib.ADX(df['high'], df['low'], df['close'], timeperiod={})",
    'ADXR' : "df['ADXR'] = talib.ADXR(df['high'], df['low'], df['close'], timeperiod={})",
    'APO' : "df['APO'] = talib.APO(df['close'], fastperiod={}, slowperiod={}, matype={})",
    'AROON' : "df['aroondown'], df['aroonup'] = talib.AROON(df['high'], df['low'], timeperiod={})",
    'AROONOSC' : "df['AROONOSC'] = talib.AROONOSC(df['high'], df['low'], timeperiod={})",
    'BOP' : "df['BOP'] = talib.BOP(open, df['high'], df['low'], df['close'])",
    'CCI' : "df['CCI'] = talib.CCI(df['high'], df['low'], df['close'], timeperiod={})",
    'CMO' : "df['CMO'] = talib.CMO(df['close'], timeperiod={})",
    'DX' : "df['DX'] = talib.DX(df['high'], df['low'], df['close'], timeperiod={})",
    'MACD' : "df['macd'],df['macdsignal'], df['macdhist'] = talib.MACD(df['close'], fastperiod={}, slowperiod={}, signalperiod={})",
    'MACDEXT' : "df['macd'], df['macdsignal'], df['macdhist'] = talib.MACDEXT(df['close'], fastperiod={}, fastmatype={}, slowperiod={}, slowmatype={}, signalperiod={}, signalmatype={})",
    'MACDFIX' : "df['macd'], df['macdsignal'], df['macdhist'] = talib.MACDFIX(df['close'], signalperiod={})",
    'MFI' : "df['MFI'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod={})",
    'MINUS_DI' : "df['MINUS_DI'] = talib.MINUS_DI(df['high'], df['low'], df['close'], timeperiod={})",
    'MINUS_DM' : "df['MINUS_DM'] = talib.MINUS_DM(df['high'], df['low'], timeperiod={})",
    'MOM' : "df['MOM'] = talib.MOM(df['close'], timeperiod={})",
    'PLUS_DI' : "df['PLUS_DI'] = talib.PLUS_DI(df['high'], df['low'], df['close'], timeperiod={})",
    'PLUS_DM' : "df['PLUS_DM'] = talib.PLUS_DM(df['high'], df['low'], timeperiod={})",
    'PPO' : "df['PPO'] = talib.PPO(df['close'], fastperiod={}, slowperiod={}, matype={})",
    'ROC' : "df['ROC'] = talib.ROC(df['close'], timeperiod={})",
    'ROCP' : "df['ROCP'] = talib.ROCP(df['close'], timeperiod={})",
    'ROCR' : "df['ROCR'] = talib.ROCR(df['close'], timeperiod={})",
    'ROCR100' : "df['ROCR100'] = talib.ROCR100(df['close'], timeperiod={})",
    'RSI' : "df['RSI'] = talib.RSI(df['close'], timeperiod={})",
    'STOCH' : "df['STOCHslowk'], df['STOCHslowd'] = talib.STOCH(df['high'], df['low'], df['close'], fastk_period={}, slowk_period={}, slowk_matype={}, slowd_period={}, slowd_matype={})",
    'STOCHF' : "df['STOCHFfastk'], df['STOCHFfastd'] = talib.STOCHF(df['high'], df['low'], df['close'], fastk_period={}, fastd_period={}, fastd_matype={})",
    'STOCHRSI' : "df['STOCHRSIfastk'], df['STOCHRSIfastd'] = talib.STOCHRSI(df['close'], timeperiod={}, fastk_period={}, fastd_period={}, fastd_matype={})",
    'TRIX' : "df['TRIX'] = talib.TRIX(df['close'], timeperiod={})",
    'ULTOSC' : "df['ULTOSC'] = talib.ULTOSC(df['high'], df['low'], df['close'], timeperiod1={}, timeperiod2={}, timeperiod3={})",
    'WILLR' : "df['WILLR'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod={})",


}
if __name__ == '__main__':# this routin is for sepration and edit multiple line indicator and conert to json
    str = "real = DEMA(close, timeperiod=30)"

    f = open("talib_indicators.py", "r")
    cont=f.read()
    lns=cont.split("\n",157)
    print(lns[2])
    # f.write(tp.templ.format(initial_indicators,open_buy,open_sell,close_buy,close_sell))
    f.close()
    gium='"'
    opr="("
    strlist=""
    for line in lns:
        if opr in line:
            phrases=line.split(opr,1)
            # print(phrases)
            ph= phrases[0].split(" = ",1)
            
            if ph[0] in ['real','integer']:
                str1 = "'{}' : 'df[{}{}{}] = {}'".format(ph[1],gium,ph[1],gium,line.split("=",1)[1])
                strlist= "{},\n{}".format(strlist,str1)
                # print(str1)  
                # 
            else: 
                strlist= "{},\n{}{}{}".format(strlist,"'",line,"'")
                                
    f = open("talib_indicators_edited.py", "w")

    f.write("{}".format(strlist))
    f.close()