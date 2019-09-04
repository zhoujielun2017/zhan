import datetime

from mongoengine import *

connect(alias='gift_card', db='gift_card')

class GiftCard(Document):

    code = StringField()
    password = StringField()
    expire_time = DateTimeField(default=datetime.datetime.utcnow)
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'db_alias': 'gift_card'}

    def as_dict(self):
        return {"code": self.code,
                "password": self.password,
                "create_time": self.create_time.strftime( '%Y-%m-%d %H:%M:%S'),
                "expire_time": self.expire_time.strftime( '%Y-%m-%d %H:%M:%S'),
                "update_time": self.update_time.strftime( '%Y-%m-%d %H:%M:%S')}