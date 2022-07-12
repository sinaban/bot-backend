from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models import bot_config
from models.exchanges.select_exchange import GetExchange

from models import bot_config,config_utils



import json


class LastBalance(Resource):


    parser = reqparse.RequestParser()
    parser.add_argument('currency',
        type=str,
        required=True,
        help="currency cannot be left blank!"
    )

    def is_balance_available(self,botid):
        balance = bot_config.get_bot_balanceWallet(botid)
        if not balance:
            raise ValueError("Balance value is not available")

    def get_balance_in_dryrun(self, botid):
        try:
            self.is_balance_available(botid)
            balance = json.loads(balance)
            return {'currency': self.data['currency'] , 'latest balance' : balance} ,200
        except ValueError as e:
            return {'message': f'balance is not available {e}'}, 501

    def get_balance_from_exchange(self,botid):
        try:
            ex = GetExchange(botid)
            response = ex.get_overall_account(self.data['currency'])
            return {'currency': self.data['currency'] , 'latest balance' : response}, 200
        except Exception as e :
            print(f"{e}")
            return {'message': f'Exception in getting data from Exchange {e}'}, 501


    @jwt_required()
    def get(self, botid):
        self.data = LastBalance.parser.parse_args()

        if config_utils.is_bot_in_dryrun_mode(botid):
            self.get_balance_in_dryrun(botid)
        else:
            self.get_balance_from_exchange(botid)