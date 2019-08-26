from typing import List, Optional

import datetime

import bson

from model.ord import Ord
from model.ord_adress import OrdAdress
from model.ord_card import OrdCard
from model.ord_product import OrdProduct


class OrdDTO(object):
    userid=''
    productid=''


def all():
    return Ord.objects()


def insert_ord(dto:OrdDTO):
    ord = Ord()
    ordPro = OrdProduct()
    ord.userid = dto.userid
    ordPro.productid = dto.productid
    dbord = ord.save()
    ordPro.orderid=dbord.id
    return dbord.id


if __name__ == '__main__':
    dto = OrdDTO()
    dto.userid="111"
    dto.productid="333"
    id = insert_ord(dto)
    print(id)
    ords = all()
    for o in ords:
        print(o.id)