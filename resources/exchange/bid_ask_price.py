from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.bot_prop import Bot_propModel


class LastBidprice(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pair',
        type=str,
        required=True,
        help="pair cannot be left blank!"
    )

    @jwt_required()
    def get(self, botid):

        """
        get last bid price
        It is neccessary to send access token
        ---
        tags:
        - exchange data
        parameters:
          - in: path
            name: pair
            type: string
            required: true

        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                pair:
                  type: string
                  description: like XBTUSDTM
                  
                LastBidPrice:
                  type: float
                  description: 42553.0
                  
        """
        bot = Bot_propModel.find_by_id(botid)
        data = LastBidprice.parser.parse_args()

        if bot.exchange_name=='kucoin':
            if bot.market_type == 'futures':            
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_realtimeticker(data['pair'])
                    return {'pair': data['pair'] , 'LastBidPrice' : response[0], 'FormalName' : response[1]} , 200
                except Exception as e:
                    return {'message': "{}".format(e)}, 201
        return {'message': 'bot not found'}, 201

class LastAskprice(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('pair',
        type=str,
        required=True,
        help="pair cannot be left blank!"
    )

    @jwt_required()
    def get(self, botid):
        """
        get last ask price
        It is neccessary to send access token
        ---
        tags:
        - exchange data
        parameters:
          - in: path
            name: pair
            type: string
            required: true
        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                pair:
                  type: string
                  description: like XBTUSDTM
                  
                LastAskPrice:
                  type: float
                  description: 42553.0                  
        """

        bot = Bot_propModel.find_by_id(botid)
        data = LastBidprice.parser.parse_args()

        if bot.exchange_name=='kucoin':
            if bot.market_type == 'futures':            
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_realtimeticker_ASK(data['pair'])
                    return {'pair': data['pair'] , 'LastAskPrice' : response[0] , 'FormalName' : response[1]} , 200
                except Exception as e:
                    return {'message': "{}".format(e)}, 201
        return {'message': 'Item not found'}, 201