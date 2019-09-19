import datetime

from mongoengine import *

connect(db='ord')

class OrdProduct(Document):
    ord_id = StringField()
    product_id = StringField()
    title = StringField()
    price = IntField()
    num = IntField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "title": self.title,
            "num": self.num
        }
