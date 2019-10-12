import datetime
import sqlite3


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


class User(BasicModel):
    _FIELDS_MAPPING = {
        'nickname': str,
        'join_date': datetime,
        'password': str,
        'email': str,
        'birth_date': datetime,
    }

    def login(self, password, nickname):
        pass

    def logout(self, password, nickname):
        pass
    
    def __init__(self, nickname, join_date, password):
        self.nickname = nickname
        self.join_date = join_date
        self.password = password


class Moderator(user):
    def __init__(self, nickname, join_date, password, service_count):
        self.nickname = nickname
        self.join_date = join_date
        self.service_count = service_count
        self.password = password

    def delete_chat_message(self):
        pass

    @staticmethod
    def ban(self, nickname):
        users[nickname].banned = True

    @staticmethod
    def unban(self, nickname):
        users[nickname].banned = False

    def set_chat_timeout(self, nickname, seconds):
        pass

    def ban_channel(self, nickname):
        pass

    
