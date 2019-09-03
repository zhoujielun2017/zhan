import sys
import unittest

sys.path.append('../')
from model.user_save import UserSave
from service import user_service


class ProductServiceTest(unittest.TestCase):

    def test_save(self):
        save = UserSave()
        save.mobile = "123"
        save.password = "123"
        user_service.save(save)

    def test_find_user(self):
        user = user_service.find_user("123","123")
        print(user.mobile)
        self.assertIsNotNone(user)