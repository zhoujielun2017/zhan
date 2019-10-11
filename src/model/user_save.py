class UserSave(object):

    def __init__(self) -> None:
        self.head_url = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = str(value)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = str(value)
