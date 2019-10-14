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
        'status': str,
        'banned': bool
    }

    def login(self, password, nickname):
        pass

    def logout(self, password, nickname):
        pass

    def __init__(self, nickname, join_date, password, email, birth_date):
        self._FIELDS_MAPPING['nickname'] = nickname
        self._FIELDS_MAPPING['join_date'] = join_date
        self._FIELDS_MAPPING['password'] = password
        self._FIELDS_MAPPING['email'] = email
        self._FIELDS_MAPPING['status'] = type(self).__name__
        self._FIELDS_MAPPING['birth_date'] = birth_date
        self._FIELDS_MAPPING['banned'] = False


class Moderator(User):
    def __init__(self, nickname, join_date, password, service_count, email, birth_date):
        super().__init__(nickname, join_date, password, email, birth_date)
        self._FIELDS_MAPPING['service_count'] = service_count

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


user1 = User(nickname="meme-poster", join_date=datetime.datetime(2019, 5, 17), password="mamkuvkinovodil", email= 'mamkatvoya@gmail.com', birth_date=datetime.datetime(2000, 4, 18))
user2 = Moderator(nickname="Vitas", join_date=datetime.datetime(2019, 5, 17), password="7element", email= 'AAAAAAAAA@gmail.com', birth_date=datetime.datetime(1979, 4, 13), service_count=69)
users = [user1, user2]

try:
    User.query("""CREATE TABLE users (nickname VARCHAR(20) PRIMARY KEY, join_date DATE, password VARCHAR(20), email VARCHAR(30), status VARCHAR(10), birth_date DATE, banned bit )""")
except sqlite3.OperationalError:
    pass

for X in users:
    User.query(
        """
            INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?) """, (X['nickname'], X['join_date'],X['password'],X['email'],X['status'],X['birth_date'],X['banned']))

