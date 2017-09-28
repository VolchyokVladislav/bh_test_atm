from abc import ABCMeta, abstractmethod


class Operation(metaclass=ABCMeta):
    """
    Abstract operation
    """

    def __str__(self):
        return self.__doc__.strip()

    @abstractmethod
    def start_operation(self, atm):
        pass
