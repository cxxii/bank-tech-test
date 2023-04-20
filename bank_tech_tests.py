import unittest
import pytest
from bank_tech import Bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    # Tests depositing function
    def test_deposit(self):
        self.bank.deposit(100, "01/01/2022")
        assert self.bank.balance == [100]
        assert self.bank.date == ["01/01/2022"]
        assert self.bank.amount == [100]

    # Test withdraw function
    def test_withdraw(self):
        self.bank.deposit(100, "01/01/2022")
        self.bank.withdraw(50, "02/01/2022")
        assert self.bank.balance == [100, 50]
        assert self.bank.date == ["01/01/2022", "02/01/2022"]
        assert self.bank.amount == [100, -50]

    # Tests attemping to a deposit negative amount
    def test_deposit_negative(self):
        with pytest.raises(Exception, match="CAN NOT DEPOSIT NEGATIVE MONEY"):
            self.bank.deposit(-1, "02/01/2022")

    # Tests attemping to a withdraw negative amount
    def test_withdraw_negative(self):
        with pytest.raises(Exception, match="CAN NOT WITHDRAW NEGATIVE MONEY"):
            self.bank.withdraw(-1, "02/01/2022")

    # Tests trying to go overdrawn
    def test_overdrawn(self):
        self.bank.deposit(100, "01/01/2022")
        with pytest.raises(Exception, match="INSUFFICIENT FUNDS"):
            self.bank.withdraw(101, "02/01/2022")
            assert self.bank.balance[-1] == 100

    # Tests trying to go withdraw 0
    def test_withdraw_0(self):
        self.bank.deposit(100, "01/01/2022")
        with pytest.raises(Exception, match="CAN NOT WITHDRAW 0"):
            self.bank.withdraw(0, "02/01/2022")
            assert self.bank.balance[-1] == 100

    # Tests trying to deposit 0
    def test_deposit_0(self):
        self.bank.deposit(100, "01/01/2022")
        with pytest.raises(Exception, match="CAN NOT DEPOSIT 0"):
            self.bank.deposit(0, "02/01/2022")
            assert self.bank.balance[-1] == 100

    # Tests the ability to enter only numerical values
    def test_alpha_deposit(self):
        self.bank.deposit(100, "01/01/2022")
        with pytest.raises(Exception, match="ONLY ENTER NUMERICAL VALUES"):
            self.bank.deposit("G", "01/01/2022")
            assert self.bank.balance == [100]

    # Tests the ability to enter only numerical values
    def test_alpha_withdraw(self):
        self.bank.deposit(100, "01/01/2022")
        with pytest.raises(Exception, match="ONLY ENTER NUMERICAL VALUES"):
            self.bank.withdraw("G", "01/01/2022")
            assert self.bank.balance == [100]


if __name__ == "__main__":
    unittest.main()
