import datetime

from mongoengine import *
from mongoenginepagination import Document

connect(alias='gift_card', db='gift_card')

class GiftCard(Document):

    code = StringField()
    password = StringField()
    # 1有效 -1过期 2已使用
    status = IntField(default=1)
    expire_time = DateTimeField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'db_alias': 'gift_card'}

    def to_dict(self):
        return {
                "id":self._id,
                "code": self.code,
                "password": self.password,
                "status": self.status,
                "create_time": self.create_time.strftime( '%Y-%m-%d %H:%M:%S'),
                "expire_time": None if self.expire_time==None else self.expire_time.strftime( '%Y-%m-%d %H:%M:%S'),
                "update_time": self.update_time.strftime( '%Y-%m-%d %H:%M:%S')}