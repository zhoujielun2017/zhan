from model.ord_product import OrdProduct


class OrdSave(object):
    ord_id = None
    user_id = None
    # productid_num [{id:id,num:num,title:title}]
    pros = []
    areas = []
    # 收货人
    name = None
    # 收货电话
    mobile = None
    # 收货地址
    address = None
    # gift_code
    gift_card_code = None
    # gift_card_id
    gift_card_id = None
    # status
    status = None

    def add_product(self, ord_product: OrdProduct):
        self.pros.append(ord_product)

    def to_ord_product(self):
        return []
