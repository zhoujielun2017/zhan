import random
import sys
import unittest

from model.gift_card_code import GiftCardCode
from model.pagination import Pagination

sys.path.append('../')
from service import gift_card_service


class GiftCardServiceTest(unittest.TestCase):

    def test_random(self):
        r = random.randint(100000000, 999999999)
        print(r)
        print(len(str(r)))
        r1 = random.randint(100000000, 999999999)
        r2 = random.randint(100000000, 999999999)
        print(str(r1) + "" + str(r2))

    def test_save(self):
        r = GiftCardCode()
        r.area = "01"
        r.print = "01"
        r.year = "2019"
        r.unit = "01"
        r.num = "000011"
        gift_card_service.save(r)

    def test_find_by_code(self):
        r = GiftCardCode()
        r.area = "01"
        r.print = "01"
        r.year = "2019"
        r.unit = "01"
        r.num = "01"
        return gift_card_service.find_by_code(r.code())

    def test_delete(self):
        gift_card_service.delete("5d70704398df4d69582faf46")

    def test_update_used(self):
        gift_card_service.update_used("0120190101000011", "766326562130472281")

    def test_page(self):
        r = Pagination(2, 10)
        pros = gift_card_service.page(r)
        # self.assertEqual(pros.)
        print(pros.to_dict())
