import json
import unittest

from app import app
from model.gift_card_code import GiftCardCode
from model.product_save import ProductSave
from service import gift_card_service, product_service


class CreateOrdByGiftCardTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.get_product()
        self.save_gift_card()
        self.get_gift_card()

    def tearDown(self):
        p = product_service.find_by_code(self.product_save.code)
        product_service.delete(str(p.id))
        p2 = product_service.find_by_code(self.product_save.code)
        self.assertIsNone(p2)
        self.delete_ord()

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

    def save_gift_card(self):
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

    def get_gift_card(self):
        r = GiftCardCode()
        r.area = "01"
        r.print = "01"
        r.year = "2019"
        r.unit = "01"
        r.num = "000001"
        gift_card = gift_card_service.find_by_code(r.code())
        gift_card.update(status=1, product_id=str(self.product.id))
        self.gift_card = gift_card

    def delete_ord(self):
        response = self.client.delete('/ord/%s' % self.ord_id)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")

    def test_save_gift_card(self):
        jsonstr = json.dumps({
            "address": "xianggggggggggggg",
            "areas": [
                "010_北京",
                "01011_海淀区",
                "02112_中山路"
            ],
            "code": self.gift_card.code,
            "mobile": 18555555555,
            "name": "xxx",
            "password": self.gift_card.password
        })
        response = self.client.post('/ord/gift_card', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")
        self.ord_id = json_dict['data']['id']

    def test_detail(self):
        self.test_save_gift_card()
        response = self.client.get('/ord/%s' % self.ord_id)
        json_data = response.data
        json_dict = json.loads(json_data)
        data = json_dict['data']
        self.assertEqual(json_dict['code'], "success")
        for p in data['products']:
            self.assertIsNotNone(p['main_pic'])
        # print(json_dict)
        self.assertEqual(data['ord']['status'], 3)
        self.assertIsNotNone(data['area']['name'])
        self.assertIsNotNone(data['area']['mobile'])
        self.assertIsNotNone(data['area']['address'])
