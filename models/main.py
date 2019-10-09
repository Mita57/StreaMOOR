import datetime

class abstract_class_init_exception(Exception):
    print('This class is abstact you pillock')

#abstract af
class user:
    nickname
    join_date
    password
    banned
    def __init__(self):
        raise abstract_class_init_exception

    def login(self, password, nickname):
        pass

    def logout(self, password, nickname):
        pass



class moderator(user):
    def __init__(self, nickname, join_date, password, service_count):
        self.nickname = nickname
        self.join_date = join_date
        self.service_count = service_count
        self.password = password

    def delete_chat_message(self):
        pass

    def ban (self, nickname):
        regular_users[nickname].banned = True

    def unban(self, nickname):
        regular_users[nickname].banned = False;
