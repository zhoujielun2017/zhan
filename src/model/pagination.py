class Pagination(object):

    def __init__(self, page=1, page_size=10):
        self.page = int(page) if page else 1
        self.page_size = int(page_size) if page_size else 10

    @property
    def start(self):
        return (self.page - 1) * self.page_size

    @property
    def end(self):
        return self.page * self.page_size
