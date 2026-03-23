#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#parent class
class BankAccount:
    #magic function, encapsulation
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    #magic functionn
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

#child class - Inheritance
class CheckAccount(BankAccount):
    def __init__(self, owner, balance, fundfee):
        super().__init__(owner, balance)
        self.fundfee = fundfee
        
    #polymorphism
    def withdrawal(self, amount):
        if amount > self.balance:
            self.balance -= self.fundfee
            print(f'Overdraft! Fee charged: {self.fundfee}. New balance: {self.balance}')
        else:
            super().withdrawal(amount)

#child class - Inheritance
class SavingAccount(BankAccount):
    def __init__(self, owner, balance, interest):
        super().__init__(owner, balance)
        self.interest = interest
        
    def depositInterest(self):
        interest_amount = (self.balance * (self.interest / 100)) / 12
        self.deposit(interest_amount)
        print(f'Monthly interest is: {interest_amount:.2f}')
    
    #polymorphism
    def withdrawal(self, amount):
        print("Savings withdrawal")
        super().withdrawal(amount)


# Objects creating, Main Menu, functions calling, working OOP sutrucure  
account = None

while True:
    print("\n----- BANK MENU -----")
    print("1. Create Checking Account")
    print("2. Create Savings Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Add Interest (Savings)")
    print("6. Show Account Details")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter owner name: ")
        balance = int(input("Enter initial balance: "))
        fee = int(input("Enter overdraft fee: "))
        account = CheckAccount(name, balance, fee)
        print("Checking account created successfully.")

    elif choice == "2":
        name = input("Enter owner name: ")
        balance = int(input("Enter initial balance: "))
        interest = eval(input("Enter interest rate (%): "))
        account = SavingAccount(name, balance, interest)
        print("Savings account created successfully.")

    elif choice == "3":
        if account:
            amount = int(input("Enter deposit amount: "))
            account.deposit(amount)
        else:
            print("No account created yet.")

    elif choice == "4":
        if account:
            amount = int(input("Enter withdrawal amount: "))
            account.withdrawal(amount)
        else:
            print("No account created yet.")

    elif choice == "5":
        if isinstance(account, SavingAccount):
            account.depositInterest()
        else:
            print("Interest available only for Savings Account.")

    elif choice == "6":
        if account:
            print(account)
        else:
            print("No account created yet.")

    elif choice == "7":
        print("Thank you for using the Bank System.")
        break

    else:
        print("Invalid choice. Try again.")


# In[ ]:




