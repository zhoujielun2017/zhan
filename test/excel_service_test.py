import unittest

from service import division_service
import pyexcel
import hashlib

class DivisionServiceTest(unittest.TestCase):

    def test_excel(self):
        # make sure you had pyexcel-xls installed
        a_list_of_dictionaries = [
            {
                "Name": 'Adam',
                "Age": 28
            },
            {
                "Name": 'Beatrice',
                "Age": 29
            },
            {
                "Name": 'Ceri',
                "Age": 30
            },
            {
                "Name": 'Dean',
                "Age": 26
            }
        ]
        pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")

    def test_if(self):
        x = 2
        y = 3

        if x > y:
            print(x)
        else:
            print(y)

        res = 'aaaaa' if x > y else 'bbbbbbb'  # 三元表达式
        print(res)


    def test_md5(self):
        m = hashlib.md5()
        m.update(b'zxcvzxcvgithub.com')
        print(m.hexdigest())