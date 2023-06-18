from .Clients import Clients
from .connection import get_db_connection


class DatabaseStorage:
    def __init__(self):
        self.__clients = Clients(get_db_connection())

    @property
    def Clients(self) -> Clients:
        return self.__clients


storage = DatabaseStorage()


__all__ = ['DatabaseStorage', 'storage']
