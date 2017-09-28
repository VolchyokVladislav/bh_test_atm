from abc import ABCMeta, abstractmethod
from bank.atm import ATM


class Action(metaclass=ABCMeta):
    @abstractmethod
    def handle_action(self, atm):
        pass

    def __str__(self):
        return self.__doc__.strip() if self.__doc__ else self.__class__.__name__


class BaseTransaction(metaclass=ABCMeta):
    _actions = None
    _atm = None

    def __init__(self, atm):
        if not isinstance(atm, ATM):
            raise TransactionError('%s should be ATM')
        self._atm = atm
        self._actions = []

    def add_action(self, action):
        self._actions.append(action)

    @property
    def atm(self):
        return self._atm

    @abstractmethod
    def _start(self):
        pass

    def __enter__(self):
        self._start()
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if not self._actions:
            raise StopIteration
        a = self._actions.pop(0)
        if not isinstance(a, Action):
            raise TransactionError('%s should be Action' % a)
        res = a.handle_action(self.atm)
        return res, a


    @abstractmethod
    def _commit(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._commit()


class Transaction(BaseTransaction):
    def _start(self):
        pass

    def _commit(self):
        pass


class TransactionException(Exception):
    pass


class TransactionError(TransactionException):
    pass


class BreakTransaction(TransactionException):
    pass


class FinishTransaction(TransactionException):
    pass
