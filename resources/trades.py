from email import parser
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.trades import Trades,ClosedTrades
from models.exchanges.kucoin import kucoin_pairs

class close_trades(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("limit",
        type=int,
        required=True,
        help="limit can't be empty"
    )

    # @jwt_required()
    def get(self, botid):
        """
        Get all closed positions in limit number 
        It is neccessary to send access token
        ---
        tags:
        - exchange data
        parameters:
          - in: path
            name: botid
            type: string
            required: true
          - in: path
            name: limit
            type: int
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
        data = close_trades.parser.parse_args()

        response = ClosedTrades.find_by_id(botid,data['limit'])
        # response = trades.find_by_name(botname,"real_tav_slope_atr_5_15min_2",data['limit']) #the right one is this
        # for row in ClosedTrades.query.filter(ClosedTrades.o_strategy=="real_tav_slope_atr_5_15min_2").order_by(ClosedTrades.o_close_date.desc()).limit(data['limit']):
        #   if row['o_exchange'] == 'kucoin':
        #     row['FormalName'] = kucoin_pairs.futures_pairs[row['o_pair']]
        if response:
          return {'message': [row.json_time() for row in ClosedTrades.query.filter(ClosedTrades.o_strategy==botid).order_by(ClosedTrades.o_close_date.desc()).limit(data['limit'])]} , 200
          return response.json() , 200
        return {'message': 'bot not found'}, 201

