from bank_module import CheckAccount, SavingAccount

def main_menu():
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

# Standard Python practice for production readiness
if __name__ == "__main__":
    main_menu()