class Player:
    """
    This class represents the player.
    """

    def __init__(self, nickname, money=1000):
        self._nickname = nickname
        self._money = money

    def get_nickname(self) -> str:
        """
        It returns the player's nickname.
        """

        return self._nickname

    def get_money(self) -> int:
        """
        It returns the player's money.
        """

        return self._money

    def get_money_with_symbol(self) -> str:
        """
        It returns the player's money with the virtual currency symbol.
        """

        return "simu$ " + str(self._money)

    def receive_money(self, money: int) -> None:
        """
        It gives a certain amount of money to the player.

        Arguments:
            money: a positive integer amount to give to the player

        In case of problems, the money will not be updated.
        """
    
        if isinstance(money, int):
            if money > 0:
                self._money += money

    def lose_money(self, money: int) -> None:
        """
        It takes away a certain amount of money from the player.

        Arguments:
            money: a positive integer amount to take away from the player

        In case of problems, the money will not be updated.
        """

        if isinstance(money, int):
            if money > 0:
                self._money -= money

    def can_bet(self, bet: int) -> bool:
        """
        It returns True if the user can bet the informed amount (the 'bet' argument) and False otherwise.

        Arguments:
            bet: a positive integer amount to bet
        """

        if isinstance(bet, int):
            return bet <= self._money and bet > 0
        
        return False
