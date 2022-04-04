import string
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.bot_prop import Bot_propModel





class OpenPositions(Resource):



    @jwt_required()
    def get(self, botid):
        """
        get open position list
        It is neccessary to send access token
        ---
        tags:
        - exchange data
        parameters:
          - in: path
            botid: botid
            type: string
            required: true

        responses:
          200:
            description: https://docs.kucoin.com/futures/#get-position-list

                  

        """
        bot = Bot_propModel.find_by_id(botid)
        # return {'message': " '{}' ".format(bot.exchange_name)}
        if bot.exchange_name=='kucoin':
            if bot.market_type =='futures':
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_open_positions()
                    # return jsonify(response)
                    # Symbol=response[0]['symbol']
                    return {'botid': botid , 'response' : response} , 200
                except Exception as e:
                    return {'message': "{}".format(e)}, 201
            else:
                return {'message': 'no such market {} defined'.format(bot.market_type)}, 201
        return {'message': 'Item not found'}, 201
    


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
            id: botid
            type: string
            required: true
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
        # return {'message': " '{}' ".format(bot.exchange_name)}
        data = LastBidprice.parser.parse_args()

        if bot.exchange_name=='kucoin':
            if bot.market_type == 'futures':            
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_realtimeticker(data['pair'])
                    # return jsonify(response)
                    # Symbol=response[0]['symbol']
                    return {'pair': data['pair'] , 'LastBidPrice' : response[0], 'FormalName' : response[1]} , 200
                except Exception as e:
                    return {'message': "{}".format(e)}, 201
        return {'message': 'Item not found'}, 201

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
            botid: botid
            type: string
            required: true
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
        # return {'message': " '{}' ".format(bot.exchange_name)}
        data = LastBidprice.parser.parse_args()

        if bot.exchange_name=='kucoin':
            if bot.market_type == 'futures':            
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_realtimeticker_ASK(data['pair'])
                    # return jsonify(response)
                    # Symbol=response[0]['symbol']
                    return {'pair': data['pair'] , 'LastAskPrice' : response[0] , 'FormalName' : response[1]} , 200
                except Exception as e:
                    return {'message': "{}".format(e)}, 201
        return {'message': 'Item not found'}, 201


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
        return {'message': 'Item not found'}, 201

class LastBalance(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('currency',
        type=str,
        required=True,
        help="currency cannot be left blank!"
    )

    @jwt_required()
    def get(self, botid):
        """
        get lastest balance base on sent currency 
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
            name: currency
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
        # return {'message': " '{}' ".format(bot.exchange_name)}
        data = LastBalance.parser.parse_args()

        if bot.exchange_name=='kucoin':
            if bot.market_type == 'futures':            
                from exchanges.kucoin_lib import kucoin_futures_ex
                try:
                    ex = kucoin_futures_ex(bot.apikey,bot.apisecret,bot.apipass,drydrun=False)
                    response = ex.get_overall_account(data['currency'])
                    # return jsonify(response)
                    # Symbol=response[0]['symbol']
                    return {'currency': data['currency'] , 'latest balance' : response} ,200
                except Exception as e:
                    return {'message': "{}".format(e)}, 201
        return {'message': 'Item not found'}, 201

