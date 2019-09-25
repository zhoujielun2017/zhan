import datetime

from mongoengine import *

connect(db='ord')


class OrdArea(Document):
    ord_id = StringField()
    area1_id = StringField()
    area2_id = StringField()
    area3_id = StringField()
    area1_name = StringField()
    area2_name = StringField()
    area3_name = StringField()
    address = StringField()
    name = StringField()
    mobile = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "area1_id": self.area1_id,
            "area1_name": self.area1_name,
            "area2_id": self.area2_id,
            "area2_name": self.area2_name,
            "area3_id": self.area3_id,
            "area3_name": self.area3_name,
            "name": self.name,
            "mobile": self.mobile,
            "address": self.address,
        }
