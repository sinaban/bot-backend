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

def get_pair_whitelist(botname) -> dict:
     pairList = json.loads(redis_client.get('bots'))
     if pairList[botname] is not None:
          # print(pairList)
          return pairList[botname]
     return None

#debug mode
if __name__ == "__main__":
     # getPairList()
     updatePrice('BCHUSDTM', 1839.383)
     getPrice('BCHUSDTM')
     getAskPrice('BCHUSDTM')
