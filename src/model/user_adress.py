import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='user_address', db='user')


class UserAddress(Document):
    user_id = StringField()
    area1_id = StringField()
    area2_id = StringField()
    area3_id = StringField()
    area1_name = StringField()
    area2_name = StringField()
    area3_name = StringField()
    address = StringField()
    name = StringField()
    mobile = StringField()
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    meta = {'db_alias': 'user_address'}

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": self.user_id,
            "area1_id": self.area1_id,
            "area1_name": self.area1_name,
            "area2_id": self.area2_id,
            "area2_name": self.area2_name,
            "area3_id": self.area3_id,
            "area3_name": self.area3_name,
            "name": self.name,
            "mobile": self.mobile,
            "address": self.address
        }

    def to_update(self):
        dd = self.to_dict()
        for k, v in list(dd.items()):
            if not v:
                dd.pop(k)
        return dd
