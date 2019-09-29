import json
import unittest

from app import app
from service import user_service
from test.views.login_view_test import LoginTest


class UserViewTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        LoginTest.test_login_in(self)
        self.save_user()

    def tearDown(self):
        # self.delete_user()
        pass

    def save_user(self):
        mobile = 123
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

    def delete_user(self):
        if self.user_id:
            response = self.client.delete('/user/%s' % str(self.user_id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")

    def test_detail_user(self):
        response = self.client.get('/user/%s' % str(self.user_id))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")
        self.assertIsNotNone(json_dict['data']['mobile'])
        self.assertNotIn('password', json_dict['data'])

    def test_update_user_head(self):
        jsonstr = json.dumps({
            "head_url": "/head/head_url.jpg"
        })
        response = self.client.put('/user/head', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")
