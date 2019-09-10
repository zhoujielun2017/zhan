import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='ord', db='ord')


class Ord(Document):
    user_id = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'db_alias': 'ord'}


if __name__ == '__main__':
    ord = Ord()
    print(dir(ord))
    print(type(ord))
    print(ord.__dict__)