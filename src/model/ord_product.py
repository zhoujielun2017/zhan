import datetime

from mongoengine import *

connect(db='ord')


class OrdProduct(Document):
    ord_id = StringField()
    product_id = StringField()
    title = StringField()
    main_pic = StringField()
    price = IntField()
    num = IntField()
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "title": self.title,
            "main_pic": self.main_pic,
            "price": self.price,
            "num": self.num
        }
