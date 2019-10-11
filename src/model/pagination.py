class Pagination(object):

    def __init__(self, page=1, page_size=10):
        self.page = int(page)
        self.page_size = int(page_size)

    @property
    def start(self):
        return (self.page - 1) * self.page_size

    @property
    def end(self):
        return self.page * self.page_size
