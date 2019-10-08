import unittest

from app import app


class FileViewTest(unittest.TestCase):
    """FileView测试用例"""

    def setUp(self):
        app.testing = True
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_captcha(self):
        response = self.client.get('/file/captcha', data={})
        self.assertTrue(response.status_code == 200)
