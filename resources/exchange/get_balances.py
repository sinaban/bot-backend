from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.bot_prop import Bot_propModel
from models import bot_config

import json


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
        config= bot_config.get_bot_config(botid)
        if config:
          config = json.loads(config)
          if config['dryrun_config']['dryrun_enable'] == True:
            balance = bot_config.get_bot_balanceWallet(botid)
            if balance:
              balance = json.loads(balance)
              return {'currency': data['currency'] , 'latest balance' : balance} ,200
          else:
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
            return {'message': 'wrong exchange name'}, 201