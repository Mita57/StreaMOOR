from .BasicModel import BasicModel


class Subsctiption(BasicModel):
    _DATABASE = 'streamoor.db'
    _TABLE = 'suscriptions'

    _FIELDS_MAPPING = {
        'user': str,  # foreign key
        'subscribed_to': str,  # foreign key
    }

    def subscribe(self, subscribed_to_nickname):

