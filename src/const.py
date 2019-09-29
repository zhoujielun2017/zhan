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
