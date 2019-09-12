from mongoengine import ListField, EmbeddedDocumentField, EmbeddedDocument, StringField

from mongoenginepagination import Document


class Comment(EmbeddedDocument):
    content = StringField()


class Page(Document):
    comments = ListField(EmbeddedDocumentField(Comment))


if __name__ == '__main__':
    comment1 = Comment(content='Good work!')
    comment2 = Comment(content='Nice article!')
    page = Page(comments=[comment1, comment2])
    print(page)
