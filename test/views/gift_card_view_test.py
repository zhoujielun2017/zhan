import json
import unittest

from app import app
from model.product_save import ProductSave
from service import product_service


class OrdViewTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        p = product_service.find_by_code(self.product_save.code)
        product_service.delete(str(p.id))
        p2 = product_service.find_by_code(self.product_save.code)
        self.assertIsNone(p2)

    def get_product(self):
        save = ProductSave()
        save.code = "test_5d79c3d07c1f2df47d4cb991"
        save.title = "test_product_title"
        save.content = "test_product_content"
        save.main_pic = "test_product_main_pic"
        save.price = 2000
        self.product_save = save
        p = product_service.save(self.product_save)
        self.product = p
        self.assertEqual(p.code, self.product_save.code)

    def test_save_gift_card(self):
        jsonstr = json.dumps({
            "area": "01",
            "num_end": "000010",
            "num_start": "000001",
            "print": "01",
            "unit": "01",
            "year": "2019"
        })
        response = self.client.post('/gift_card/gift_cards', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")

    def test_bind_product_range(self):
        self.get_product()
        jsonstr = json.dumps({
            "product_id": str(self.product.id),
            "start_code": "0120190101000100",
            "end_code": "0120190101000001"
        })
        response = self.client.put('/gift_card/product/range', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")
