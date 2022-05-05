from datetime import timedelta
from urllib.parse import  quote


from flask import Flask, send_from_directory
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS


from flasgger import Swagger


from security import authenticate, identity
from resources.user import UserRegister,ReturnUser
from resources.item import Item, ItemList
from resources.bot_prop import Bot_prop, BotsList,Bot_prop_byid
from resources.store import Store, StoreList
from resources.exchange_data import OpenPositions,LastBidprice,LastAskprice,Klines,LastBalance
from resources.bot_config import pair_whitelist ,Indicators,TempConfig, Config ,Strategy, Commands,TempIndicators
from resources.trades import close_trades
from resources.reports import BotOverallReports,BotReports


app = Flask(__name__)
CORS(app)


app.config['DEBUG'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/bot_trades'% quote('ro0t!@#')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@mysql/bot_trades'% quote('ro0t!@#')


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

api.add_resource(Bot_prop_byid, '/bot/<int:botid>')
api.add_resource(Bot_prop, '/bot/<string:botname>')
api.add_resource(BotsList, '/bots')
api.add_resource(OpenPositions, '/openpositions/<int:botid>')
api.add_resource(LastBidprice, '/lastbidprice/<int:botid>')
api.add_resource(LastAskprice, '/lastaskprice/<int:botid>')
api.add_resource(Klines, '/klines/<int:botid>')
api.add_resource(LastBalance,'/overallbalance/<int:botid>')
api.add_resource(pair_whitelist, '/pairwhitelist/<int:botid>')
api.add_resource(close_trades, '/closetrades/<int:botid>')
api.add_resource(ReturnUser, '/auth/me')
api.add_resource(Indicators, '/indicators/<int:botid>')
api.add_resource(TempIndicators, '/tempindicators')
api.add_resource(TempConfig, '/tempconfig')
api.add_resource(Config, '/config/<int:botid>')
api.add_resource(Strategy, '/strategy/<int:botid>')
api.add_resource(Commands, '/commands/<int:botid>')
api.add_resource(BotReports, '/report/<int:botid>')
api.add_resource(BotOverallReports, '/overallreport/<string:botids>')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':


    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(host="0.0.0.0", port=7000)#for docker
    # app.run( port=7002)#for local