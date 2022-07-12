from logging import exception
from models.bot_prop import BotPropModel
from models.bot_validation import validate_bot_by_id,NoBotError


class NotIdentifiedExchangeError(ValueError):
    pass

identified_exchanges = [
    "kucoin_futures"
]

class GetExchange():
    def __init__(self, botid) -> None:
        self.botid = botid
        self.find_exchange_name()

    def is_exchange_identified(self):
        if not self.bot.exchange_name in identified_exchanges:
            raise NotIdentifiedExchangeError(f"{self.bot.exchange_name} not identified" )

    def find_exchange_name(self):
        try:
            self.bot = validate_bot_by_id(self.botid)
        except NoBotError as e:
            print(f"{e}")
            return None

    def get_exchange_properties(self):
        try:
            self.is_exchange_identified()
            if self.bot.exchange_name == "kucoin_futures":
                from exchanges.kucoin.kucoin_lib import KucoinFutures
                return KucoinFutures(self.bot.apikey, self.bot.apisecret, self.bot.apipass)

        except NotIdentifiedExchangeError as e:
            print(f"{e}")



    
        



