import datetime
import sqlite3


class AbstractClassError(Exception):
    pass


class SQLModel:
    _DATABASE = None
    _TABLE = None

    def __init__(self):
        raise AbstractClassError

    @classmethod
    def _connect(cls):
        return sqlite3.connect(cls._DATABASE)

    @classmethod
    def query(cls, query, attrs=None):
        conn = cls._connect()
        cur = conn.cursor()
        if attrs:
            cur.execute(query, attrs)
        else:
            cur.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def get_by_pk(cls, pk):
        conn = cls._connect()
        cur = conn.cursor()
        cur.execute(
            """
                SELECT *
                FROM :table
                WHERE id = :pk
            """,
            {'table': cls._TABLE, 'pk': pk}
        )
        result = {}
        record = cur.fetchone()
        for key, val in enumerate(cur.description):
            result[val] = record[key]
        conn.close()
        return result


class BasicModel(SQLModel):
    _FIELDS_MAPPING = {}
    _DATABASE = 'users.db'
    _TABLE = 'users'

    __dict__ = {}

    def __getattr__(self, item):
        if item in self._FIELDS_MAPPING.keys():
            return self.__dict__[item]
        raise AttributeError

    def __setattr__(self, key, value):
        if key in self._FIELDS_MAPPING.keys():
            self.__dict__[key] = value
        raise AttributeError

    def __init__(self):
        raise AbstractClassError

    def print_info(self):
        for value in self._FIELDS_MAPPING:
            print(str(value) + " = " + str(self.__dict__[value]))


class User(BasicModel):
    _FIELDS_MAPPING = {
        'id': int,
        'nickname': str,
        'join_date': datetime,
        'password': str,
        'email': str,
        'birth_date': datetime,
        'status': str,
        'banned': bool
    }

    def login(self, password, nickname):
        pass

    def logout(self, password, nickname):
        pass

    def __init__(self, user_id, nickname, join_date, password, email, birth_date):
        self.__dict__['id'] = user_id
        self.__dict__['nickname'] = nickname
        self.__dict__['join_date'] = join_date
        self.__dict__['password'] = password
        self.__dict__['email'] = email
        self.__dict__['status'] = type(self).__name__
        self.__dict__['birth_date'] = birth_date
        self.__dict__['banned'] = False


class Moderator(User):
    def __init__(self, user_id,  nickname, join_date, password, service_count, email, birth_date):
        super().__init__(user_id, nickname, join_date, password, email, birth_date)
        self.__dict__['service_count'] = service_count

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


user1 = User(user_id=0, nickname="meme-poster", join_date=datetime.datetime(2019, 5, 17), password="mamkuvkinovodil",
             email='mamkatvoya@gmail.com', birth_date=datetime.datetime(2000, 4, 18))

user2 = Moderator(user_id=1, nickname="Vitas", join_date=datetime.datetime(2019, 5, 17), password="7element",
                  email='AAAAAAAAA@gmail.com', birth_date=datetime.datetime(1979, 4, 13), service_count=69)
users = [user1, user2]
user1.print_info()
user2.print_info()

try:
    User.query("""CREATE TABLE users (id INTEGER, nickname VARCHAR(20), join_date DATE, password VARCHAR(20),
     email VARCHAR(30), status VARCHAR(10), birth_date DATE, banned bit )""")
except sqlite3.OperationalError:
    pass
for X in users:
    User.query(
        """
            INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?) """, (X.__getattr__('id'), X.__getattr__('nickname'), X.__getattr__('join_date'), X.__getattr__('password'), X.__getattr__('email'), X.__getattr__('status'), X.__getattr__('birth_date'), X.__getattr__('banned')))

