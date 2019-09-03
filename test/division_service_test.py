import unittest

from service import division_service


class DivisionServiceTest(unittest.TestCase):

    def test_read(self):
        save = division_service.read()
        print(save)

