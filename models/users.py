import datetime
import sqlite3


class AbstractClassError(Exception):
    print('Dis is an abstract class u dummy')


class BasicModel:
    _FIELDS_MAPPING = {}

    def __getattr__(self, item):
        if item in self._FIELDS_MAPPING.keys():
            return self._FIELDS_MAPPING[item]
        raise AttributeError

    def __setattr__(self, key, value):
        if key in self._FIELDS_MAPPING.keys():
            self._FIELDS_MAPPING[key] = value
        raise AttributeError

    def __init__(self):
        raise AbstractClassError

    def print_info(self):
        for value in self._FIELDS_MAPPING:
            print(value + " = " + self._FIELDS_MAPPING[value])


class User(BasicModel):
    _FIELDS_MAPPING = {
        'nickname': str,
        'join_date': datetime,
        'password': str,
        'email': str,
        'birth_date': datetime,
        'status': str
    }

    def login(self, password, nickname):
        pass

    def logout(self, password, nickname):
        pass
    
    def __init__(self, nickname, join_date, password):
        self.nickname = nickname
        self.join_date = join_date
        self.password = password
        self.status = self.__class__.__name__


class Moderator(User):
    def __init__(self, nickname, join_date, password, service_count):
        super().__init__(nickname, join_date, password)
        self.service_count = service_count

    @staticmethod
    def ban(nickname):
        users[nickname].banned = True

    @staticmethod
    def unban(nickname):
        users[nickname].banned = False

    def set_chat_timeout(self, nickname, seconds):
        pass

    def ban_channel(self, nickname):
        pass



    
