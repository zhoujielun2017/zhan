import unittest

from const import const
from model.gift_card_code import GiftCardCode
from model.pagination import Pagination
from service import gift_card_service


class GiftCardServiceTest(unittest.TestCase):

    def setUp(self):
        r = GiftCardCode()
        r.area = "01"
        r.print = "01"
        r.year = "2019"
        r.unit = "01"
        r.num = "000011"
        self.code = r
        self.assertEqual(self.code.code(), "0120190101000011")
        gift_card_service.save(self.code)

    def tearDown(self):
        gift_card = gift_card_service.find_by_code(self.code.code())
        gift_card_service.delete(gift_card.id)
        gift_card = gift_card_service.find_by_code(self.code.code())
        self.assertIsNone(gift_card)

    def test_find_by_code(self):
        return gift_card_service.find_by_code(self.code.code())

    def test_update_used(self):
        gift_card = gift_card_service.find_by_code(self.code.code())
        gift_card_service.update_used(gift_card.code, gift_card.password)
        gift_card2 = gift_card_service.find_by_code(self.code.code())
        self.assertEqual(gift_card2.status, const.GIFT_CARD_USED)

    def test_page(self):
        r = Pagination(1, 10)
        pros = gift_card_service.page(r)
        self.assertGreater(pros.total, 0)
