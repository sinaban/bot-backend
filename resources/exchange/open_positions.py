from flask_restful import Resource
from flask_jwt import jwt_required

from models.exchanges.select_exchange import GetExchange
from models import bot_config,config_utils

import json

class OpenPositions(Resource):

    def get_dryrun_openpositions(self, botid):
        final_resp=[]
        resp =json.loads(bot_config.get_bot_pairPosition(botid))
        for pair in resp.keys():
            if resp[pair]['isOpen'] == True:
                final_resp.append(resp[pair])
            return {'botid': botid , 'response' : final_resp} , 200

    def get_open_position_from_exchange(self,botid):
        try:           
            ex = GetExchange(botid)
            response = ex.get_open_positions()
            return {'botid': botid , 'response' : response} , 200
        except Exception as e :
            print(f"{e}")
            return {'message': 'bot not found'}, 501

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
        if config_utils.is_bot_in_dryrun_mode(botid):
            self.get_dryrun_openpositions(botid)
        else:
            self.get_open_position_from_exchange(botid)


