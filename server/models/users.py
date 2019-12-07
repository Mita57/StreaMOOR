import datetime
from .BasicModel import BasicModel


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
    subs: int
    email: str
    description: str
    birth_date: datetime
    status: str
    banned: bool
    online: bool
    curr_hub: str

    _FIELDS_MAPPING = {
        'nickname': str,
        'email': str,  # primary key
        'password': str,
        'img': str,
        'join_date': datetime,
        'subs': int,
        'description': str,
        'birth_date': datetime,
        'status': str,
        'banned': bool,
        'online': bool,
        'curr_hub': str
    }

    def login(self, password, nickname):
        pass

    def logout(self, nickname):
        pass

    def __init__(self, nickname, email, password, join_date, birth_date):
        self.nickname = nickname
        self.email = email
        self.password = password
        self.join_date = join_date
        self.status = type(self).__name__
        self.birth_date = birth_date
