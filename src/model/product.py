import datetime

from mongoengine import *

from mongoenginepagination import Document

connect(alias='product', db='product')


class Product(Document):

    code = StringField()
    title = StringField()
    # 内容
    content = StringField()
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
                "content": self.content,
                "main_pic": self.main_pic,
                "pics": self.pics,
                "create_time": self.create_time.strftime( '%Y-%m-%d %H:%M:%S'),
                "update_time": self.update_time.strftime( '%Y-%m-%d %H:%M:%S')}


if __name__ == '__main__':
    start = datetime.datetime.now()
    print(start)
    ord = Product()
    print(dir(ord))
    print(type(ord))
    print(ord.__dict__)
    end = datetime.datetime.now()
    print(end-start)