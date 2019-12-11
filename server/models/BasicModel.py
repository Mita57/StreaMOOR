from contextlib import closing
import psycopg2


class AbstractClassError(Exception):
    pass


class SQLModel:
    _TABLE = None
    _DATABASE = None
    _USER = None
    _PASSWORD = None
    _HOST = None
    _PORT = None

    def __init__(self):
        raise AbstractClassError

    @classmethod
    def _connect(cls):
        """
        connects to the POSTGRESQL batabase
        Returns:
        Connection to postgres
        """
        return psycopg2.connect(database=cls._DATABASE,  user=cls._USER,
                                password=cls._PASSWORD, host=cls._HOST, port=cls._PORT)

    @classmethod
    def query(cls, query, attrs=None):
        """
        Performs a query than us not specified in the other methods
        Args:
            query; a query to be executed
            attrs: a set of attributes, if needed of the query
        """
        conn = cls._connect(cls._DATABASE)
        cur = conn.cursor()
        if attrs:
            cur.execute(query, attrs)
        else:
            cur.execute(query)
        conn.commit()
        conn.close()

    @classmethod
    def normalize_cols(cls, cols):
        new_cols = ''
        for x in cols:
            new_cols += str(x) + ', '
        new_cols = new_cols[0:-2]
        return new_cols

    @classmethod
    def insert(cls, values):
        """
            Inserts the data into the database
            args:
                values: the values to be inserted into the database
        """
        with closing(psycopg2.connect(database='streamoor', user='postgres', password='3395925000',
                                      host='127.0.0.1', port='5432')) as conn:
            with conn.cursor() as cursor:
                sql_insert_query = """INSERT INTO {} VALUES {} """.format(cls._TABLE, values)
                cursor.execute(sql_insert_query)
                conn.commit()

    @classmethod
    def get_by_attrs(cls, cols, attr_cols, attr_values, group_by=None, order_by=None):
        """
            Gets the values from the database that correspond to the values given
            attrs:
                cols: columns that will be returned : list
                attr_cols: columns that will be used in the WHERE statement : list
                attr_values: values that will be used in the WHERE statement according to the attr_cols : list
                group_by: set None as default, if it is given, then the query result is grouped by this arg
                sorted_by: set None as defaul, if it si given, then they query result is sorted by this arg
            returns:
                query result as a dictionary
        """
        new_cols = cls.normalize_cols(cols)
        with closing(psycopg2.connect(database='streamoor', user='postgres', password='3395925000',
                                      host='127.0.0.1', port='5432')) as conn:
            with conn.cursor() as cursor:
                if group_by is None and order_by is None:
                    sql_select_query = """SELECT {} FROM {} WHERE {}='{}' """.format(new_cols, cls._TABLE, attr_cols, attr_values)
                    cursor.execute(sql_select_query)
                    value = cursor.fetchall()
                    return value
                if group_by is not None and order_by is None:
                    sql_select_query = """SELECT {} FROM {} WHERE {}='{}' GROUP BY {}""".format(new_cols, cls._TABLE, attr_cols, attr_values, group_by)
                    cursor.execute(sql_select_query)
                    value = cursor.fetchall()
                    return value
                if group_by is None and order_by is not None:
                    sql_select_query = ("""SELECT {} FROM {} WHERE {} = '{}' ORDER BY {}""").format(new_cols, cls._TABLE, attr_cols, attr_values, order_by)
                    cursor.execute(sql_select_query)
                    value = cursor.fetchall()
                    return value
                else:
                    sql_select_query = """SELECT {} FROM {} WHERE {}='{}' GROUP BY {} ORDER BY {}""".format(
                        new_cols, cls._TABLE, attr_cols, attr_values, group_by, order_by)
                    cursor.execute(sql_select_query)
                    value = cursor.fectchall()
                    return value

    @classmethod
    def update_by_attrs(cls, columns, values, attr_cols, attr_values):
        """
            Updates the values in the database that correspond to the values given
            attrs:
                columns: columns that will be updated : list
                values: values that will be inserted into the DB in accordance to columns : list
                attr_cols: columns that will be used in the WHERE statement : list
                attr_values: values that will be used in the WHERE statement according to the attr_cols : list
        """
        new_cols = cls.normalize_cols(columns)
        with closing(psycopg2.connect(database='streamoor', user='postgres', password='3395925000',
                                      host='127.0.0.1', port='5432')) as conn:
            with conn.cursor() as cursor:
                sql_update_query = """UPDATE {} SET {}=%s WHERE {}=%s""".format(cls._TABLE, new_cols, attr_cols)
                cursor.execute(sql_update_query, (values, attr_values))

    @classmethod
    def delete_by_attrs(cls, attr_cols, attr_values):
        """
            Deletes the rows in the database that correspond to the values given
            attrs:
                attr_cols: columns that will be used in the WHERE statement : list
                attr_values: values that will be used in the WHERE statement according to the attr_cols : list
        """
        with closing(psycopg2.connect(database='streamoor', user='postgres', password='3395925000',
                                      host='127.0.0.1', port='5432')) as conn:
            with conn.cursor() as cursor:
                sql_delete_query = """DELETE FROM {} where {}=%s""".format(cls._TABLE, attr_cols)
                cursor.execute(sql_delete_query, attr_values)


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
        """
         prints all the attributes of the object
        """
        for value in self._FIELDS_MAPPING:
            print(str(value) + " = " + str(self.__dict__[value]))