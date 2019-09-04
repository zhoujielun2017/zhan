class Result(object):

    def __init__(self) -> None:
        self._data=None
        self._code=None
        self._msg=None

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

    def success(self):
        if self._data==None:
            return '{"code": "success"}'
        return '{"code": "success",data:"%s"}' % self._data

    def fail(self):
        return '{"code": "%s","msg":"%s"}' % (self._code,self._msg)