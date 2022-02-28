from email import parser
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.trades import trades

class close_trades(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("limit",
        type=int,
        required=True,
        help="limit can't be empty"
    )

    # @jwt_required()
    def get(self, botname):
        """
        Get all closed positions in limit number 
        It is neccessary to send access token
        ---
        tags:
        - exchange data
        parameters:
          - in: path
            name: botname
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

        response = trades.find_by_name("real_tav_slope_atr_5_15min_2",data['limit'])
        # response = trades.find_by_name(botname,"real_tav_slope_atr_5_15min_2",data['limit']) #the right one is this

        if response:
          return {'message': [row.json() for row in trades.query.filter((trades.strategy=="real_tav_slope_atr_5_15min_2") & (trades.is_open ==0)).order_by(trades.id.desc()).limit(data['limit'])]} , 200
          return response.json() , 200
        return {'message': 'Item not found'}, 404

