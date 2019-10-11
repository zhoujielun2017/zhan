import unittest

from model.ord_product import OrdProduct
from model.ord_save import OrdSave


class OrdSaveTest(unittest.TestCase):

    def test_add_product(self):
        save = OrdSave()
        p = OrdProduct()
        save.add_product(p)
        save2 = OrdSave()
        p2 = OrdProduct()
        save2.add_product(p2)
        self.assertEqual(len(save2.pros), 1)
        save.color = "#ffff"
        self.assertEqual(save.color, "#ffff")
