import datetime

from mongoengine import *

connect(alias='ord_gift_card', db='ord_gift_card')


class OrdGiftCard(Document):
    orderid = StringField()
    gift_card_code = StringField()
    gift_card_id = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'db_alias': 'ord_gift_card'}
