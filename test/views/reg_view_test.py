import json
import unittest

from app import app
from service import user_service


class RegViewTest(unittest.TestCase):
    """为注册逻辑编写测试案例"""

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_reg(self):
        data = {"mobile": 18577778888, "password": 123, "password2": 123}
        response = self.client.post('/login/reg', data=json.dumps(data))
        json_data = response.data
        json_dict = json.loads(json_data)
        user = user_service.find_by_mobile(data['mobile'])
        if not user:
            self.assertEqual(json_dict['code'], "success")
        else:
            self.assertEqual(json_dict['code'], "user.exists")

    def test_password_not_equal(self):
        data = {"mobile": 18577778888, "password": 123, "password2": 1234}
        response = self.client.post('/login/reg', data=json.dumps(data))
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "password.not.equal")
