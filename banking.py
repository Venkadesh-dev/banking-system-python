class Account:
    def __init__(self, acc_id, acc_name, acc_balance):
        self.acc_id = acc_id
        self.acc_name = acc_name
        self.acc_balance = acc_balance
        self.Transactions = []

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Amount {amount} should be greater than zero")

        elif amount <= self.acc_balance:
            self.acc_balance -= amount
            print(f"After withdrawal, balance: {self.acc_balance}")

            transaction = Transactions(
                Transactions.transaction_counter,
                "WITHDRAWAL",
                amount,
                "SUCCESSFUL"
            )

            self.Transactions.append(transaction)

        else:
            print("Insufficient funds!")

    def deposit(self, amount):
        if amount <= 0:
            print(f"Amount {amount} should be greater than zero")

        else:
            self.acc_balance += amount
            print(f"After deposit, balance: {self.acc_balance}")

    def display_transactions(self):
        for transaction in self.Transactions:
            transaction.Display_transaction()

class Transactions:
    transaction_counter = 0
    def __init__(self,trans_id, trans_type, trans_amount, trans_status):
        Transactions.transaction_counter += 1
        self.trans_id = Transactions.transaction_counter
        self.trans_type = trans_type
        self.trans_amount = trans_amount
        self.trans_status = trans_status

    def Display_transaction(self):
        print(
            f"Transaction ID: {self.trans_id}, "
            f"Type: {self.trans_type}, "
            f"Amount: {self.trans_amount}, "
            f"Transaction Status: {self.trans_status}"
        )


# Test the class

account1 = Account(101, "venkadesh", 100000)

account1.withdraw(7000)
account1.withdraw(9000)

account2 = Account(102, "srilekha", 200000)

account2.deposit(50000)


print("\nAccount Details:")

print(
    f"Account Number: {account1.acc_id} "
    f"Account Holder: {account1.acc_name} "
    f"Balance: {account1.acc_balance}"
)

print(
    f"Account Number: {account2.acc_id} "
    f"Account Holder: {account2.acc_name} "
    f"Balance: {account2.acc_balance}"
)


print("\nAccount 1 Transactions:")

account1.display_transactions()