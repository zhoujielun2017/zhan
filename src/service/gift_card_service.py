import random
from typing import List, Optional

import datetime

import bson
import shortuuid
from bson import ObjectId

from model.gift_card import GiftCard

from model.gift_card_code import GiftCardCode
from model.pagination import Pagination
from model.product_save import ProductSave


def all():
    users = GiftCard.objects()
    for user in users:
        print(user.mobile)


def page(page: Pagination):
    users = GiftCard.objects[page.start:page.end]
    return users


def find_by_id(id: str) -> GiftCard:
    return GiftCard.objects.get(pk=id)


def find_by_code(code: str) -> GiftCard:
    return GiftCard.objects(code=code).first()


def save(code: GiftCardCode) -> GiftCard:
    p = GiftCard()
    p.code = code.code()
    r1 = random.randint(100000000, 999999999)
    r2 = random.randint(100000000, 999999999)
    p.password = str(r1) + str(r2)
    return p.save()
