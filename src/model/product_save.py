class ProductSave(object):

    def __init__(self) -> None:
        self.id = None
        self.price = None
        self.code = None
        self.title = None
        self.content = None
        self.main_pic = None
        self.pics = None

    def to_update(self):
        dd = {
            "title": self.title,
            "content": self.content,
            "price": self.price,
            "main_pic": self.main_pic,
            "pics": self.pics}
        for k, v in list(dd.items()):
            if not v:
                dd.pop(k)
        return dd
