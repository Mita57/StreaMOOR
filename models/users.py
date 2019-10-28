import datetime
import psycopg2


class AbstractClassError(Exception):
    pass


class SQLModel:
    _DATABASE = None
    _TABLE = None

    def __init__(self):
        raise AbstractClassError

    @classmethod
    def _connect(cls):
        return psycopg2.connect(cls._DATABASE)

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

    def __getattr__(self, item):
        if item in self._FIELDS_MAPPING.keys():
            return self.__dict__[item]
        raise AttributeError

    def __setattr__(self, key, value):
        if key in self._FIELDS_MAPPING.keys():
            print(value)
            self.__dict__[key] = value
        else:
            raise AttributeError

    def __init__(self):
        raise AbstractClassError

    def print_info(self):
        for value in self._FIELDS_MAPPING:
            print(str(value) + " = " + str(self.__dict__[value]))


class User(BasicModel):
    _DATABASE = 'streamoor.db'
    _TABLE = 'users'

    _FIELDS_MAPPING = {
        'nickname': str,
        'join_date': datetime,
        'password': str,
        'img': str,
        'email': str,
        'description': str,
        'birth_date': datetime,
        'status': str,
        'banned': bool,
        'online': bool,
        'watching_now': int
    }

    def login(self, password, nickname):
        pass

    def logout(self, nickname):
        pass

    def __init__(self, nickname, join_date, password, email, birth_date, watching_now):
        self.nickname = nickname
        self.join_date = join_date
        self.password = password
        self.email = email
        self.status = type(self).__name__
        self.birth_date = birth_date
        self.banned = False
        self.online = True
        self.watching_now = watching_now


class Moderator(User):

    _FIELDS_MAPPING = {
        'nickname': str,
        'join_date': datetime,
        'password': str,
        'email': str,
        'img': str,
        'birth_date': datetime,
        'description': str,
        'status': str,
        'service_count': int,
        'banned': bool,
        'online': bool,
        'watching_now': int
    }

    def __init__(self, nickname, join_date, password, service_count, email, birth_date, watching_now):
        super().__init__(nickname, join_date, password, email, birth_date, watching_now)
        self.service_count = service_count

    @staticmethod
    def ban(nickname):
        users[nickname].banned = True

    @staticmethod
    def unban(nickname):
        users[nickname].banned = False

    @staticmethod
    def set_chat_timeout(nickname, seconds):
        pass

