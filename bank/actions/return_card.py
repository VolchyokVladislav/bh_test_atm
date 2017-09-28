from bank.actions import Action, TransactionError


class ReturnCard(Action):
    """
    Return card
    """

    def handle_action(self, atm):
        raise TransactionError
