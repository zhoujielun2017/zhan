import json
import random
import sys
import unittest

from flask import jsonify

from model.gift_card import GiftCard
from model.gift_card_code import GiftCardCode
from model.pagination import Pagination
from model.result import Result

sys.path.append('../')
from model.user_save import UserSave
from service import user_service, gift_card_service


class GiftCardServiceTest(unittest.TestCase):

    def test_random(self):
        r = random.randint(100000000, 999999999)
        print(r)
        print(len(str(r)))
        r1 = random.randint(100000000, 999999999)
        r2 = random.randint(100000000, 999999999)
        print(str(r1) + "" + str(r2))

    def test_str(self):
        r= Result("success","param error")
        print(json.dumps(r))

    def test_save(self):
        r= GiftCardCode()
        r.area="01"
        r.print="01"
        r.year="2019"
        r.unit="01"
        r.num="000011"
        gift_card_service.save(r)

    def test_find_by_code(self):
        r= GiftCardCode()
        r.area="01"
        r.print="01"
        r.year="2019"
        r.unit="01"
        r.num="01"
        gift_card_service.find_by_code(r.code())

    def test_page(self):
        # r= Pagination(1,10)
        # pros = gift_card_service.page(r)
        # aa = list(map(lambda employee: employee.as_dict(), list(pros)))
        # r = Result()
        # r.data=aa
        print(jsonify({"a":1}))