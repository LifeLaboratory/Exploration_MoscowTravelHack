import psycopg2
import os
from psycopg2.extras import RealDictCursor

from app.settings import DATABASES, BASE_DIR


class Provider:
    """
    Базовый класс для работы с БД
    """
    def __init__(self, sql_root=None):
        """
        При совершение запроса
        """
        self.query = None
        self.connect, self.current_connect = Provider.connect()
        self.sql_root = sql_root

    def __del__(self):
        """
        После завершения обработки запроса
        """
        self.connect.commit()
        self.connect.close()

    @staticmethod
    def import_sql(sql_root, name):
        with open(os.path.join(BASE_DIR, sql_root, name), encoding='utf-8', mode='r') as _fne:
            return _fne.read()

    def exec_by_file(self, name, params=None):
        query = self.import_sql(self.sql_root, name)
        return self.exec(query, params)

    def execute(self):
        return self.exec(self.query)

    @staticmethod
    def connect():
        """
        Метод подключения к бд
        :return:
        """
        config_connect = "dbname='{NAME}' user='{USER}' host='{HOST}' password='{PASSWORD}'"
        connect = psycopg2.connect(config_connect.format(**DATABASES['default']))
        return connect, connect.cursor(cursor_factory=RealDictCursor)

    @staticmethod
    def exec(query=None, args=None, file=None):
        """
        Метод для выполнения sql запроса
        :param query:
        :param args:
        :param file:
        :return:
        """
        return Provider._switch(query=query, args=args, file=file)

    @staticmethod
    def _switch(query=None, args=None, file=None):
        """
        Метод разводящий - для выбора режима sql запроса
        с аргументами
        без аргументов
        файл с аргументами
        файл без аргументов
        :param query:
        :param args:
        :param file:
        :return:
        """
        if query and args:
            return Provider._query_exec_args(query, args)
        if query and not args:
            return Provider._query_exec(query)
        if file and args:
            return Provider._query_file_args_exec(file, args)
        if file:
            return Provider._query_file_exec(file)
        return

    @staticmethod
    def _query_exec(query):
        """
        Выполнить sql без аргументов
        :param query:
        :return:
        """
        return Provider._exec(query)

    @staticmethod
    def _query_file_exec(file):
        """
        Метод вычитывает sql запрос из файла и исполняет его без аргументов
        :param file:
        :return:
        """
        with open(file, 'r') as f:
            query = f.read()
            return Provider._exec(query)

    @staticmethod
    def _query_file_args_exec(file, args):
        """
        Метод вычитывает sql запрос из файла и исполняет его с аргументами
        :param file:
        :param args:
        :return:
        """
        with open(file, 'r') as f:
            query = f.read().format(**args)
            return Provider._exec(query)

    @staticmethod
    def _query_exec_args(query, args):
        """
        Метод выполняет sql запрос с аргументами
        :param query:
        :param args:
        :return:
        """
        for k, v in args.items():
            alert_items = [';', '-', '*', 'drop', 'select', 'insert']
            if isinstance(v, str):
                # args[k] = f"'{args[k]}'"
                for alert in alert_items:
                    if alert in v:
                        args[k] = args[k].replace(alert, '')
        query = query.format(**args)
        if os.environ.get("IS_DEBUG"):
            print(query)
        return Provider._exec(query)

    @staticmethod
    def _exec(query):
        """
        Метод выполняет SQL запрос к базе
        :param query: str SQL запрос
        :return: dict результат выполнения запроса
        """
        connect, current_connect = Provider.connect()
        current_connect.autocommit = True
        result = None
        try:
            current_connect.execute(query)
            connect.commit()
        except psycopg2.Error as e:
            print(e.pgerror)
            print(e.diag.message_primary)
            print(psycopg2.errorcodes.lookup(e.pgcode))
        finally:
            try:
                result = current_connect.fetchall()
            except:
                pass
            finally:
                connect.close()
                return result
