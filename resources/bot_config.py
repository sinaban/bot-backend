from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from numpy import empty
from models import bot_config
from indicators.ta_indicators import Indicator, indicator_properties
from indicators import config_template
from models.bot_prop import Bot_propModel
import json,ast
import requests

container_network = "http://127.17.0.1:7001"

class Commands(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('start',
      required=True,
      type = bool,
      help="This field cannot be blank."
  )
  parser.add_argument('stop',
      required=True,
      type = bool,
      help="This field cannot be blank."
  )
  parser.add_argument('stop_buy',
      required=True,
      type = bool,
      help="This field cannot be blank."
  )
  parser.add_argument('restart',
      required=True,
      type = bool,
      help="This field cannot be blank."
  )  
  @jwt_required()
  def get(self, botid):
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
      ret={}
      res=json.loads(bot_config.get_bot_commands(botid))
      if res:  
        ret['start'] = res['start']
        ret['stop'] = res['stop']
        ret['stop_buy'] = res['stop_buy']
        ret['restart'] = res['restart']
        # print(ret)
        return ret , 200
      else:
        return {"message":"could not find commands settings"},201

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
      try:
        bot = Bot_propModel.find_by_id(botid)
        if bot:            
          data = Commands.parser.parse_args()
          # res=json.loads(bot_config.get_bot_commands(botid))
          # print(data)
          res = {}
          if data:
            res['start']= data['start']
            res['stop']= data['stop']
            res['stop_buy']= data['stop_buy']
            res['restart']= data['restart']
            # print((res['buy_open_conditions']))
            bot_config.set_bot_commands(botid,**res)
            if data['start'] == True:
              endpoint = f"{container_network}/containers"
              names = requests.get(endpoint)
              # print(not f"b{botid}" in names.json()['container_names'])
              if  (not f"b{botid}" in names.json()['container_names']):#(not bot.json()['container_name']) or
                bot_config.setNewBot(False,bot.json()['id'],False)
                endpoint = f"{container_network}/runnew/{bot.json()['id']}"
                # print (endpoint)
                response = requests.post(endpoint)
                if response.json()['message']:
                  print(bot.json())
                  bot.container_name = bot.json()['id']
                  
                  bot.save_to_db()
                return {"message" : "action confirmed"}
              else: 
                return{"message" : "bot already started"}
          else:
            return {"message" : "action confirmed"}
        else: 

          return {"message": "there is no such bot name."}, 400
      except Exception as e:
        print(f'Exception in post commands :{e}')


        # bot_config.save_to_file(**data)
        


class Strategy(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('buy_open_conditions',
      required=True,
      type = str,
      help="This field cannot be blank."
  )
  parser.add_argument('sell_open_conditions',
      required=True,
      type = str,
      help="This field cannot be blank."
  )
  parser.add_argument('buy_close_conditions',
      required=True,
      type = str,
      help="This field cannot be blank."
  )
  parser.add_argument('sell_close_conditions',
      required=True,
      type = str,
      help="This field cannot be blank."
  )  
  @jwt_required()
  def get(self, botid):
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
      ret={}
      res=json.loads(bot_config.get_bot_config(botid))
      # print(type(res))
      
      ret['buy_open_conditions'] = res['buy_open_conditions']
      ret['buy_close_conditions'] = res['buy_close_conditions']
      ret['sell_open_conditions'] = res['sell_open_conditions']
      ret['sell_close_conditions'] = res['sell_close_conditions']
      # print(ret)
      return ret , 200

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
        data = Strategy.parser.parse_args()
        res=json.loads(bot_config.get_bot_config(botid))
        # print(data)
        res['buy_open_conditions']= data['buy_open_conditions']
        res['buy_close_conditions']= data['buy_close_conditions']
        res['sell_open_conditions']= data['sell_open_conditions']
        res['sell_close_conditions']= data['sell_close_conditions']
        # print((res['buy_open_conditions']))
        bot_config.set_bot_config(botid,**res)


        # bot_config.save_to_file(**data)
        return {"action" : "confirmed"}

      else: 

        return {"message": "there is no such bot name."}, 400

class Config(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('configs',
      required=True,
      action="append",
      help="This field cannot be blank."
  )
  @jwt_required()
  def get(self,botid):
      """
      get all configs for bot
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
      # print(json.loads(bot_config.get_bot_config(botid)))
      return {'configs': json.loads(bot_config.get_bot_config(botid)) } , 200  

  @jwt_required()
  def post(self,botid):
      """
      get all configs for bot
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
      if Bot_propModel.find_by_id(botid):            
        data = Config.parser.parse_args()
        # print(type((data['configs'][0])))
        new_config= ast.literal_eval(data['configs'][0])#converts str to dict
        if bot_config.get_bot_config(botid):
          config = json.loads(bot_config.get_bot_config(botid)) 
        else:
          config = config_template.config
        # print(type(config))
        # print(config)
        for key in new_config.keys():
          config[key]=new_config[key]

        bot_config.set_bot_config(botid,**config)

        return {"action" : "confirmed"}

class TempConfig(Resource):

  @jwt_required()
  def get(self):
        """
        get all configs
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
class TempIndicators(Resource):

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
      """                


      return {'indicators Template': indicator_properties } , 200    
class Indicators(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('indicators',
      required=True,
      action="append",
      help="This field cannot be blank."
  )


  @jwt_required()
  def get(self, botid):
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
      res=json.loads(bot_config.get_bot_config(botid))
      # print(type(ast.literal_eval(res['indicators'])))
      return {'indicators': ast.literal_eval(res['indicators']) } , 200

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
        res['indicators']= data['indicators'][0]
        # print((res['indicators']))
        bot_config.set_bot_config(botid,**res)


        # bot_config.save_to_file(**data)
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
    def get(self, botid):
        """
        Get pair white list with its attributes
        It is neccessary to send access token
        ---
        tags:
        - bot_config
        parameters:
          - in: path
            name: botid
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
        pair_whitelist = bot_config.get_pair_whitelist(botid)
        if pair_whitelist:
            return {'pair_whitelist': pair_whitelist} , 200
        return {'pair_whitelist': ''}, 201
    @jwt_required()
    def post(self, botid):
      pass
      """
        Register new bot
        It is neccessary to send access token
        ---
        tags:
        - bot
        parameters:
          - in: path
            name: botid
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
    def delete(self, botid):
      pass
        # bot = Bot_propModel.find_by_name(name)
        # if bot:
        #     bot.delete_from_db()

        # return {'message': 'bot deleted'}
    @jwt_required()
    def put(self, botid):
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
