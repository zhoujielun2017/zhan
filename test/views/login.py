import json
import unittest

from werkzeug.http import parse_cookie

from app import app
from test.service.user_service_test import UserServiceTest


class LoginTest(unittest.TestCase):
    """为登录逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        self.client = app.test_client()
        user_test = UserServiceTest()
        user_test.setUp()
        self.login_user = user_test.user
        self.login_in()

    def login_in(self):
        response = app.test_client().post('/login/in',
                                          data=json.dumps(
                                              {'mobile': self.login_user.mobile, 'password': self.login_user.password}))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertIn('code', json_dict)
        self.assertEqual(json_dict['code'], 'success')
        cookies = response.headers.getlist('Set-Cookie')
        session = parse_cookie(cookies[0])['session']
        self.client.set_cookie('localhost', 'session', session)
