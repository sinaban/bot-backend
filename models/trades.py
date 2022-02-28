from db import db
import json
import datetime

class trades(db.Model):
    __tablename__ = 'trades'

    id = db.Column(db.Integer, primary_key=True)
    pair = db.Column(db.String(50))
    oid_close = db.Column(db.String(50)) 
    oid_open = db.Column(db.String(50))
    open_date = db.Column(db.DateTime)
    close_date = db.Column(db.DateTime)
    open_price = db.Column(db.Float)
    close_price = db.Column(db.Float)
    profit = db.Column(db.Float)
    amount = db.Column(db.Float)
    close_reason = db.Column(db.String(50))
    is_open = db.Column(db.Integer)
    symbol = db.Column(db.String(50)) 
    exchange = db.Column(db.String(50)) 
    profit_percent = db.Column(db.Float)
    take_profit = db.Column(db.Float)
    dynamic_stoploss = db.Column(db.Float)
    strategy = db.Column(db.String(50))

    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')

    def __init__(self, pair, oid_close, oid_open,open_date,close_date,open_price,close_price,profit,amount,close_reason,is_open,symbol,exchange
    ,profit_percent,take_profit,dynamic_stoploss,strategy):
        self.pair = pair
        self.oid_close = oid_close
        self.oid_open = oid_open
        self.open_date = open_date
        self.close_date = close_date
        self.open_price = open_price
        self.close_price = close_price
        self.profit = profit
        self.amount = amount
        self.close_reason = close_reason
        self.is_open = is_open
        self.symbol = symbol
        self.exchange = exchange
        self.profit_percent = profit_percent
        self.take_profit = take_profit
        self.dynamic_stoploss = dynamic_stoploss
        self.strategy = strategy
    def defaultconverter(self,o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    def json(self):
        return {
            "pair" : self.pair,
            "oid_close" : self.oid_close,
            "oid_open" : self.oid_open, 
            "open_date" : json.dumps(self.open_date,indent=4, sort_keys=True, default=str), 
            "close_date" : json.dumps(self.close_date,indent=4, sort_keys=True, default=str), 
            "open_price" : self.open_price, 
            "close_price" : self.close_price, 
            "profit" : self.profit, 
            "amount" : self.amount, 
            "close_reason" : self.close_reason ,
            "is_open" : self.is_open ,
            "symbol" : self.symbol, 
            "exchange" : self.exchange, 
            "profit_percent" : self.profit_percent, 
            "take_profit" : self.take_profit, 
            "dynamic_stoploss" : self.dynamic_stoploss, 
            "strategy" : self.strategy, 
        }

    @classmethod
    def find_by_name(cls,strategy,limit):
        return cls.query.filter_by(strategy=strategy).limit(limit)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
