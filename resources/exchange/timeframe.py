from flask_restful import Resource
from flask_jwt import jwt_required

from models.exchanges.select_exchange import GetExchange


class Timeframe(Resource):

  @jwt_required()
  def get(self, botid):
        try:
            ex = GetExchange(botid)
            return {"timeframes" : ex.get_timefrmaes()}
        except Exception as e :
            print(f"{e}")
            return {'message': 'bot not found'}, 501
