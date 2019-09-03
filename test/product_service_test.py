import hashlib
import unittest
import uuid

import shortuuid as shortuuid

from model.pagination import Pagination
from model.product_save import ProductSave
from service import product_service

class ProductServiceTest(unittest.TestCase):
    def test_something(self):
        a = shortuuid.uuid()
        print("test_something %s" % a)

    def decode_b64(self,str):
        table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                 "6": 6, "7": 7, "8": 8, "9": 9,
                 "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16,
                 "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22, "n": 23,
                 "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
                 "v": 31, "w": 32, "x": 33, "y": 34, "z": 35,
                 "A": 36, "B": 37, "C": 38, "D": 39, "E": 40, "F": 41, "G": 42,
                 "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49,
                 "O": 50, "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56,
                 "V": 57, "W": 58, "X": 59, "Y": 60, "Z": 61,
                 "-": 62, "_": 63}
        result = 0
        for i in range(len(str)):
            result *= 64
            result += table[str[i]]
        return result

    def test_page(self):
        p = Pagination(1, 4)
        product_service.page(p)

    def test_find_by_id(self):
        p = product_service.find_by_id("5d65ff35e0c4f62d92c46dc6")
        self.assertIsNotNone(p,"")

    def test_find_by_code(self):
        p = product_service.find_by_code("5cTJxqUoUPXmucpTPni9ZL")
        self.assertIsNotNone(p,"")

    def test_save(self):
        save = ProductSave()
        save.title="test_product_title"
        save.content="test_product_content"
        product_service.save(save)


if __name__ == '__main__':
    unittest.main()
