from mongoengine import DoesNotExist

from model.pagination import Pagination
from model.user import User
from model.user_adress import UserAddress


def find_by_user_id(user_id: str):
    users = UserAddress.objects(user_id=user_id)
    return users


def find_by_id(id: str):
    try:
        return UserAddress.objects.get(pk=id)
    except DoesNotExist:
        return None


def page(page: Pagination):
    users = UserAddress.objects.paginate(page.page,
                                         page.page_size)
    return users


def update(address: UserAddress) -> User:
    return address.update()


def save(address: UserAddress) -> User:
    address.save()
    return str(address.id)


def delete(id: str):
    p = find_by_id(id)
    if p == None:
        return
    p.delete()
