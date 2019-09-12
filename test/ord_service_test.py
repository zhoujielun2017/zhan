import unittest

from model.ord_save import OrdSave
from service import ord_service


class ProductServiceTest(unittest.TestCase):

    def test_save(self):
        save = OrdSave()
        save.pros = [{"id": "sdfsf", "num": 1, "title": "test_tile"}]
        save.areas = ["test_1", "test2_2"]
        save.mobile = "test_123123"
        save.name = "test_123123"
        save.address = "test_address"
        ord_service.save(save)
