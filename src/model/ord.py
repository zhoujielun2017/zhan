import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='ord', db='ord')


class Ord(Document):
    user_id = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'strict': False, 'db_alias': 'ord'}

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "create_time": self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            "update_time": self.update_time.strftime('%Y-%m-%d %H:%M:%S')}
