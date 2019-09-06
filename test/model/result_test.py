import unittest

from model.result import Result
from service import division_service


class DivisionServiceTest(unittest.TestCase):

    def test_result_dict(self):

        self.assertDictEqual(Result().success(),{'code': 'success'})
        self.assertDictEqual(Result().success("data"),{'code': 'success', 'data': 'data'})
        self.assertDictEqual(Result().fail(),{'code': 'fail'})
        self.assertDictEqual(Result().fail(code="cod11e",msg="msg11"),{'code': 'cod11e', 'msg': 'msg11'})

