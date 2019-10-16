import json

from service import user_service
from test.views.login import LoginTest


class UserViewTest(LoginTest):

    def setUp(self):
        super().setUp()
        self.save_user()

    def tearDown(self):
        self.delete_user()
        user = user_service.find_by_id(self.user_id)
        self.assertIsNone(user)
        # pass

    def save_user(self):
        self.mobile = 18566667777
        self.password = 18566667777
        jsonstr = json.dumps({
            "mobile": self.mobile,
            "password": self.password
        })
        response = self.client.post('/user/users', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        if json_dict['code'] == "success":
            uid = json_dict['data']['id']
            self.assertIsNotNone(uid)
            self.user_id = uid
        else:
            user = user_service.find_by_mobile(self.mobile)
            self.user_id = str(user.id)

    def delete_user(self):
        if self.user_id:
            response = self.client.delete('/user/%s' % str(self.user_id))
            json_data = response.data
            json_dict = json.loads(json_data)
            self.assertEqual(json_dict['code'], "success")

    def delete_user_not_exist(self):
        response = self.client.delete('/user/test_not_exist')
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "error.not.exists")

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

    def test_update_user_password(self):
        jsonstr = json.dumps({
            "password_old": self.login_user.password,
            "password_new1": 123,
            "password_new2": 123
        })
        response = self.client.put('/user/password', data=jsonstr)
        json_data = response.data
        json_dict = json.loads(json_data)
        self.assertEqual(json_dict['code'], "success")
