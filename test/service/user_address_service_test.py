import unittest

from model.pagination import Pagination
from model.user_adress import UserAddress
from service import user_address_service


class UserAddressServiceTest(unittest.TestCase):

    def setUp(self) -> None:
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
        self.address_id = user_address_service.save(address)

    def tearDown(self) -> None:
        user_address_service.delete(self.address_id)

    def test_update(self):
        address = user_address_service.find_by_id(self.address_id)
        address.user_id = "test_xxxxxxxxx_update"
        address.area1_id = "test_xxxxxxxxx_update"
        address.area2_id = "test_xxxxxxxxx_update"
        address.area3_id = "test_xxxxxxxxx_update"
        address.area1_name = "test_xxxxxxxxx_update"
        address.area2_name = "test_xxxxxxxxx_update"
        address.area3_name = "test_xxxxxxxxx_update"
        address.name = "test_xxxxxxxxx_update"
        address.mobile = "18566663363"
        address.address = "test_address_update"
        user_address_service.update(address)

    def test_page(self):
        re = user_address_service.page(Pagination(1, 10))
        self.assertGreater(re.total, 0)
