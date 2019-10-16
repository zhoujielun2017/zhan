import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='gift_card', db='gift_card')


class GiftCard(Document):
    user_id = StringField()
    product_id = StringField()
    code = StringField(unique=True)
    password = StringField()
    # 0 未绑定 "1有效 -1过期 2已使用"
    status = IntField(default=1)
    expire_time = DateTimeField()
    use_time = DateTimeField()
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)
    meta = {'db_alias': 'gift_card'}

    def to_dict(self):
        return {
            "id": str(self.id),
            "code": self.code,
            "password": self.password,
            "status": self.status,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "create_time": self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            "expire_time": None if not self.expire_time else self.expire_time.strftime('%Y-%m-%d %H:%M:%S'),
            "use_time": None if not self.use_time else self.use_time.strftime('%Y-%m-%d %H:%M:%S'),
            "update_time": self.update_time.strftime('%Y-%m-%d %H:%M:%S')}
