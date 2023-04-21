class Account:
    def __init__(self, name: str) -> None:
        """
        Function creates an account and names it.
        :param name: Name of account created.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function adds deposited amount to account balance.
        :param amount: Amount of money deposited.
        :return: Boolean value for whether transaction completed or not.
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function subtracts withdrawn amount from account balance.
        :param amount: Amount of money withdrawn.
        :return: Boolean value for whether transaction completed or not.
        """
        if self.__account_balance >= amount > 0:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function gets account balance.
        :return: Account balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function gets account name.
        :return: Account name.
        """
        return self.__account_name
