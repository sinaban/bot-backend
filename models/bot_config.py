import redis
import json

redis_client = redis.Redis(
     host= 'localhost',
     port= '6379',
     db=0)

_bidPrice= "bestBidPrice"
_askPrice= "bestAskPrice"
_pairs = "pairs"

def save_to_file(**kwargs):
     # pr=json.load(kwargs)
     f = open("test.py", "w")
     f.write(str(kwargs))
     f.close()

def updatePrice(pair, price) -> None:
     redis_client.hset(pair, _bidPrice, str(price))

def updateAskPrice(pair, price) -> None:
     redis_client.hset(pair, _askPrice, str(price))

def getPrice(pair) -> float:
     price = redis_client.hget(pair, _bidPrice)
     price = price.decode()
     if price is not None:
          return (float)(price)
     return None


def getAskPrice(pair) -> float:
     price = redis_client.hget(pair, _askPrice)
     price = price.decode()
     if price is not None:
          return (float)(price)
     return None

def get_pair_whitelist(botid) -> dict:
     # resp = redis_client.hget("bots:config",botid)     
     pairList = json.loads(redis_client.hget("bots:config",botid))
     if pairList['pair_whitelist'] is not None:
          # print(pairList)
          return pairList['pair_whitelist']
     return None

def set_indicators(botname) -> dict:
     redis_client.hmset()
     pairList = json.loads(redis_client.get('bots'))
     if pairList[botname] is not None:
          # print(pairList)
          return pairList[botname]
     return None

def get_bot_config(botid) -> dict :
     resp = redis_client.hget("bots:config",botid)     
     return resp

def set_bot_config(botid,**kwargs) -> bool :
     resp = redis_client.hset("bots:config",botid,json.dumps(kwargs))     
     return resp

def get_bot_commands(botid) -> dict :
     resp = redis_client.hget("bots:command",botid)     
     return resp

def set_bot_commands(botid,**kwargs) -> bool :
     resp = redis_client.hset("bots:command",botid,json.dumps(kwargs))     
     return resp

def get_bot_status(botid) -> dict :
     resp = redis_client.hget("bots:status",botid)     
     return resp
def set_bot_status(botid,status) -> bool :
     resp = redis_client.hset("bots:status",botid,status)     
     return resp

def set_bot_pairPosition(botid,**kwargs) -> bool :
     resp = redis_client.hset("bots:pairPosition",botid,json.dumps(kwargs))     
     return resp

def get_bot_pairPosition(botid) -> dict :
     resp = redis_client.hget("bots:pairPosition",botid)     
     return resp
def get_bot_balanceWallet(botid) -> bool :
     resp = redis_client.hget("bots:balanceWallet",botid)     
     return resp
#debug mode
if __name__ == "__main__":
     # getPairList()
     updatePrice('BCHUSDTM', 1839.383)
     getPrice('BCHUSDTM')
     getAskPrice('BCHUSDTM')
