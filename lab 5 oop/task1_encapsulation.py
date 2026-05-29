from random import randint
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          
        self.__balance = balance    

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance


account = BankAccount("Bohdan", 1000)

print(f"Початковий баланс: {account.get_balance()}")

for i in range(5):
    deposit_amount = randint(100, 500)
    withdraw_amount = randint(50, 600)

    account.deposit(deposit_amount)
    print(f"Хід {i + 1}: поповнення +{deposit_amount}")

    result = account.withdraw(withdraw_amount)
    if isinstance(result, int):
        print(f"Хід {i + 1}: зняття -{withdraw_amount}")
    else:
        print(f"Хід {i + 1}: спроба зняти {withdraw_amount} — {result}")

    print(f"Баланс після ходу {i + 1}: {account.get_balance()}")

print(f"\nКінцевий баланс: {account.get_balance()}")
