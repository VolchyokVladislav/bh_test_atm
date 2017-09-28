from abc import ABCMeta, abstractmethod

from bank.db import Account


class Session(metaclass=ABCMeta):
    _account = None
    _identity = None

    def __str__(self):
        self.__doc__.strip() if self.__doc__ else ''

    @abstractmethod
    def get_identity(self):
        pass

    @abstractmethod
    def get_credential(self):
        pass

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, acc):
        if not isinstance(acc, Account):
            raise TypeError
        self._account = acc


class BankCard(Session):
    def get_identity(self):
        if not self._identity:
            self._identity = input('Insert bank card: ')
        return self._identity

    def get_credential(self):
        return input('Enter PIN: ')
