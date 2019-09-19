import os
import unittest

import pyexcel


class ExcelServiceTest(unittest.TestCase):

    def setUp(self) -> None:
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
        self.file = "your_file.xls"
        pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name=self.file)
        self.assertTrue(os.path.exists(self.file))

    def tearDown(self) -> None:
        os.remove(self.file)

    def test_pass(self):
        pass
