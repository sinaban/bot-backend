from db import db
import json
import datetime
from exchanges import kucoin_pairs

class Trades(db.Model):
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
            "FormalName" : kucoin_pairs.futures_pairs[self.o_pair]

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


class ClosedTrades(db.Model):
    __tablename__ = 'closed_trades'
    o_id = db.Column(db.BigInteger, primary_key=True)

    o_exchange = db.Column(db.String(50)) 
    o_pair = db.Column(db.String(50))
    o_symbol = db.Column(db.String(50)) 
    o_side = db.Column(db.String(50)) 
    o_order_id = db.Column(db.String(50)) 
    o_price = db.Column(db.Float)
    o_amount = db.Column(db.Float)
    o_status = db.Column(db.String(50)) 
    o_type = db.Column(db.String(50)) 
    o_oid_close = db.Column(db.String(50)) 
    o_oid_open = db.Column(db.String(50))
    o_open_date = db.Column(db.DateTime)
    o_close_date = db.Column(db.DateTime)
    o_open_price = db.Column(db.Float)
    o_close_price = db.Column(db.Float)
    o_take_profit = db.Column(db.Float)
    o_dynamic_stoploss = db.Column(db.Float)
    o_profit = db.Column(db.Float)
    o_profit_percent = db.Column(db.Float)
    o_strategy = db.Column(db.String(50))
    o_close_reason = db.Column(db.String(50))


    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')

    def __init__(self, o_exchange,o_pair,o_symbol,o_side,o_order_id,o_id,o_price,o_amount,o_status,o_type,o_oid_close,o_oid_open
        ,o_open_date,o_close_date,o_open_price,o_close_price,o_take_profit,o_dynamic_stoploss,o_profit,o_profit_percent,o_strategy,o_close_reason):
        self.o_pair = o_pair
        self.o_oid_close = o_oid_close
        self.o_oid_open = o_oid_open
        self.o_open_date = o_open_date
        self.o_close_date = o_close_date
        self.o_open_price = o_open_price
        self.o_close_price = o_close_price
        self.o_order_id = o_order_id
        self.o_id = o_id
        self.o_price = o_price
        self.o_profit = o_profit
        self.o_amount = o_amount
        self.o_status = o_status
        self.o_type = o_type
        self.o_close_reason = o_close_reason
        self.o_side = o_side
        self.o_symbol = o_symbol
        self.o_exchange = o_exchange
        self.o_profit_percent = o_profit_percent
        self.o_take_profit = o_take_profit
        self.o_dynamic_stoploss = o_dynamic_stoploss
        self.o_strategy = o_strategy
        
    def defaultconverter(self,o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    def json(self):
        return {
            "pair" : self.o_pair,
            "oid_close" : self.o_oid_close,
            "oid_open" : self.o_oid_open, 
            "open_date" : json.dumps(self.o_open_date,indent=4, sort_keys=True, default=str), 
            "close_date" : json.dumps(self.o_close_date,indent=4, sort_keys=True, default=str), 
            "open_price" : self.o_open_price, 
            "close_price" : self.o_close_price, 
            "profit" : self.o_profit, 
            "amount" : self.o_amount, 
            "side" : self.o_side,
            "close_reason" : self.o_close_reason ,
            "symbol" : self.o_symbol, 
            "exchange" : self.o_exchange, 
            "profit_percent" : self.o_profit_percent, 
            "take_profit" : self.o_take_profit, 
            "dynamic_stoploss" : self.o_dynamic_stoploss, 
            "strategy" : self.o_strategy, 
            "FormalName" : kucoin_pairs.futures_pairs[self.o_pair]
        }

    @classmethod
    def find_by_name(cls,strategy,limit):
        return cls.query.filter_by(o_strategy=strategy).limit(limit)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
