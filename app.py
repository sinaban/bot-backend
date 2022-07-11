from datetime import timedelta
from urllib.parse import  quote

from flask import Flask, send_from_directory
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from swagger_config import swagger_config

from endpoints import init_endpoints


app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/bot_trades'% quote('ro0t!@#')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@mysql/bot_trades'% quote('ro0t!@#')

swagger = swagger_config(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Ax365lprtGHy'
jwt = JWT(app, authenticate, identity)  
app.config['JWT_EXPIRATION_DELTA'] =timedelta(minutes=60)

from db import db
db.init_app(app)

api = Api(app)

init_endpoints(api)

if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run( port=7000)
