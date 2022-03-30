from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models import bot_config
from indicators.ta_indicators import Indicator, indicator_properties
from indicators import config_template
from models.bot_prop import Bot_propModel
import json




class Config(Resource):
    @jwt_required()
    def get(self,botname):
        """
        get all indicators
        It is neccessary to send access token
        ---
        tags:
        - indicators


        responses:          
          200:
            description: return all existed idicators

            schema:
              id: User
              properties:
                category:
                  type: string
                  description: technical indicators category                  


        """
        return {'configs': config_template.config } , 200  

class Indicators(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('indicators',
      required=True,
      action="append",
      help="This field cannot be blank."
  )


  @jwt_required()
  def get(self):
      """
      get all indicators
      It is neccessary to send access token
      ---
      tags:
      - indicators


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
            description: it returns last indicators number    
          returns:
            type: indicator return value
            description: it can be more than one element if it is one element shows real or inetegr and if it is more than one elements show return indicators
          descrption:
            type: string
            description: it describe what is the indicator
          params:
            type: json
            description: it is neccessary parameter for define a indicators and shows the default parameters 
          suffix:
            type: integer
            description: for each indicator we need suffix because it can be more than one type of one indicator 
                  
                                

                

      """

      return {'indicators': indicator_properties } , 200

  @jwt_required()
  def post(self, botid):

      """
      post indicators which is neccessary to define new strategy
      It is neccessary to send access token
      ---
      tags:
      - bot_config
      parameters:
        - in: path
          name: botid
          type: integer
          required: true
        - in: path
          indicators: indicators
          type: json
          required: true

      responses:
        200:
          description: indicators saved
          schema:
            id: User
            properties:
              name:
                type: string
                description: bot name

                

      """


      if Bot_propModel.find_by_id(botid):            
        data = Indicators.parser.parse_args()
        res=json.loads(bot_config.get_bot_config(botid))
        res['buy_open_conditions']= data['indicators'][0]
        print((res['buy_open_conditions']))
        bot_config.set_bot_config(botid,**res)


        bot_config.save_to_file(**data)
        return {"action" : "confirmed"}
        try:
            bot.save_to_db()
        except:
            return {"message": "An error occurred inserting the bot."}, 500
      else: 

        return {"message": "there is no such bot name."}, 400

class pair_whitelist(Resource):
    
    parser = reqparse.RequestParser()
    
    @jwt_required()
    def get(self, botname):
        """
        Get pair white list with its attributes
        It is neccessary to send access token
        ---
        tags:
        - bot_config
        parameters:
          - in: path
            name: botname
            type: string
            required: true
        responses:
          200:
            description: return all whitelist configs these configs can change per strategy
            schema:
              pairname: XBTUSDTM
              properties:
                pairname:
                  type: string
                  description: The name of the user
                  bot properties: Steven Wilson
        """
        pair_whitelist = bot_config.get_pair_whitelist(botname)
        if pair_whitelist:
            return {'pair_whitelist': pair_whitelist} , 200
        return {'message': 'Item not found'}, 201
    @jwt_required()
    def post(self, name):
      pass
      """
        Register new bot
        It is neccessary to send access token
        ---
        tags:
        - bot
        parameters:
          - in: path
            name: botname
            type: string
            required: true
          - in: path
            exchange_name: exchange_name
            type: string
            required: true
          - in: path
            apikey: apikey
            type: string
            required: true
          - in: path
            apisecret: apisecret
            type: string
            required: true
          - in: path
            apipass: apipass
            type: string
            required: true
          - in: path
            market_type: market_type
            type: string
            required: true
        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                name:
                  type: string
                  description: bot name
                  
                exchange_name:
                  type: string
                  description: exchange_name
                apikey:
                  type: string
                  description: apikey
                market type:
                  type: string
                  description: futures or spot
                  

        """
        # if Bot_propModel.find_by_name(name):
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # data = Bot_prop.parser.parse_args()

        # bot = Bot_propModel(name, **data)

        # try:
        #     bot.save_to_db()
        # except:
        #     return {"message": "An error occurred inserting the bot."}, 500

        # return bot.json(), 201
    @jwt_required()
    def delete(self, name):
      pass
        # bot = Bot_propModel.find_by_name(name)
        # if bot:
        #     bot.delete_from_db()

        # return {'message': 'bot deleted'}
    @jwt_required()
    def put(self, name):
      pass
        # data = Bot_prop.parser.parse_args()

        # item = Bot_propModel.find_by_name(name)

        # if item is None:
        #     item = Bot_propModel(name, **data)
        # else:
        #     item.price = data['price']

        # item.save_to_db()

        # return item.json()


# class BotsList(Resource):
#     def get(self):
#         return {'bot': [x.json() for x in Bot_propModel.query.all()]}
