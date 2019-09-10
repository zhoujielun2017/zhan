import datetime

from mongoengine import DoesNotExist

from model.pagination import Pagination
from model.user import User
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


def page(page: Pagination):
    id = User.objects.first().id
    total = User.objects.count()
    users = User.objects.paginate_field('mobile', page.page,
                                        page.page_size, total=total)
    return users


def find_by_mobile(mobile: str) -> User:
    user = User.objects(mobile=str(mobile)).first()
    return user


def find_by_user(mobile: str, password: str) -> User:
    user = User.objects(mobile=str(mobile), password=str(password)).first()
    return user


def update(userSave: UserSave) -> User:
    user = find_by_mobile(userSave.mobile)
    return user.update(password=str(userSave.password), update_time=datetime.datetime.now())


def save(userSave: UserSave) -> User:
    owner = User()
    owner.mobile = userSave.mobile
    owner.password = userSave.password
    owner.save()
    return str(owner.id)
