import datetime

from mongoengine import *

connect(alias='ord_product', db='ord_product')

class OrdProduct(Document):
    ord_id = StringField()
    product_id = StringField()
    num = IntField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'ord_product'}
