import json
import unittest

from app import app
from test.service.user_service_test import UserServiceTest


class LoginTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_empty_param(self):
        response = self.client.post('/login/in', data={})
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "error.json")

    def test_empty_username_password(self):
        response = self.client.post('/login/in', data=json.dumps({'mobile': ''}))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "param.null")

    def test_login_in(self):
        UserServiceTest().setUp()
        response = app.test_client().post('/login/in', data=json.dumps({'mobile': '18577778888', 'password': '123'}))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertIn('code', json_dict)
        self.assertEqual(json_dict['code'], 'success')
