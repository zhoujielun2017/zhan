import datetime

from mongoengine import DoesNotExist, ValidationError

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
    except ValidationError:
        print("id length is wrong")
        return None


def page(page: Pagination):
    users = UserAddress.objects.paginate(page.page,
                                         page.page_size)
    return users


def update(address: UserAddress) -> UserAddress:
    return address.update(area1_id=address.area1_id,
                          area2_id=address.area2_id,
                          area3_id=address.area3_id,
                          area1_name=address.area1_name,
                          area2_name=address.area2_name,
                          area3_name=address.area3_name,
                          mobile=address.mobile,
                          address=address.address,
                          update_time=datetime.datetime.now())


def save(address: UserAddress) -> User:
    address.save()
    return str(address.id)


def delete(id: str):
    p = find_by_id(id)
    if p == None:
        return
    p.delete()
