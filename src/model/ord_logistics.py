from mongoengine import *
import datetime

connect(alias='ord_logistics', db='ord_logistics')


class OrdLogistics(Document):
    orderid = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'ord_logistics'}
