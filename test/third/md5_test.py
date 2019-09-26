import hashlib
import unittest


class MD5Test(unittest.TestCase):

    def test_md5(self):
        m = hashlib.md5()
        m.update(b'zxcvzxcvgithub.com')
        self.assertEqual(m.hexdigest(), "dd1d964df1f16b047d6c814fd5037674")
        m2 = hashlib.md5()
        m2.update(b'zxcvzxcv163.com')
        self.assertEqual("4b6a58b00c956becde7f4ce4df207aa3", m2.hexdigest())
