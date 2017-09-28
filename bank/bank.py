from abc import ABCMeta, abstractmethod


class Bank(metaclass=ABCMeta):
    """
    Abstract Bank
    """

    @abstractmethod
    def get_account(self, session):
        pass

    def __str__(self):
        return self.__doc__.strip() if self.__doc__ else ''


class Services:
    _services = None

    def __init__(self, **services):
        self._services = dict(services)

    def has(self, service):
        return service in self._services

    def get(self, service):
        return self._services.get(service)
