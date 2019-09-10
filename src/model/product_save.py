class ProductSave(object):

    def __init__(self) -> None:
        self._code = None
        self._title = None
        self._content = None
        self._main_pic = None
        self._pics = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

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

    @property
    def main_pic(self):
        return self._main_pic

    @main_pic.setter
    def main_pic(self, value):
        self._main_pic = value

    @property
    def pics(self):
        return self._pics

    @pics.setter
    def pics(self, value):
        self._pics = value
