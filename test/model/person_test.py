import unittest

from mongoengine import connect, disconnect, Document, StringField


class Person(Document):
    name = StringField()


class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_thing(self):
        pers = Person(name='John')
        pers.save()

        fresh_pers = Person.objects().first()
        self.assertEqual(fresh_pers.name, 'John')
