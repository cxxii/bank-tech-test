class Bank:
    def __init__(self):
        self.balance = []
        self.date = []
        self.amount = []

    def deposit(self, amount, date):
        """
        Deposits given amount into bank

        Args:
            amount (int, float): amount to deposit in the bank.
            date (string): Date on which transaction occurs.

        Raises:
            TypeError: If amount is not numerical
            Exception: If amount is <= 0
        """

        # Error handling
        match amount:
            case n if not isinstance(n, (float, int)):
                raise TypeError("ONLY ENTER NUMERICAL VALUES")
            case n if n == 0:
                raise Exception("CAN NOT DEPOSIT 0")
            case n if n < 0:
                raise Exception("CAN NOT DEPOSIT NEGATIVE MONEY")

        if len(self.balance) > 0:
            self.balance.append(self.balance[-1] + amount)
        else:
            self.balance.append(amount)

        # Deposit function
        self.date.append(date)
        self.amount.append(amount)

    def withdraw(self, amount, date):
        """
        Function withdraws given amount of money from the bank account.

        Args:
            amount (float, int): amount to withdraw from bank
            date (string): Date on which transaction occurs

        Raises:
            TypeError: If amount is not numerical
            Exception: If amount is <= 0 and if amount is  > bank balance
        """

        # Error Handling
        match amount:
            case n if not isinstance(n, (float, int)):
                raise TypeError("ONLY ENTER NUMERICAL VALUES")
            case n if n == 0:
                raise Exception("CAN NOT WITHDRAW 0")
            case n if n < 0:
                raise Exception("CAN NOT WITHDRAW NEGATIVE MONEY")
            case n if n > self.balance[-1]:
                raise Exception("INSUFFICIENT FUNDS")

        # Widthdrawl function
        if len(self.balance) == 0:
            raise Exception("INSUFFICIENT FUNDS")
        else:
            self.date.append(date)
            self.amount.append(-abs(amount))

        if self.balance:
            self.balance.append(float(self.balance[-1] - amount))
        else:
            self.balance.append(float(amount))

    def statement(self):
        """
        Prints the account statement in a formatted table

        Returns:
            _type_: _description_
        """

        horizontal_line = "." * 69

        print(horizontal_line)
        print(
            "||",
            "DATE".center(12),
            "||",
            "CREDIT".center(13),
            "||",
            "DEBIT".center(13),
            "||",
            "BALANCE".center(13),
            "||",
        )
        print(horizontal_line)

        for date, amount, balance in zip(
            reversed(self.date), reversed(self.amount), reversed(self.balance)
        ):
            if amount > 0:
                credit = "{:.2f}".format(amount).rjust(13)
                debit = " ".rjust(13)
            else:
                credit = " ".rjust(13)
                debit = "{:.2f}".format(abs(amount)).rjust(13)

            print(
                "||",
                date.rjust(12),
                "||",
                credit,
                "||",
                debit,
                "||",
                "{:.2f}".format(balance).rjust(13),
                "||",
            )

        print(horizontal_line)

        return ""