from abc import ABCMeta, abstractmethod


class OperationNotFound(KeyError):
    pass


class ATMException(Exception):
    pass


class ATM(metaclass=ABCMeta):
    _operations = None
    _card = None

    def __init__(self, operations):
        self._operations = {}
        for i, o in operations.items():
            self._operations[str(i)] = o

    def has_operation(self, operation):
        return str(operation) in self._operations

    def get_operation(self, operation):
        if self.has_operation(operation):
            return self._operations[operation]()
        raise OperationNotFound('%s operation not found' % operation.__name__)

    @property
    def card(self):
        return self._card

    @abstractmethod
    def _get_session(self):
        pass

    @abstractmethod
    def _get_bank(self):
        pass

    def run_atm(self):
        print(self._get_bank())
        while True:
            self._get_session()

    def get_operations(self):
        return self._operations.keys()

    def insert_card(self, card):
        if self._card:
            raise ATMException('Card in ATM')
        self._card = card()

    def remove_card(self):
        if self._card:
            self._card = None
