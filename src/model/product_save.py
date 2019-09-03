class ProductSave(object):

    @property
    def code(self):
        return self.code

    @code.setter
    def code(self, value):
        self.code = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

