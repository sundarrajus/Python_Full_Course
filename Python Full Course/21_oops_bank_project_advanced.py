# ============================================================
# CLEANED PYTHON FULL COURSE
# FILE: 21_oops_bank_project_advanced.py
# ============================================================

import random
import datetime

class BankAccount:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.transactions = []
        self.account_number = random.randint(100000, 999999)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(
                f"{datetime.datetime.now()}: Deposited ₹{amount}. Balance: ₹{self.balance}"
            )
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(
                f"{datetime.datetime.now()}: Withdrawn ₹{amount}. Balance: ₹{self.balance}"
            )
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"{self.name}, your current balance is: ₹{self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for t in self.transactions:
                print(t)

# Main program
accounts = {}

def authenticate():
    acc_no = int(input("Enter your account number: "))
    pin = input("Enter your PIN: ")
    account = accounts.get(acc_no)
    if account and account.pin == pin:
        return account
    else:
        print("Authentication failed. Invalid account number or PIN.")
        return None

def main():
    while True:
        print("\n=== Welcome to Python Bank ===")
        print("1. Create Account")
        print("2. Login to Existing Account")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            pin = input("Set a 4-digit PIN: ")
            account = BankAccount(name, pin)
            accounts[account.account_number] = account
            print(f"Account created successfully! Your account number is {account.account_number}")

        elif choice == "2":
            account = authenticate()
            if account:
                while True:
                    print(f"\nWelcome {account.name}!")
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Transaction History")
                    print("5. Logout")
                    sub_choice = input("Enter choice: ")

                    if sub_choice == "1":
                        account.check_balance()
                    elif sub_choice == "2":
                        amount = float(input("Enter amount to deposit: ₹"))
                        account.deposit(amount)
                    elif sub_choice == "3":
                        amount = float(input("Enter amount to withdraw: ₹"))
                        account.withdraw(amount)
                    elif sub_choice == "4":
                        account.show_transactions()
                    elif sub_choice == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice!")

        elif choice == "3":
            print("Thank you for using Python Bank. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-3.")

if __name__ == "__main__":
    main()
