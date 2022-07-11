from security import authenticate, identity
from resources.user import UserRegister,ReturnUser
from resources.bot_prop import Bot_prop, BotsList,Bot_prop_byid
from resources.exchange_data import OpenPositions,LastBidprice,LastAskprice,Klines,LastBalance,Timeframe
from resources.bot_config import pair_whitelist ,Indicators,TempConfig, Config ,Strategy, Commands,TempIndicators
from resources.trades import close_trades
from resources.reports import BotOverallReports,BotReports

def init_endpoints(api):

    api.add_resource(Bot_prop_byid, '/bot/<int:botid>')
    api.add_resource(Bot_prop, '/bot/<string:botname>')
    api.add_resource(BotReports, '/report/<int:botid>')
    api.add_resource(BotOverallReports, '/overallreport/<string:botids>')
    api.add_resource(BotsList, '/bots')

    api.add_resource(Timeframe, '/timeframes/<int:botid>')

    api.add_resource(OpenPositions, '/openpositions/<int:botid>')
    api.add_resource(LastBidprice, '/lastbidprice/<int:botid>')
    api.add_resource(LastAskprice, '/lastaskprice/<int:botid>')
    api.add_resource(Klines, '/klines/<int:botid>')
    api.add_resource(LastBalance,'/overallbalance/<int:botid>')

    api.add_resource(pair_whitelist, '/pairwhitelist/<int:botid>')
    api.add_resource(close_trades, '/closetrades/<int:botid>')
    api.add_resource(ReturnUser, '/auth/me')

    api.add_resource(Indicators, '/indicators/<int:botid>')
    api.add_resource(TempIndicators, '/tempindicators')

    api.add_resource(TempConfig, '/tempconfig')
    api.add_resource(Config, '/config/<int:botid>')
    api.add_resource(Strategy, '/strategy/<int:botid>')
    
    api.add_resource(Commands, '/commands/<int:botid>')

    api.add_resource(UserRegister, '/register')