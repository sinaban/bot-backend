from db import db

class Bot_propModel(db.Model):
    __tablename__ = 'bots_prop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    apikey = db.Column(db.String(80)) 
    apisecret = db.Column(db.String(80))
    apipass = db.Column(db.String(80))
    exchange_name = db.Column(db.String(80))
    market_type = db.Column(db.String(10))


    # store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # store = db.relationship('StoreModel')

    def __init__(self, name, apikey, apisecret,apipass,exchange_name,market_type):
        self.name = name
        self.apikey = apikey
        self.apisecret = apisecret
        self.apipass = apipass
        self.exchange_name = exchange_name
        self.market_type = market_type


    def json(self):
        return {'name': self.name,'id':self.id, 'exchange_name': self.exchange_name,'apikey':self.apikey,'market type': self.market_type}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
