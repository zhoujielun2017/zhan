class OrdSave(object):

    def __init__(self) -> None:
        self._ord_id = None
        self._user_id = None
        # productid_num
        self._pros = []
        self._areas = []
        # 收货人
        self._name = None
        # 收货电话
        self._mobile = None
        # 收货地址
        self._address = None

    @property
    def ord_id(self):
        return self._ord_id

    @ord_id.setter
    def ord_id(self, value):
        self._ord_id = value

    @property
    def pros(self):
        return self._pros

    @pros.setter
    def pros(self, value):
        self._pros = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def areas(self):
        return self._areas

    @areas.setter
    def areas(self, value):
        self._areas = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
