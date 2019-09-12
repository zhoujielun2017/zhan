import datetime

from mongoengine import *

connect(alias='ord_product', db='ord_product')

class OrdProduct(Document):
    ord_id = StringField()
    product_id = StringField()
    title = StringField()
    price = IntField()
    num = IntField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'ord_product'}

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "title": self.title,
            "num": self.num
        }
