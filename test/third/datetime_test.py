import datetime
import time
import unittest


class ProductServiceTest(unittest.TestCase):
    def test_something(self):
        print(int(time.time()))
        print(datetime.datetime.fromtimestamp(int(time.time())).date().isoformat())


