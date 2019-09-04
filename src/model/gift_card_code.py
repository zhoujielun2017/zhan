class GiftCardCode(object):

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value

    @property
    def print(self):
        return self._print

    @print.setter
    def print(self, value):
        self._print = value

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    def code(self):
        return str(self.area)+str(self.year)+str(self.unit)+str(self.print)+str(self.num)
