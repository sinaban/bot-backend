from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models import bot_config
from models.indicators.ta_indicators import Indicator, indicator_properties


from resources.reports.generate_all_reports import BotReport


class BotReports(Resource):
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
        # print(type(res))
        
        return {"message" : (res)}

        
class BotOverallReports(Resource):

    @jwt_required()
    def get(self, botids):
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
        
        bots=botids.split(",")        
        final_res=[]
        for id in bots:
          res= BotReport.get_bot_reports(id, perday=False)
          final_res.append(res)
        return {"message" : (final_res)}