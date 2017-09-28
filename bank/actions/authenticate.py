from bank.actions import Action, TransactionError


class Authenticate(Action):
    def handle_action(self, atm):
        for i in range(0, 3):
            c = atm.card.get_credential()
            if atm.card.account.pin == c:
                return
        raise TransactionError
