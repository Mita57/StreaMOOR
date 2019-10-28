from .users import BasicModel


class Hub(BasicModel):
    _DATABASE = 'streamoor.db'
    _TABLE = 'hubs'

    _FIELDS_MAPPING = {
        'name': str,
        'color': str,
        'people_online': int,
        'logo': int,
        'description': int
    }
