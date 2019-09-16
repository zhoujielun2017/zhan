import re
import unittest

from model.result import Result


class DivisionServiceTest(unittest.TestCase):

    def test_result_dict(self):
        self.assertDictEqual(Result().success(), {'code': 'success'})
        self.assertDictEqual(Result().success("data"), {'code': 'success', 'data': 'data'})
        self.assertDictEqual(Result().fail(), {'code': 'fail'})
        self.assertDictEqual(Result().fail(code="cod11e", msg="msg11"), {'code': 'cod11e', 'msg': 'msg11'})
        self.assertDictEqual(Result().fail(code="cod11e"), {'code': 'cod11e'})

    def test_string_in(self):
        ALLOW_PATH = ["/login/in", "/login/reg", "/login/reg", "/area/areas"]
        if '/login/in' in ALLOW_PATH:
            print("yes")
        else:
            print("no")

    def test_match(self):
        url = "/product/products"
        if re.match("/product/products", url):
            print("match")
