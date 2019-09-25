import unittest

from model.pagination import Pagination
from model.user_save import UserSave
from service import user_service


class UserServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        save = UserSave()
        save.mobile = "18577778888"
        save.password = "123"
        self.user = save
        user = user_service.find_by_mobile(save.mobile)
        if not user:
            self.user_id = user_service.save(save)
        else:
            self.user_id = str(user.id)

    def tearDown(self) -> None:
        user_service.delete(self.user_id)

    def test_find_by_user(self):
        user = user_service.find_by_user(self.user.mobile, self.user.password)
        self.assertIsNotNone(user)

    def test_page(self):
        p = Pagination(1, 10)
        user = user_service.page(p)
        self.assertGreater(user.total, 0)

    def test_page_contains(self):
        p = Pagination(1, 10)
        user = user_service.page(p, mobile__contains=self.user.mobile)
        self.assertGreater(user.total, 0)
