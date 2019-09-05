from mongoengine import *
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
