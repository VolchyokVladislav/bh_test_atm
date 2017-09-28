from bank.actions import Transaction, FinishTransaction, TransactionError, BreakTransaction
from bank.actions.authenticate import Authenticate
from bank.actions.choice import Choice
from bank.actions.get_balance import GetBalance
from bank.actions.return_card import ReturnCard
from bank.actions.select_actions import SelectActions
from bank.operations import Operation


class CheckBalance(Operation):
    """
    Check account balance
    """

    def start_operation(self, atm):
        transaction = Transaction(atm)
        transaction.add_action(Authenticate())
        transaction.add_action(GetBalance())
        c1 = Choice()
        c1.add_choice('1', ReturnCard())
        c1.add_choice('2', SelectActions())
        transaction.add_action(c1)
        with transaction as tr:
            try:
                for result, action in tr:
                    if isinstance(action, GetBalance):
                        print('balance is: %s' % str(result))
            except FinishTransaction:
                return
            except BreakTransaction:
                raise TransactionError
