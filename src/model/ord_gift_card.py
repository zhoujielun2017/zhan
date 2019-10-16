import datetime

from mongoengine import *

connect(db='ord')


class OrdGiftCard(Document):
    ord_id = StringField()
    gift_card_code = StringField()
    gift_card_id = StringField()
    create_time = DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        return {
            "gift_card_id": self.gift_card_id,
            "gift_card_code": self.gift_card_code
        }
