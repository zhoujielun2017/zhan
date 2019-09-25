import datetime
import time
import unittest


class A:
    name = "A"

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value


class DateTimeTest(unittest.TestCase):
    def test_time(self):
        self.assertIsInstance(time.time(), float)
        self.assertEqual(datetime.datetime.fromtimestamp(1568858752).date().isoformat(), "2019-09-19")

    def test_getattr(self):
        a = A()
        b = A()
        b.name = "B"
        na = getattr(a, "name")  # 输出:A   获得name属性
        self.assertEqual(na, "A")
        self.assertEqual(b.get_name(), "B")

    def test_if(self):
        x = 2
        y = 3
        res = 'a' if x > y else 'b'  # 三元表达式
        self.assertEqual(res, "b")

    def test_split(self):
        self.assertEqual("0120190101000011"[-6:], "000011")
        self.assertEqual("0120190101000011"[:-6], "0120190101")
