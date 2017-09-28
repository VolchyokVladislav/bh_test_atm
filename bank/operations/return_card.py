from bank.actions import Transaction, FinishTransaction, TransactionError, BreakTransaction
from bank.actions.authenticate import Authenticate
from bank.actions.choice import Choice
from bank.actions.get_balance import GetBalance
from bank.actions.return_card import ReturnCard
from bank.actions.select_actions import SelectActions
from bank.operations import Operation


class ReturnCard(Operation):
    """
    Return card
    """

    def start_operation(self, atm):
        transaction = Transaction(atm)
        transaction.add_action(ReturnCard())
        with transaction as tr:
            next(tr)
