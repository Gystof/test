from .Clients import Regions


class LocalStorage:
    def __init__(self):
        self.__regions = Clients()

    @property
    def regions(self) -> Clients:
        return self.__regions


storage = LocalStorage()


__all__ = ['storage']
