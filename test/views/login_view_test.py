import json
import unittest

from app import app


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
        self.assertEqual(json_dict['code'], "error.json", '状态码返回错误')

    def test_empty_username_password(self):
        response = self.client.post('/login/in', data=json.dumps({'mobile': ''}))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "param.null", '状态码返回错误')

    def test_login_in(self):
        response = app.test_client().post('/login/in', data=json.dumps({'mobile': '18577778888', 'password': '123'}))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertIn('code', json_dict, '数据格式返回错误')
        self.assertEqual(json_dict['code'], 'success', '状态码返回错误')
