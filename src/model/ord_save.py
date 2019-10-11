from model.ord_product import OrdProduct


class OrdSave(object):

    def __init__(self) -> None:
        self.ord_id = None
        self.user_id = None
        # productid_num [{id:id,num:num,title:title}]
        self.pros = []
        self.areas = []
        # 收货人
        self.name = None
        # 收货电话
        self.mobile = None
        # 收货地址
        self.address = None
        # gift_code
        self.gift_card_code = None
        # gift_card_id
        self.gift_card_id = None
        # status
        self.status = None

    def add_product(self, ord_product: OrdProduct):
        self.pros.append(ord_product)

    def to_ord_product(self):
        return []
