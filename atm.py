from bank.actions import TransactionError
from bank.atm import ATM
from bank.bank import Bank, Services
from bank.session import BankCard
from bank.db.test_static_db import TestDB, _db

sl = Services(db=TestDB(_db))


class BHBank(Bank):
    """
    BH Bank
    """

    def get_account(self, session):
        pass


class BHBankCard(BankCard):
    """
    Starting
    """

    _db = sl.get('db')

    def get_identity(self):
        uid = super().get_identity()
        self.account = self._db.get_account(uid)


class BHATM(ATM):
    _card = None

    def _get_session(self):
        if not self._card:
            while True:
                try:
                    self.insert_card(BHBankCard)
                    self._card.get_identity()
                    break
                except:
                    self.remove_card()
                    pass

        print('\n'.join(['%s) %s' % (opname, self.get_operation(opname)) for opname in self.get_operations()]))

        opname = input('Chose operation> ')
        if self.has_operation(opname):
            try:
                self.get_operation(opname).start_operation(self)
            except TransactionError:
                print('Please remove your card')
                self.remove_card()

    def __init__(self, operations):
        super().__init__(operations)
        self.__bank = BHBank()

    def _get_bank(self):
        return self.__bank
