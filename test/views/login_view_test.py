import json
import unittest

from werkzeug.http import parse_cookie

from app import app
from test.service.user_service_test import UserServiceTest


class LoginViewTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.user_test = UserServiceTest()
        self.user_test.setUp()
        self.user = self.user_test.user

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
        response = app.test_client().post('/login/in',
                                          data=json.dumps({'mobile': self.user.mobile, 'password': self.user.password}))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertIn('code', json_dict)
        self.assertEqual(json_dict['code'], 'success')
        cookies = response.headers.getlist('Set-Cookie')
        session = parse_cookie(cookies[0])['session']
        self.client.set_cookie('localhost', 'session', session)
        return self.user_test.user
