import datetime
import sqlite3


class AbstractClassError(Exception):
    print('Dis is an abstract class u dummy')


class SQLModel:
    _DATABASE = None
    _TABLE = None

    @classmethod
    def _connect(cls):
        return sqlite3.connect(cls._DATABASE)

    @classmethod
    def query(cls, query):
        conn = cls._connect()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()


class BasicModel(SQLModel):
    _FIELDS_MAPPING = {}
    _DATABASE = 'users.db'

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
        'nickname': str,                 #id
        'join_date':datetime,
        'password': str,
        'email': str,
        'birth_date': datetime,
        'status': str
    }

    def login(self, password, nickname):
        pass

    def logout(self, password, nickname):
        pass
    
    def __init__(self, nickname, join_date, password, email, birth_date):
        self._FIELDS_MAPPING['nickname'] = nickname
        self._FIELDS_MAPPING['join_date'] = join_date
        self._FIELDS_MAPPING['password'] = password
        self._FIELDS_MAPPING['status'] = type(self).__name__
        self._FIELDS_MAPPING['email'] = email
        self._FIELDS_MAPPING['birth_date'] = birth_date


class Moderator(User):
    def __init__(self, nickname, join_date, password, service_count, email, birth_date):
        super().__init__(nickname, join_date, password, email, birth_date)
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


user1 = User(nickname="meme-poster", join_date=datetime.datetime(2019, 5, 17), password="mamkuvkinovodil", email= 'mamkatvoya@gmail.com', birth_date=datetime.datetime(2000, 18, 4))
user2 = Moderator(nickname="meme-poster", join_date=datetime.datetime(2019, 5, 17), password="mamkuvkinovodil", email= 'mamkatvoya@gmail.com', birth_date=datetime.datetime(2000, 18, 4), service_count=69)
users = [user1, user2]

