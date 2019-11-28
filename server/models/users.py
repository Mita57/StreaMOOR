import datetime
from .BasicModel import BasicModel
from flask_sqlalchemy import SQLAlchemy

class User(BasicModel):
    _DATABASE = 'streamoor.db'
    _TABLE = 'users'
    _USER = 'root'
    _PASSWORD = 'MOORMOOR'
    _HOST = '127.0.0.1'

    nickname: str
    join_date: datetime
    password: str
    img: str
    email: str
    description: str
    birth_date: datetime
    status: str




    _FIELDS_MAPPING = {
        'nickname': str,  # primary key
        'join_date': datetime,
        'password': str,
        'img': str,
        'email': str,
        'description': str,
        'birth_date': datetime,
        'status': str,
    }

    def login(self, password, nickname):
        pass

    def logout(self, nickname):
        pass

    def __init__(self, nickname, join_date, password, email, birth_date):
        self.nickname = nickname
        self.join_date = join_date
        self.password = password
        self.email = email
        self.status = type(self).__name__
        self.birth_date = birth_date


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
    }

    def __init__(self, nickname, join_date, password, service_count, email, birth_date):
        super().__init__(nickname, join_date, password, email, birth_date)
        self.service_count = service_count

    @staticmethod
    def ban(nickname):
        pass

    @staticmethod
    def unban(nickname):
        pass

    @staticmethod
    def set_chat_timeout(nickname, seconds):
        pass
