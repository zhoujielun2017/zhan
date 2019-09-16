class Result(object):

    def __init__(self) -> None:
        self._data = None
        self._code = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def success(self, *args):
        if args:
            return {"code": "success", "data": args[0]}
        return {"code": "success"}

    def fail(self, **kwargs):
        if kwargs:
            if not kwargs.get("msg"):
                return {"code": kwargs.get("code")}
            return {"code": kwargs.get("code"), "msg": kwargs.get("msg")}
        return {"code": "fail"}
