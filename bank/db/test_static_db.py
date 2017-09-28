from bank.db import DB, Account

_db = [
    {'pk': '7777', 'name': 'Stive', 'money_balance': 101, 'pin': '0000'}
]


class TestDB(DB):
    _accounts = []

    def __init__(self, db):
        for acc in db:
            self._accounts.append(Account(**acc))

    def get_account(self, uid):
        try:
            return next(acc for acc in self._accounts if acc.pk == uid)
        except StopIteration:
            pass
        return None
