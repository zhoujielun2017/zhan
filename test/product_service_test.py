import hashlib
import unittest
import uuid

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
        for item in pros.queryset:
            print(item.code)

    def test_find_by_id(self):
        p = product_service.find_by_id("5d65ff35e0c4f62d92c46dc6")
        self.assertIsNotNone(p,"")

    def test_find_by_code(self):
        p = product_service.find_by_code("5cTJxqUoUPXmucpTPni9ZL")
        self.assertIsNotNone(p,"")

    def test_save(self):
        save = ProductSave()
        save.title="test_product_title"
        save.content="test_product_content"
        product_service.save(save)


if __name__ == '__main__':
    unittest.main()
