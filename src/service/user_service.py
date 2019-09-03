from typing import List, Optional

import datetime

import bson

from model.user import User
from model.pagination import Pagination
from model.user_save import UserSave


def all():
    # owner.mobile = mobile
    # owner.password = password
    users = User.objects()
    for user in users:
        print(user.mobile)


def page(page:Pagination):
    # owner.mobile = mobile
    # owner.password = password
    users = User.objects[page.start:page.end]
    print(users)
    for user in users:
        print(user.mobile)

def find_user(mobile: str, password: str) -> User:
    # owner.mobile = mobile
    # owner.password = password
    user = User.objects(mobile=mobile,password=password).first()
    return user


def save(userSave: UserSave) -> User:
    owner = User()
    owner.mobile = userSave.mobile
    owner.password = userSave.password
    return owner.save()


if __name__ == '__main__':
    # all()
    print("------")
    p = Pagination()
    page()
    # id = insert_user("123","123")
    # print(id)
    # print(id.id)
    # print(id.mobile)