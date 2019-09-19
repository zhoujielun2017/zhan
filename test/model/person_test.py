import hashlib
import unittest

from mongoengine import connect, disconnect, Document, StringField


class Person(Document):
    name = StringField()


@unittest.skip
class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls):
        disconnect()

    @unittest.skip
    def test_thing(self):
        pers = Person(name='John')
        pers.save()

        fresh_pers = Person.objects().first()
        self.assertEqual(fresh_pers.name, 'John')

    @unittest.skip
    def test_md5(self):
        m = hashlib.md5()
        # m.update(b'zxcvzxcv163.com')
        # print(m.hexdigest())
        m.update(b'zxcvzxcvgithub.com')
        print(m.hexdigest())
