import random

from mongoengine import DoesNotExist

from const import const
from model.gift_card import GiftCard
from model.gift_card_code import GiftCardCode
from model.pagination import Pagination


def all():
    users = GiftCard.objects()
    for user in users:
        print(user.mobile)


def page(page: Pagination, **kwargs):
    users = GiftCard.objects.paginate_field(page.page, page.page_size, **kwargs)
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
    p.product_id = code.product_id
    p.code = code.code()
    r1 = random.randint(100000000, 999999999)
    r2 = random.randint(100000000, 999999999)
    if not p.product_id:
        p.status = const.GIFT_NOT_BIND
    else:
        p.status = const.GIFT_VALID
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
        p.update(status=const.GIFT_CARD_USED)
    return p


# 绑定用印
def update_bind_user(code: str, password: str, user_id: str) -> GiftCard:
    p = find_by_code(code)
    if p.password == password:
        p.update(user_id=user_id)
    return p


# 绑定商品
def update_bind_product(codes, product_id: str) -> GiftCard:
    for code in codes:
        p = find_by_code(code)
        p.update(status=const.GIFT_VALID, product_id=product_id)
