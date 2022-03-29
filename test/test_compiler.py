from unittest import result
from numpy import integer
from indicators import Indicator,indicator_properties
import strategy_template as tp
received_ind={
    "BBANDS5" : { "IndicatorName": "BBANDS","params" : {"suffix":"5","CandlePricePoint" : "close", "timeperiod":5, "nbdevup":2, "nbdevdn":2, "matype":0}},
    "DEMA14" : { "IndicatorName": "DEMA","params" : {"suffix":"14","CandlePricePoint" : "close", "timeperiod":12}},
    "EMA12" : { "IndicatorName": "EMA","params" : {"suffix":"12","CandlePricePoint" : "close", "timeperiod":20}},
}
i=Indicator()
final_indicators=""
for ind in received_ind:
    # print(received_ind[ind]['IndicatorName'] )
    if received_ind[ind]['IndicatorName'] in indicator_properties:
        # print(received_ind[ind])
        
        for param in received_ind[ind]['params']:
            exec("i.{}='{}'".format(param,received_ind[ind]['params'][param]))
            print("i.{}='{}'".format(param,received_ind[ind]['params'][param]))
            # print(i.("{}".format(param)))
        i.rebuild_params()
        # print()
        # print("{}\n    {}".format(final_indicators,i.indicator_replacement[received_ind[ind]['IndicatorName']]))
        final_indicators= "{}\n    {}".format(final_indicators,i.indicator_replacement[received_ind[ind]['IndicatorName']])
print(f"final:{final_indicators}")






operators=[" ",">", "<",">=","<=","==","!="]

str1 = "(SLOPE_ATR#1>@trading_data.pair_dict_long[pair]['atr_slope_ratio'])and(SLOWK#3<40)or(SLOWD#2<SLOWD#1)and"

sentence = """((SLOPE_ATR#1>@trading_data.pair_dict_long[pair]['atr_slope_ratio'])and(SLOWK#3<40)or(SLOWD#2<SLOWD#1)and(SLOPE_SLOWK#0>5.67)or(SLOPE_SLOWD#0>2.75))"""

def get_number_after_sharp(str) :
    phrs=str.split("#",1)
    if int(phrs[1]) == 0 :
        return phrs[0],'last_row_index'
    elif int(phrs[1]) > 0:
        return phrs[0],f'last_row_index - {phrs[1]}'

def is_float(string):
  try :
    float(string) 
    return True 
  except ValueError:  # String is not a number
    return False

def detect_phrases(str):
    result = ''
    candlenumber=''
    if str is not None:

        for opr in operators:
            if opr in str:
                phrases=str.split(opr,1)
                # if phrases[0] in indicator_properties:
                phrases1,candlenumber1 = get_number_after_sharp(phrases[0].strip("("))        

                if is_float(phrases[1].strip(")")) or phrases[1].strip(")")[0] == '@':
                    print(phrases)
                    ph=phrases[1].strip(")")
                    ph=ph.strip("@")
                    result="df['{}'][{}] {} {}".format(phrases1,candlenumber1,opr,ph) 
                else:
                    phrases2 , candlenumber2 = get_number_after_sharp(phrases[1].strip(")"))
                    result="df['{}'][{}] {} df['{}'][{}]".format(phrases1,candlenumber1,opr,phrases2,candlenumber2)


                    # return indicators[detect_phrases(str)[1]],detect_phrases(str)[2]
                # else:
                #     return False,"error {} in {} in unknown".format(phrases[0],str)

                return True,result
        
        return False,"error there is no operator in {}".format(str)

    else:
        return False,"error phrase {} can not be empty".format(str)

def translate_phrases(str):
    if detect_phrases(str)[0]:
        if detect_phrases(str)[1] in indicator_properties:
            print(detect_phrases(str))
            # return indicators[detect_phrases(str)[1]],detect_phrases(str)[2]
        else:
            return False,"error {} in {} in unknown".format(detect_phrases(str)[1],str)
    else:
        return detect_phrases(str)[1]



# print(translate_phrases(str1))
# resp = detect_phrases(str1)
# if resp[0]:
#     open_buy="if ( {} ):".format(resp[1])
# initial_indicators = ""


 
def iter_split(sentence,lopr) -> str:
    resp = ""
    s_sent = sentence.split(lopr,sentence.count(lopr))
    for sent in s_sent:
        if resp:
            s = detect_phrases(sent)
            if s[0]:
                resp = "{} {} {}".format(resp,lopr,detect_phrases(sent)[1])
                # return open_buy
                # print(resp)
        else:
            s = detect_phrases(sent)
            if s[0]:
                resp = "{}".format(s[1])
                # print(resp)
    return resp  

def finalize_string_to_condition(str) -> str:
    return "if ({}):".format(str)
def detect_all_conditions(sentence):
    fstr=''
    andn=sentence.count("and")
    orn=sentence.count("or")
    if andn > 0 and orn > 0 :
        if andn >= orn:
            orsent = sentence.split("or")
            print(f"or sentences : {orsent}")
            for sent in orsent:
                andsent = iter_split(sent,"and")
                
                print(f"and sentence is {andsent}")
                if fstr:
                    fstr = "{} or ({})".format(fstr,andsent)
                else:
                    fstr = "({})".format(andsent)
        elif andn < orn:
            andsent = sentence.split("and")
            print(f"and sentences : {andsent}")
            for sent in andsent:
                orsent = iter_split(sent,"or")
                
                print(f"or sentence is {orsent}")
                if fstr:
                    fstr = "{} and ({})".format(fstr,orsent)
                else:
                    fstr = "({})".format(orsent)
        return fstr    
    elif orn:
        resp = iter_split(sentence,"or")
        return resp
    elif andn:
        resp=iter_split(sentence,"and")
        return resp
    
def get_condition_and_convert_to_str(sentence) -> str:
    resp=detect_all_conditions(sentence)
    # print(resp)
    resp=finalize_string_to_condition(resp)
    # print(resp)
    return resp

open_buy= get_condition_and_convert_to_str(sentence)
open_sell = "if df['rsi']<50 :"
close_buy = "if df['rsi']>100 :"
close_sell = "if df['rsi']>100 :"

f = open("strategy_test.py", "w")
f.write(tp.templ.format(final_indicators,open_buy,open_sell,close_buy,close_sell))
f.close()