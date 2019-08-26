from mongoengine import *
import datetime

connect(alias='ord_product', db='ord_product')


class OrdProduct(Document):
    orderid = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'ord_product'}
