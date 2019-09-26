import json
import unittest

from app import app
from service import product_service


class ProductViewTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.save_product()

    def tearDown(self):
        self.delete_product()

    def save_product(self):
        jsonstr = json.dumps({
            "content": "test_contet",
            "main_pic": "/2019/09/05/12312312.jpg",
            "pics": "/2019/09/05/12312312.jpg,/2019/09/05/1231238934.jpg",
            "price": 1000,
            "title": "test_title"
        })
        response = self.client.post('/product/products', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")
        code = json_dict['data']
        self.assertIsNotNone(code)
        psaved = product_service.find_by_code(code)
        self.product = psaved

    def test_get_product_id(self):
        if self.product:
            response = self.client.get('/product/id/%s' % str(self.product.id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")

    def delete_product(self):
        if self.product:
            response = self.client.delete('/product/%s' % str(self.product.id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")
