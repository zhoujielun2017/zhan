import json
import unittest

from app import app
from test.service.product_service_test import ProductServiceTest


class GiftCardViewTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.product_service_test = ProductServiceTest()
        self.product_service_test.setUp()
        self.product = self.product_service_test.product

    def tearDown(self):
        self.product_service_test.tearDown()

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
        jsonstr = json.dumps({
            "product_id": str(self.product.id),
            "start_code": "0120190101000100",
            "end_code": "0120190101000001"
        })
        response = self.client.put('/gift_card/product/range', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")

    def test_page_empty_status(self):
        response = self.client.get('/gift_card/gift_cards?page=1&page_size=10')
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")

    def test_page(self):
        response = self.client.get('/gift_card/gift_cards?page=1&page_size=10&status=1')
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")
