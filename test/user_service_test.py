import sys
import unittest

from model.pagination import Pagination

sys.path.append('../')
from model.user_save import UserSave
from service import user_service


class ProductServiceTest(unittest.TestCase):
    def test_save(self):
        save = UserSave()
        save.mobile = "123"
        save.password = "123"
        user_service.save(save)

    def test_find_by_user(self):
        user = user_service.find_by_user("123", "123")
        print(user.mobile)
        self.assertIsNotNone(user)

    def test_page(self):
        p = Pagination(1, 10)
        user = user_service.page(p)
        print(user.to_dict())

    def test_page_contains(self):
        p = Pagination(1, 10)
        user = user_service.page(p, mobile__contains="")
        print(user.to_dict())
