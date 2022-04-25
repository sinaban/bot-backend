from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models import bot_config
from indicators.ta_indicators import Indicator, indicator_properties
from indicators import config_template
from models.bot_prop import Bot_propModel
from models.reports import BotReport
import json,ast

class BotOverallReports(Resource):
    @jwt_required()
    def get(self, botid):
        """
      get all report for bot
      It is neccessary to send access token
      ---
      tags:
      - reports


      responses:          
        200:
          description: return all existed idicators

        schema:
          id: properties
          properties:
          category:
            type: string
            description: technical indicators category                  
          function:
            type: json
            description: mathematical function which will apply on indicators
          CandleNumber:
            type: integer

        """
        res= BotReport.get_bot_reports(botid)
        # print(res)
        
        return {"message" : res}