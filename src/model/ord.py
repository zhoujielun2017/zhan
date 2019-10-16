import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='ord', db='ord')


class Ord(Document):
    user_id = StringField()
    # 1 待支付 2 已支付 3 待发货 4 已发货 5 待收货 6 已收货 7 待评价 8 已评价
    status = IntField()
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)
    meta = {'strict': False, 'db_alias': 'ord',
            'collection': 'ord'}

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "status": self.status,
            "create_time": self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            "update_time": self.update_time.strftime('%Y-%m-%d %H:%M:%S')}
