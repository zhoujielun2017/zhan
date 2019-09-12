import datetime
import time
import unittest


class A:
    name = "A"

    def get_name(self):
        print(self.name)

    def set_name(self, value):
        self.name = value

class ProductServiceTest(unittest.TestCase):
    def test_something(self):
        print(int(time.time()))
        print(datetime.datetime.fromtimestamp(int(time.time())).date().isoformat())

    def test_getattr(self):
        a = A()
        b = A()
        b.name = "B"
        na = getattr(a, "name")  # 输出:A   获得name属性
        print(na)
        b.get_name()


def test_arg(**kwargs):
    print(kwargs)


test_arg(mobile__contains="12368877399")
