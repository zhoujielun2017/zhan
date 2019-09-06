from typing import List, Optional

import datetime

import bson
from mongoengine import DoesNotExist

from model.user import User
from model.pagination import Pagination
from model.user_save import UserSave


def all():
    # owner.mobile = mobile
    # owner.password = password
    users = User.objects()
    for user in users:
        print(user.mobile)


def find_by_id(id: str):
    try:
        return User.objects.get(pk=id)
    except DoesNotExist:
        return None


def page(page:Pagination):
    # owner.mobile = mobile
    # owner.password = password
    users = User.objects[page.start:page.end]
    print(users)
    for user in users:
        print(user.mobile)


def find_user(mobile: str, password: str) -> User:
    user = User.objects(mobile=str(mobile),password=str(password)).first()
    return user

def update(userSave: UserSave) -> User:
    owner = User()
    owner.mobile = userSave.mobile
    owner.password = userSave.password
    return owner.save()


def save(userSave: UserSave) -> User:
    owner = User()
    owner.mobile = userSave.mobile
    owner.password = userSave.password
    return owner.save()
