import random
from typing import List, Optional

import datetime

import bson
import shortuuid
from bson import ObjectId
from mongoengine import DoesNotExist

from model.gift_card import GiftCard

from model.gift_card_code import GiftCardCode
from model.pagination import Pagination
from model.product_save import ProductSave


def all():
    users = GiftCard.objects()
    for user in users:
        print(user.mobile)


def page(page: Pagination):
    id = GiftCard.objects.first().id
    users = GiftCard.objects.paginate_field('code', id, page.page,
                                            page_size=page.page_size)
    return users


def find_by_id(id: str) -> GiftCard:
    try:
        return GiftCard.objects.get(pk=id)
    except DoesNotExist:
        print("does not exist")
        return None


def find_by_code(code: str) -> GiftCard:
    return GiftCard.objects(code=code).first()


def save(code: GiftCardCode) -> GiftCard:
    p = GiftCard()
    p.code = code.code()
    r1 = random.randint(100000000, 999999999)
    r2 = random.randint(100000000, 999999999)
    p.status = 0
    p.password = str(r1) + str(r2)
    return p.save()


def delete(id: str):
    p = find_by_id(id)
    if p == None:
        return
    p.delete()


# 已使用
def update_used(code: str, password: str) -> GiftCard:
    p = find_by_code(code)
    if p.password == password:
        p.update(status=2)
    return p
