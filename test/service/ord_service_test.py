import unittest

from model.ord_save import OrdSave
from model.pagination import Pagination
from service import ord_service


class OrdServiceTest(unittest.TestCase):

    def setUp(self):
        print("pass")
        save = OrdSave()
        save.pros = [{"id": "sdfsf", "num": 1, "title": "test_tile"}]
        save.areas = ["test_1", "test2_2"]
        save.mobile = "test_123123"
        save.name = "test_123123"
        save.address = "test_address"
        # 千万不要命名为self.id 和 unittest里面的id重复
        self.ord_id = ord_service.save(save)
        self.assertIsNotNone(self.ord_id)

    def tearDown(self):
        ord_service.delete(self.ord_id)
        o = ord_service.find_by_id(self.ord_id)
        self.assertIsNone(o)

    def test_find_by_id(self):
        o = ord_service.find_by_id(self.ord_id)
        self.assertIsNotNone(o)

    def test_page(self):
        p = Pagination(1, 4)
        pros = ord_service.page(p)
        self.assertGreater(pros.get("total"), 0)
