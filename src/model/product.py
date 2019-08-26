from mongoengine import *
import datetime

connect(alias='product', db='product')


class Product(Document):

    # productid = StringField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'db_alias': 'product'}


if __name__ == '__main__':
    start = datetime.datetime.now()
    print(start)
    ord = Product()
    print(dir(ord))
    print(type(ord))
    print(ord.__dict__)
    end = datetime.datetime.now()
    print(end-start)