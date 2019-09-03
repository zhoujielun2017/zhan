class UserSave(object):

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value