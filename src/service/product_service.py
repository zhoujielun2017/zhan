from typing import List, Optional

import datetime

import bson
import shortuuid
from bson import ObjectId

from model.product import Product
from model.pagination import Pagination
from model.product_save import ProductSave


def all():
    users = Product.objects()
    for user in users:
        print(user.mobile)


def page(page: Pagination):
    users = Product.objects[page.start:page.end]
    print(users)
    for user in users:
        print(user.mobile)


def find_by_id(id: str) -> Product:
    return Product.objects.get(pk=id)


def find_by_code(code: str) -> Product:
    return Product.objects.get(code=code)


def save(save: ProductSave) -> Product:
    p = Product()
    p.code=shortuuid.uuid()
    p.title = save.title
    p.content = save.content
    p.view_count = 0
    p.stock = 0
    return p.save()
