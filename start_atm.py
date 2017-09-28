if __name__ == '__main__':
    from atm import BHATM
    from bank.operations.check_balance import CheckBalance
    from bank.operations.return_card import ReturnCard

    atm = BHATM({
        '1': CheckBalance,
        '2': ReturnCard
    })
    atm.run_atm()
