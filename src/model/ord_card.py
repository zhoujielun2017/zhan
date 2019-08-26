from mongoengine import *
import datetime

connect(alias='ord_card', db='ord_card')


class OrdCard(Document):
    orderid = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'ord_card'}
