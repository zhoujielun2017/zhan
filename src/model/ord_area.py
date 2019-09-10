import datetime

from mongoengine import *

connect(alias='ord_area', db='ord_area')


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

    meta = {'db_alias': 'ord_area'}
