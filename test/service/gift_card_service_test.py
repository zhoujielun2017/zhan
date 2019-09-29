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
        gift_card = gift_card_service.find_by_code(self.code.code())
        if not gift_card:
            gift_card = gift_card_service.save(self.code)
            self.assertEqual(gift_card.status, const.GIFT_NOT_BIND)

    def tearDown(self):
        gift_card = gift_card_service.find_by_code(self.code.code())
        gift_card_service.delete(gift_card.id)
        gift_card = gift_card_service.find_by_code(self.code.code())
        self.assertIsNone(gift_card)

    def test_bind_product(self):
        gift_card_service.update_bind_product([self.code.code()], "test_product_id")
        gift_card = gift_card_service.find_by_code(self.code.code())
        self.assertEqual(gift_card.status, const.GIFT_VALID)

    def test_find_by_code(self):
        return gift_card_service.find_by_code(self.code.code())

    def test_update_used(self):
        gift_card = gift_card_service.find_by_code(self.code.code())
        gift_card_service.update_used(gift_card.code, gift_card.password)
        gift_card2 = gift_card_service.find_by_code(self.code.code())
        self.assertEqual(gift_card2.status, const.GIFT_CARD_USED)

    def test_page(self):
        self.test_update_used()
        r = Pagination(1, 10)
        pros = gift_card_service.page(r, status=const.GIFT_CARD_USED)
        for item in pros.items:
            self.assertEqual(item.status, const.GIFT_CARD_USED)
        self.assertGreater(pros.total, 0)

    def test_page_status_1(self):
        self.test_bind_product()
        r = Pagination(1, 10)
        pros = gift_card_service.page(r, status=const.GIFT_VALID)
        for item in pros.items:
            self.assertEqual(item.status, const.GIFT_VALID)
        self.assertGreater(pros.total, 0)
