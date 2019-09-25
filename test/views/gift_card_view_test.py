import json
import unittest

from app import app


class OrdViewTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

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
