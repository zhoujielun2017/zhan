# -*- coding:utf-8 -*-
class Const(object):
    class ConsError(TypeError):
        pass

    class ConstCaseError(ConsError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise (self.ConsError, "Can't change const.%s" % name)
        if not name.isupper():
            raise (self.ConstCaseError, "const name '%s' is not all uppercase" % name)
        self.__dict__[name] = value


const = Const()
# gift card
const.GIFT_CARD_USED = 2
const.GIFT_CARD_EXPIRE = -1
const.GIFT_VALID = 1
const.GIFT_NOT_BIND = 0
# session
const.SESSION_USER_ID = "user_id"
const.SESSION_MOBILE = "mobile"
const.SESSION_CAPTCHA = "captcha"

# 1 待支付 2 已支付 3 待发货 4 已发货 5 待收货 6 已收货 7 待评价 8 已评价
const.ORD_WAIT_PAY = 1
const.ORD_PAID = 2
const.ORD_WAIT_SEND = 3
const.ORD_HAD_SEND = 4
const.ORD_WAIT_RECEIVE = 5
const.ORD_HAD_RECEIVE = 6
const.ORD_WAIT_COMMENT = 7
const.ORD_HAD_COMMENT = 8
