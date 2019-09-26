import json
import unittest

from app import app
from service import user_service


class UserViewTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_save_user(self):
        mobile = 18577779999
        jsonstr = json.dumps({
            "mobile": mobile,
            "password": 123
        })
        response = self.client.post('/user/users', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        if json_dict['code'] == "success":
            uid = json_dict['data']['id']
            self.assertIsNotNone(uid)
            self.user_id = uid
        else:
            user = user_service.find_by_mobile(mobile)
            self.user_id = str(user.id)

        self.detail_user()
        self.delete_product()

    def detail_user(self):
        if self.user_id:
            response = self.client.get('/user/%s' % str(self.user_id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")
            self.assertIsNotNone(json_dict['data']['mobile'])
            self.assertNotIn('password', json_dict['data'])

    def delete_product(self):
        if self.user_id:
            response = self.client.delete('/user/%s' % str(self.user_id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")
