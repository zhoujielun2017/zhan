from mongoengine import *
import datetime

connect(alias='ord_log', db='ord_log')


class OrdLog(Document):
    orderid = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'ord_log'}
