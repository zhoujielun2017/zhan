from mongoengine import Document, StringField, ReferenceField


class User(Document):
    name = StringField()


class Page(Document):
    content = StringField()
    author = ReferenceField(User)


if __name__ == '__main__':
    john = User(name="John Smith")
    post = Page(content="Test Page")
    post.author = john
    print(post)
