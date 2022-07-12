from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.bot_prop import Bot_propModel


class Klines(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('pair',
        type=str,
        required=True,
        help="pair cannot be  blank!"
    )
    parser.add_argument('timeframe',
        type=int,
        required=True,
        help="timeframe cannot be blank!"
    )
    parser.add_argument('start_time',
        type=str,
        required=False,
        help="start_time!"
    )
    parser.add_argument('end_time',
        type=str,
        required=False,
        help="end_time!"
    )

    @jwt_required()
    def get(self, botid):
        """
        get klines
        It is neccessary to send access token
        ---
        tags:
        - exchange data
        parameters:
          - in: path
            botid: botid
            type: string
            required: true
          - in: path
            name: pair like ETHUSDT
            type: string
            required: true
          - in: path
            name: time frame multiply of 1 minutes
            type: int
            required: true
          - in: path
            name: from time must be epoch time
            type: string
            required: false
          - in: path
            name: end time must be epoch time
            type: string
            required: false

        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                pair:
                  type: string
                  description: like XBTUSDTM
                  
                klines:
                  type: float
                  description: time open high low close volume

                  

        """
        bot = Bot_propModel.find_by_id(botid)
        # return {'message': " '{}' ".format(bot.exchange_name)}
        data = Klines.parser.parse_args()

        if bot.exchange_name=='kucoin':
            if bot.market_type == 'futures':            
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_kline(data['pair'],data['timeframe'],data['start_time'],data['end_time'])
                    return {'pair': data['pair'] , 'FormalName' : response[0], 'klines' : response[1]} , 200
                except Exception as e:
                    return {'Exception': "{}".format(e)}, 201
        return {'message': ''}, 201