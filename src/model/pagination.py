class Pagination(object):

    def __init__(self,page:int,page_size:int):
        self.page = 1
        self.page_size = 10

    @property
    def start(self):
        return (self.page - 1) * self.page_size

    @property
    def end(self):
        return self.page * self.page_size
