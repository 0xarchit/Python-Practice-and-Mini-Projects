'''
8. Menu-Driven Bank System
Design a menu-driven Banking System. The system should support the following options:
• Create Account (name, initial deposit)
• Deposit money
• Withdraw money
• Display Account Details
• Exit
Write a Python program using classes to implement this. Use methods to handle each of the
operations above.
Scenario: Each account is an object of the class BankAccount.
'''

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance is ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance is ${self.balance}")

    def display_details(self):
        print(f"Account Name: {self.name}")
        print(f"Account Balance: ${self.balance}")


def main():
    accounts = {}

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Display Account Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder's name: ")
            ini_deposit = float(input("Enter initial deposit amount: "))
            accounts[name] = BankAccount(name, ini_deposit)
            print(f"Account created for {name} with initial deposit of ${ini_deposit}")

        elif choice == "2":
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            name = input("Enter account holder's name: ")
            if name in accounts:
                accounts[name].display_details()
            else:
                print("Account not found.")

        elif choice == "5":
            print("Exiting the banking system.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()