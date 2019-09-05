# -*- coding: utf-8 -*-
import math

import mongoengine

from mongoengine.queryset import MultipleObjectsReturned, DoesNotExist, QuerySet
from mongoengine import ValidationError


class MongoEnginePaginationException(Exception):
    pass


class BaseQuerySet(QuerySet):
    """
    A base queryset with handy extras
    """

    def paginate(self, page, page_size, error_out=True):
        return Pagination(self, page, page_size)

    def paginate_field(self, field_name, doc_id, page, page_size,
                       total=None):
        item = self.get(id=doc_id)
        count = getattr(item, field_name + "_count", '')
        total = total or count or len(getattr(item, field_name))
        return ListFieldPagination(self, field_name, doc_id, page, page_size,
                                   total=total)


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

    @property
    def pages(self):
        """The total number of pages"""
        return int(math.ceil(self.total / float(self.page_size)))

    def prev(self, error_out=False):
        """Returns a :class:`Pagination` object for the previous page."""
        assert self.iterable is not None, 'an object is required ' \
                                          'for this method to work'
        iterable = self.iterable
        if isinstance(iterable, QuerySet):
            iterable._skip = None
            iterable._limit = None
            iterable = iterable.clone()
        return self.__class__(iterable, self.page - 1, self.page_size)

    @property
    def prev_num(self):
        """Number of the previous page."""
        return self.page - 1

    @property
    def has_prev(self):
        """True if a previous page exists"""
        return self.page > 1

    def next(self, error_out=False):
        """Returns a :class:`Pagination` object for the next page."""
        assert self.iterable is not None, 'an object is required ' \
                                          'for this method to work'
        iterable = self.iterable
        if isinstance(iterable, QuerySet):
            iterable._skip = None
            iterable._limit = None
            iterable = iterable.clone()
        return self.__class__(iterable, self.page + 1, self.page_size)

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.pages

    @property
    def next_num(self):
        """Number of the next page"""
        return self.page + 1

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=3, right_edge=2):
        """Iterates over the page numbers in the pagination.  The four
        parameters control the thresholds how many numbers should be produced
        from the sides.  Skipped page numbers are represented as `None`.
        This is how you could render such a pagination in the templates:

        .. sourcecode:: html+jinja

            {% macro render_pagination(pagination, endpoint) %}
              <div class=pagination>
              {%- for page in pagination.iter_pages() %}
                {% if page %}
                  {% if page != pagination.page %}
                    <a href="{{ url_for(endpoint, page=page) }}">{{ page }}</a>
                  {% else %}
                    <strong>{{ page }}</strong>
                  {% endif %}
                {% else %}
                  <span class=ellipsis>…</span>
                {% endif %}
              {%- endfor %}
              </div>
            {% endmacro %}
        """
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
                    (num > self.page - left_current - 1 and
                     num < self.page + right_current) or \
                    num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


class ListFieldPagination(Pagination):

    def __init__(self, queryset, field_name, doc_id, page, page_size,
                 total=None):
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
        self.doc_id = doc_id
        self.field_name = field_name

        start_index = (page - 1) * page_size

        field_attrs = {field_name: {"$slice": [start_index, page_size]}}

        self.items = getattr(queryset().fields(**field_attrs
                                               ).first(), field_name)

        self.total = total or len(self.items)

        if not self.items and page != 1:
            raise MongoEnginePaginationException()

    def prev(self, error_out=False):
        return self.page > 1

    def next(self, error_out=False):
        return self.page*self.page_size < self.total

    def to_dict(self):
        queryset = list(map(lambda employee: employee.to_dict(), list(self.queryset)))
        return {
            "page": self.page,
            "page_size": self.page_size,
            "total": self.total,
            "prev": self.prev(),
            "next": self.next(),
            "list": queryset
        }
