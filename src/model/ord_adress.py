from mongoengine import *
import datetime

connect(alias='ord_address', db='ord_address')


class OrdAdress(Document):
    orderid = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'ord_address'}
