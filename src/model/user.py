import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='user', db='user')


class User(Document):
    # userid = StringField(default=datetime.datetime.utcnow)
    name = StringField()
    mobile = StringField(unique=True)
    head_url = StringField()
    password = StringField()
    # 1 有效 0 无效
    status = IntField(default=1)
    # 1 普通用户 2 管理员
    type = IntField(default=1)
    login_time = DateTimeField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'user'}

    def to_dict(self):
        return {
            "id": str(self.id),
            "mobile": self.mobile,
            "status": self.status,
            "type": self.type,
            "head_url": self.head_url,
            "create_time": self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            "update_time": self.update_time.strftime('%Y-%m-%d %H:%M:%S')}
