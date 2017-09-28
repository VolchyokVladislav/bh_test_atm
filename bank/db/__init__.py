from abc import ABCMeta, abstractmethod

from copy import deepcopy


class DB(metaclass=ABCMeta):
    @abstractmethod
    def get_account(self, uid):
        pass


class Field(metaclass=ABCMeta):
    _value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        self._value = None

    def __eq__(self, other):
        return self.value == other

    def __str__(self):
        return str(self.value)


class Str(Field):
    def __init__(self, max_length=255):
        if max_length > 255 or max_length < 1:
            raise ValueError
        self.max_length = max_length

    @Field.value.setter
    def value(self, new_value):
        new_value = str(new_value)
        if len(new_value) > self.max_length:
            new_value = new_value[:self.max_length]
        self._value = new_value


class Number(Field):
    @Field.value.setter
    def value(self, new_value):
        new_value = float(new_value)
        self._value = new_value

    def __eq__(self, other):
        self._value = float(other)


class FieldPrototype:
    _objects = []

    def register(self, object):
        if not isinstance(object, Field):
            raise TypeError
        if not any (object is o for o in self._objects):
            self._objects.append(object)

    def clone(self, object, **values):
        if any(object is o for o in self._objects):
            c = deepcopy(object)
        else:
            raise ValueError
        for name, value in values.items():
            setattr(c, name, value)
        return c


prototypes = FieldPrototype()


class Model(metaclass=ABCMeta):
    def __new__(cls, *args, **kwargs):
        for d in dir(cls):
            if isinstance(getattr(cls, d), Field):
                prototypes.register(getattr(cls, d))
        return super().__new__(cls)

    def __init__(self, **data):
        for field, value in data.items():
            if hasattr(self, field) and isinstance(getattr(self, field), Field):
                setattr(self, field, prototypes.clone(getattr(self.__class__, field), value=value))
                del value


class Account(Model):
    pk = Str()
    name = Str()
    money_balance = Number()
    pin = Str(max_length=4)

    def get_money_amount(self):
        return self.money_balance

    def block_money(self, amount):
        pass

    def accrue_money(self, amount):
        pass

    def write_off_money(self, amount):
        pass


class BlockedMoney(Model):
    pk = Field()
    account = Field()
    date = Field()
    money_amount = Field()
