import redis

redis_client = redis.Redis(
     host= 'localhost',
     port= '6379',
     db=0)

_bidPrice= "bestBidPrice"
_askPrice= "bestAskPrice"
_pairs = "pairs"

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

def getPairList() -> str:
     pairList = redis_client.get(_pairs)
     if pairList is not None:
          print(pairList)
          pairList = pairList.decode()
          return pairList
     print('empty pair list in redis')
     return None

#debug mode
if __name__ == "__main__":
     getPairList()
     updatePrice('BCHUSDTM', 1839.383)
     getPrice('BCHUSDTM')
     getAskPrice('BCHUSDTM')
