import datetime


#abstract af
class user:

    def login(self, password, nickname):
        pass

    def logout(self, password, nickname):
        pass
    
    def __init__(self, nickname, join_date, password):
        self.nickname = nickname
        self.join_date = join_date
        self.password = password



class moderator(user):
    def __init__(self, nickname, join_date, password, service_count):
        self.nickname = nickname
        self.join_date = join_date
        self.service_count = service_count
        self.password = password

    def delete_chat_message(self):
        pass

    def ban (self, nickname):
        users[nickname].banned = True

    def unban(self, nickname):
        users[nickname].banned = False

    def set_chat_timeout(self, nickname, seconds):
        pass

    def ban_channel(self, nickname):
        pass

    
