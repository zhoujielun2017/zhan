from mongoengine import *
from mongoenginepagination import Document
import datetime

connect(alias='user', db='user')


class User(Document):
    # userid = StringField(default=datetime.datetime.utcnow)
    name = StringField()
    mobile = StringField()
    password = StringField()
    status = IntField()
    type = IntField()
    login_time = DateTimeField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'user'}

    def to_dict(self):
        return {
                "id":self._id,
                "mobile": self.mobile,
                "status": self.status,
                "type": self.status,
                "create_time": self.create_time.strftime( '%Y-%m-%d %H:%M:%S'),
                "update_time": self.update_time.strftime( '%Y-%m-%d %H:%M:%S')}