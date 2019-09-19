import datetime

from mongoengine import *

connect(db='ord')


class OrdLog(Document):
    orderid = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'collection': 'ord_log'}
