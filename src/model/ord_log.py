import datetime

from mongoengine import *

connect(db='ord')


class OrdLog(Document):
    ord_id = StringField()
    create_time = DateTimeField(default=datetime.datetime.now)

    meta = {'collection': 'ord_log'}
