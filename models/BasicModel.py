from contextlib import closing
import psycopg2


class AbstractClassError(Exception):
    pass


class SQLModel:
    _DATABASE = None
    _TABLE = None
    _USER= None
    _PASSWORD = None
    _HOST = None
    _PORT = None

    def __init__(self):
        raise AbstractClassError

    @classmethod
    def _connect(cls):
        return psycopg2.connect(database = cls._DATABASE, table = cls._TABLE, user = cls._USER,
                                password = cls._PASSWORD, host = cls._HOST, port = cls._PORT)

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
    def insert(cls, values):
        values_query = ''
        for X in values:
            values_query += X + ','

        with closing(psycopg2.connect()) as conn:
            with conn.cursor() as cursor:
                sql_insert_query = """INSERT INTO %s VALUES (%s) """
                cursor.execute(sql_insert_query, cls._TABLE, values_query)


    @classmethod
    def get_by_id(cls, elem_id, cols):
        with closing(psycopg2.connect()) as conn:
            with conn.cursor() as cursor:
                sql_select_query = """SELECT %s FROM %s WHERE id=%s """
                cursor.execute(sql_select_query, cols, cls._TABLE, elem_id)

    @classmethod
    def update_by_id(cls, column, value, elem_id):
        with closing(psycopg2.connect()) as conn:
            with conn.cursor() as cursor:
                sql_update_query = """UPDATE %s SET %s=%s WHERE id=%s"""
                cursor.execute(sql_update_query, cls._TABLE, column,value, elem_id)

    @classmethod
    def delete_by_id(cls, value):
        with closing(psycopg2.connect()) as conn:
            with conn.cursor() as cursor:
                sql_delete_query = """DELETE FROM %s where id=%s"""
                cursor.execute(sql_delete_query, cls._TABLE, value)


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

