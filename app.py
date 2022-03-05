from datetime import timedelta
from distutils.command.config import config
import os
from urllib.parse import  quote


from flask import Flask, send_from_directory
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS


from flasgger import Swagger


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.bot_prop import Bot_prop, BotsList
from resources.store import Store, StoreList
from resources.exchange_data import OpenPositions,LastBidprice,LastAskprice,Klines,LastBalance
from resources.bot_config import pair_whitelist
from resources.trades import close_trades


app = Flask(__name__)
CORS(app)


app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/bot_trades'% quote('ro0t!@#')
# os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# 'mysql+pymysql://root:%s@localhost/bot_trades'% quote('ro0t!@#')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sina12345678'
api = Api(app)
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'bot',
            "route": '/bot.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app,
    template={
        "info": {
            "title": "backend api",
            "version": "1.0",
        },

    },config=swagger_config
)


jwt = JWT(app, authenticate, identity)  # /auth
app.config['JWT_EXPIRATION_DELTA'] =timedelta(minutes=60)

from db import db
db.init_app(app)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(Bot_prop, '/bot/<string:name>')
api.add_resource(BotsList, '/bots')
api.add_resource(OpenPositions, '/openpositions/<string:botname>')
api.add_resource(LastBidprice, '/lastbidprice/<string:botname>')
api.add_resource(LastAskprice, '/lastaskprice/<string:botname>')
api.add_resource(Klines, '/klines/<string:botname>')
api.add_resource(LastBalance,'/overallbalance/<string:botname>')
api.add_resource(pair_whitelist, '/pairwhitelist/<string:botname>')
api.add_resource(close_trades, '/closetrades/<string:botname>')


api.add_resource(UserRegister, '/register')

if __name__ == '__main__':


    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=7000)