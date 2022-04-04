from email import parser
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.bot_prop import Bot_propModel

class Bot_prop(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("exchange_name",
        type=str,
        required=True,
        help="An item with name exchange_name can't be empty"
    )
    parser.add_argument("apikey",
        type=str,
        required=True,
        help="An item with name apikey can't be empty"
    )
    parser.add_argument("apisecret",
        type=str,
        required=True,
        help="An item with name apisecret can't be empty"
    )
    parser.add_argument("apipass",
        type=str,
        required=True,
        help="An item with name apipass can't be empty"
    )
    parser.add_argument("market_type",
        type=str,
        required=True,
        help="An item with name market_type can't be empty"
    )
    @jwt_required()
    def get(self, botid):
        """
        Get bot characteristics
        It is neccessary to send access token
        ---
        tags:
        - bot
        parameters:
          - in: path
            botid: botid
            type: string
            required: true
        responses:
          200:
            description: A single user item
            schema:
              id: id
              properties:
                username:
                  type: string
                  description: The name of the user
        """
        bot = Bot_propModel.find_by_id(botid)
        if bot:
            return bot.json() , 200
        return {'message': 'Item not found'}, 201
    @jwt_required()
    def post(self, botid):
        """
        Register new bot
        It is neccessary to send access token
        ---
        tags:
        - bot
        parameters:
          - in: path
            botid: botid
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
        if Bot_propModel.find_by_id(botid):
            return {'message': "An item with name '{}' already exists.".format(botid)}, 400

        data = Bot_prop.parser.parse_args()

        bot = Bot_propModel(botid, **data)

        try:
            bot.save_to_db()
        except:
            return {"message": "An error occurred inserting the bot."}, 500

        return bot.json(), 200
    @jwt_required()
    def delete(self, botid):
        bot = Bot_propModel.find_by_name(botid)
        if bot:
            bot.delete_from_db()

        return {'message': 'bot deleted'}
    @jwt_required()
    def put(self, botid):
        data = Bot_prop.parser.parse_args()

        item = Bot_propModel.find_by_name(botid)

        if item is None:
            item = Bot_propModel(botid, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class BotsList(Resource):
    def get(self):
        return {'bot': [x.json() for x in Bot_propModel.query.all()]}
