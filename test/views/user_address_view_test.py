import json
import unittest

from app import app


class UserAddressViewTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.save_address()

    def tearDown(self):
        self.delete_address()

    def save_address(self):
        jsonstr = json.dumps({
            "address": "xx小区xx栋xxx房",
            "area1_id": 11,
            "area1_name": "北京",
            "area2_id": 1101,
            "area2_name": "市辖区",
            "area3_id": 110101,
            "area3_name": "东城区",
            "mobile": 18666666666
        })
        response = self.client.post('/address/address', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        if json_dict['code'] == "success":
            uid = json_dict['data']['id']
            self.assertIsNotNone(uid)
            self.address_id = uid

    def test_detail(self):
        if self.address_id:
            response = self.client.get('/address/%s' % str(self.address_id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")
            self.assertIsNotNone(json_dict['data']['mobile'])
            self.assertEqual(json_dict['data']['mobile'], "18666666666")

    def delete_address(self):
        if self.address_id:
            response = self.client.delete('/address/%s' % str(self.address_id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")
