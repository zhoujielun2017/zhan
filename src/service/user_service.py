import datetime

from mongoengine import DoesNotExist, ValidationError

from model.pagination import Pagination
from model.user import User
from model.user_save import UserSave


def all():
    # owner.mobile = mobile
    # owner.password = password
    users = User.objects()
    for user in users:
        print(user.mobile)


def find_by_id(uid: str):
    try:
        return User.objects.get(pk=uid)
    except DoesNotExist:
        return None
    except ValidationError:
        print("id length is wrong %s" % uid)
        return None


def page(page: Pagination, **kwargs):
    users = User.objects.paginate_field(page.page, page.page_size, **kwargs)
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


def save(userSave: UserSave) -> str:
    owner = User()
    owner.mobile = userSave.mobile
    owner.password = userSave.password
    owner.head_url = userSave.head_url
    owner.save()
    return str(owner.id)


def delete(id: str):
    u = find_by_id(id)
    if u:
        u.delete()
