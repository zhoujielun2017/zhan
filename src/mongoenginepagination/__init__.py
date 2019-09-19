# -*- coding: utf-8 -*-

import mongoengine
from mongoengine.queryset import QuerySet


class MongoEnginePaginationException(Exception):
    pass


class BaseQuerySet(QuerySet):
    """
    A base queryset with handy extras
    """

    def paginate(self, page, page_size):
        return Pagination(self, page, page_size)

    def paginate_field(self, page, page_size, **kwargs):
        return ListFieldPagination(self, page, page_size, **kwargs)


class Document(mongoengine.Document):
    """Abstract document with extra helpers in the queryset class"""

    meta = {'abstract': True,
            'queryset_class': BaseQuerySet}


class Pagination(object):

    def __init__(self, iterable, page, page_size):

        if page < 1:
            raise MongoEnginePaginationException()

        self.iterable = iterable
        self.page = page
        self.page_size = page_size
        self.total = len(iterable)

        start_index = (page - 1) * page_size
        end_index = page * page_size

        self.items = iterable[start_index:end_index]
        if isinstance(self.items, QuerySet):
            self.items = self.items.select_related()
        if not self.items and page != 1:
            raise MongoEnginePaginationException()

    def prev(self, error_out=False):
        return self.page > 1

    def next(self, error_out=False):
        return self.page * self.page_size < self.total

    @property
    def next_num(self):
        """Number of the next page"""
        return self.page + 1

    def to_dict(self):
        queryset = list(map(lambda employee: employee.to_dict(), list(self.items)))
        return {
            "page": self.page,
            "page_size": self.page_size,
            "total": self.total,
            "prev": self.prev(),
            "next": self.next(),
            "list": queryset
        }


class ListFieldPagination(Pagination):

    def __init__(self, queryset, page, page_size,
                 **kwargs):
        """Allows an array within a document to be paginated.

        Queryset must contain the document which has the array we're
        paginating, and doc_id should be it's _id.
        Field name is the name of the array we're paginating.
        Page and page_size work just like in Pagination.
        Total is an argument because it can be computed more efficiently
        elsewhere, but we still use array.length as a fallback.
        """
        if page < 1:
            raise MongoEnginePaginationException()

        self.page = page
        self.page_size = page_size

        self.queryset = queryset
        if len(self.queryset) == 0:
            self.total = 0
            print("query set is None")
            return
        self.total = len(self.queryset)
        start_index = (page - 1) * page_size
        if start_index > self.total:
            print("start index greater than total %s %s" % (page, self.total))
            return
        for key, value in list(kwargs.items()):
            if not value:
                kwargs = kwargs.pop(key)
        if not kwargs:
            self.items = self.queryset[start_index:start_index + page_size]
        else:
            self.items = self.queryset(**kwargs)[start_index: start_index + page_size]

        if not self.items and page != 1:
            raise MongoEnginePaginationException()

    def prev(self, error_out=False):
        return self.page > 1

    def next(self, error_out=False):
        return self.page * self.page_size < self.total

    def total(self):
        return self.total

    def to_dict(self):
        queryset = list(map(lambda employee: employee.to_dict(), list(self.items)))
        return {
            "page": self.page,
            "page_size": self.page_size,
            "total": self.total,
            "prev": self.prev(),
            "next": self.next(),
            "list": queryset
        }
