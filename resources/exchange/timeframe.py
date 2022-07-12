from flask import jsonify
from flask_restful import Resource
from flask_jwt import jwt_required
from models.bot_prop import Bot_propModel


class Timeframe(Resource):

  @jwt_required()
  def get(self, botid):
    bot = Bot_propModel.find_by_id(botid)
      # return {'message': " '{}' ".format(bot.exchange_name)}
    if bot.exchange_name=='kucoin':         
      if bot.market_type =='futures':
        from models.exchanges.kucoin_lib import kucoin_futures_ex
        ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
        return {"timeframes" : ex.get_timefrmaes()}
      else:
        return {"message" : "could not find market type"}
    else:
      {"message" : "could not exchange name"}