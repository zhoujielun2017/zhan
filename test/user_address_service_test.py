import unittest

from model.pagination import Pagination
from model.user_adress import UserAddress
from service import user_address_service


class UserAddressServiceTest(unittest.TestCase):
    def test_save(self):
        address = UserAddress()
        address.user_id = "test_xxxxxxxxx"
        address.area1_id = "test_xxxxxxxxx"
        address.area2_id = "test_xxxxxxxxx"
        address.area3_id = "test_xxxxxxxxx"
        address.area1_name = "test_xxxxxxxxx"
        address.area2_name = "test_xxxxxxxxx"
        address.area3_name = "test_xxxxxxxxx"
        address.name = "test_xxxxxxxxx"
        address.mobile = "18566663363"
        address.address = "test_address"
        user_address_service.save(address)

    def test_delete(self):
        user_address_service.delete("5d79a58acfc60733668a78e6")

    def test_page(self):
        re = user_address_service.page(Pagination(1, 10))
        print(re.to_dict())
