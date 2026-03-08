class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("x- Invalid deposit amount -x")

    def withdraw(self, amount):
        if amount > self.balance:
            print("x- Insufficient balance -x")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"| Current balance: {self.balance} |")


def main():
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print()
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdraw amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            print("x--- SERVER CLOSED ---x")
            break
        else:
            print("---Invalid option---")


if __name__ == "__main__":
    main()
