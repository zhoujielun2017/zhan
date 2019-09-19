import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='product', db='product')


class Product(Document):
    code = StringField(unique=True)
    title = StringField()
    # 内容
    content = StringField()
    price = IntField()
    # 主图
    main_pic = StringField()

    user_id = StringField()
    # 多图
    pics = StringField()
    # 显示数量
    view_count = LongField()
    # 库存
    stock = IntField()
    create_time = DateTimeField(default=datetime.datetime.utcnow)
    update_time = DateTimeField(default=datetime.datetime.utcnow)
    meta = {'db_alias': 'product'}

    def to_dict(self):
        return {
            "id": str(self.id),
            "code": self.code,
            "title": self.title,
            "content": self.content,
            "price": self.price,
            "main_pic": self.main_pic,
            "pics": self.pics,
            "create_time": self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            "update_time": self.update_time.strftime('%Y-%m-%d %H:%M:%S')}
