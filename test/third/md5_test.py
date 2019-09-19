import hashlib
import unittest


class MD5Test(unittest.TestCase):

    def test_md5(self):
        m = hashlib.md5()
        m.update(b'zxcvzxcvgithub.com')
        self.assertEqual(m.hexdigest(), "dd1d964df1f16b047d6c814fd5037674")
