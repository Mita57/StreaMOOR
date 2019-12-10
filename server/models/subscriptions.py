from .BasicModel import BasicModel
from .users import User


class Subsctiption(BasicModel):
    _DATABASE = 'streamoor'
    _TABLE = 'subscriptions'
    _USER = 'root'
    _PASSWORD = 'MOORMOOR'
    _HOST = '127.0.0.1'

    _FIELDS_MAPPING = {
        'user': str,  # foreign key
        'subscribed_to': str,  # foreign key
    }

    def __init__(self, user, subscribed_to):
        self.user = user
        self.subscribe_to = subscribed_to

    def subscribe(self):
        """
        adds the subscription info to the database
        """
        BasicModel.insert(Subsctiption, values=[self.user, self.subscribe_to])
        User.update_by_attrs('subs', 'subs + 1', 'nickname', self.subscribe_to)

    def unsubscribe(self):
        """
        removes the subscription info from the database
        :return:
        """
        BasicModel.delete_by_attrs(Subsctiption, values=[self.user, self.subscribe_to])
        User.update_by_attrs('subs', 'subs - 1', 'nickname', self.subscribe_to)
