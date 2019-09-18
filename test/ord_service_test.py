import unittest

from model.ord_save import OrdSave
from model.pagination import Pagination
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

    def test_find_by_id(self):
        ord = ord_service.find_by_id("5d818ddd7e5c06998b96297a")
        print(ord)

    def test_page(self):
        p = Pagination(1, 4)
        pros = ord_service.page(p)
        print(pros)
