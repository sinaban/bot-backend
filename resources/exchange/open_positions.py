import string
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.bot_prop import Bot_propModel
from models import bot_config
import json

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
    if bot_config.get_bot_config(botid):
      config = json.loads(bot_config.get_bot_config(botid))
      if config['dryrun_config']['dryrun_enable']==True:
        final_resp=[]
        resp =json.loads(bot_config.get_bot_pairPosition(botid))
        for pair in resp.keys():
          if resp[pair]['isOpen'] == True:
            final_resp.append(resp[pair])
        return {'botid': botid , 'response' : final_resp} , 200
      elif bot.exchange_name=='kucoin':
          
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
    return {'message': 'config not found'}, 201