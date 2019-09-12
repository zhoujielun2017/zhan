import unittest

import shortuuid as shortuuid

from model.pagination import Pagination
from model.product_save import ProductSave
from service import product_service


class ProductServiceTest(unittest.TestCase):
    def test_something(self):
        a = shortuuid.uuid()
        print("test_something %s" % a)

    def test_page(self):
        p = Pagination(1, 4)
        pros = product_service.page(p)
        print(pros.to_dict())

    def test_find_by_id(self):
        p = product_service.find_by_id("5d65ff35e0c4f62d92c46dc6")

    def test_find_by_code(self):
        p = product_service.find_by_code("5cTJxqUoUPXmucpTPni9ZL")
        print(p.to_dict())
        self.assertIsNotNone(p,"")

    def test_save(self):
        save = ProductSave()
        save.title="test_product_title"
        save.content="test_product_content"
        save.price = 1000
        product_service.save(save)

    def test_update(self):
        save = ProductSave()
        save.id = "5d79c3d07c1f2df47d4cb991"
        save.title = "test_product_ti22tle"
        save.content = "test_product_33content"
        save.price = 2000
        # save.main_pic="test_update_main_pic"
        product_service.update(save)
