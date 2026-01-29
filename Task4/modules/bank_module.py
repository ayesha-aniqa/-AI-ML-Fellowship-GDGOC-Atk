# Parent class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f'Account Owner: {self.owner}\tBalance: {self.balance:.2f}'
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited amount: {amount}. New balance is {self.balance}')
        
    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient Amount.")
        else:
            self.balance -= amount
            print(f'Withdrawn amount: {amount}\nRemaining balance: {self.balance}')

# Child class - Inheritance
class CheckAccount(BankAccount):
    def __init__(self, owner, balance, fundfee):
        super().__init__(owner, balance)
        self.fundfee = fundfee
        
    def withdrawal(self, amount):
        if amount > self.balance:
            self.balance -= self.fundfee
            print(f'Overdraft! Fee charged: {self.fundfee}. New balance: {self.balance}')
        else:
            super().withdrawal(amount)

# Child class - Inheritance
class SavingAccount(BankAccount):
    def __init__(self, owner, balance, interest):
        super().__init__(owner, balance)
        self.interest = interest
        
    def depositInterest(self):
        # Formula: $Interest = \frac{Balance \times (\frac{InterestRate}{100})}{12}$
        interest_amount = (self.balance * (self.interest / 100)) / 12
        self.deposit(interest_amount)
        print(f'Monthly interest is: {interest_amount:.2f}')
    
    def withdrawal(self, amount):
        print("Savings withdrawal")
        super().withdrawal(amount)