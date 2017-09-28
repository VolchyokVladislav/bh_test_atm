from bank.actions import Action


class GetBalance(Action):
    def handle_action(self, atm):
        return atm.card.account.get_money_amount()
