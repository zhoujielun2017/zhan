import unittest

from model.pagination import Pagination
from model.product_save import ProductSave
from service import product_service


class ProductServiceTest(unittest.TestCase):

    def setUp(self):
        save = ProductSave()
        save.code = "test_5d79c3d07c1f2df47d4cb991"
        save.title = "test_product_title"
        save.content = "test_product_content"
        save.price = 2000
        self.product_save = save
        p = product_service.save(self.product_save)
        self.product = p
        self.assertEqual(p.code, self.product_save.code)

    def tearDown(self):
        p = product_service.find_by_code(self.product_save.code)
        product_service.delete(str(p.id))
        p2 = product_service.find_by_code(self.product_save.code)
        self.assertIsNone(p2)

    def test_update(self):
        p = product_service.find_by_code(self.product_save.code)
        save = ProductSave()
        save.id = p.id
        save.title = "test_title_update"
        save.content = "test_content_update"
        save.price = 2000
        count = product_service.update(save)
        self.assertEqual(count, 1)

    def test_page(self):
        p = Pagination(1, 4)
        pros = product_service.page(p)
        print(pros.to_dict())
        self.assertGreater(pros.total, 0)

    def test_find_by_id(self):
        p = product_service.find_by_code(self.product_save.code)
        p2 = product_service.find_by_id(p.id)
        self.assertEqual(p, p2)

    def test_find_by_code(self):
        p = product_service.find_by_code(self.product_save.code)
        self.assertIsNotNone(p)
