import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('Ethan')
        self.a1.deposit(100)
        self.a2 = Account('Aaron')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'Ethan'
        assert self.a1.get_balance() == 100
        assert self.a1.get_name() != 'Aaron'
        assert self.a1.get_balance() != 365
        assert self.a2.get_name() == 'Aaron'
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(100) is True
        assert self.a1.get_balance() == 200
        assert self.a1.get_balance() != 100
        assert self.a2.get_balance() == 0
        assert self.a2.get_balance() != 100

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 200
        assert self.a1.get_balance() != 0

        assert self.a1.deposit(-100) is False
        assert self.a1.get_balance() == 200
        assert self.a1.get_balance() != 100
        assert self.a1.get_balance() != -100

        with pytest.raises(TypeError):
            self.a1.deposit('one million dollars')
        assert self.a1.get_balance() == 200

    def test_withdraw(self):
        assert self.a1.withdraw(100) is True
        assert self.a1.get_balance() == 0
        assert self.a1.get_balance() != 100
        assert self.a2.get_balance() == 0
        assert self.a2.get_balance() != 100

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0
        assert self.a1.get_balance() != 100

        assert self.a1.withdraw(-100) is False
        assert self.a1.get_balance() == 0
        assert self.a1.get_balance() != 100
        assert self.a1.get_balance() != -100

        with pytest.raises(TypeError):
            self.a1.withdraw('a bazillion dollars')
        assert self.a1.get_balance() == 0