class BankAccount:
    def __init__(self, account_num, amount, bank_name):
        self.__account_number = account_num  # Private attribute
        self.__amount = amount  # Private attribute
        self.__bank_name = bank_name  # Private attribute

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.__amount += amount

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if self.__amount < amount:
            print("Insufficient balance")
            return
        self.__amount -= amount

    # Getter method to access the balance
    def get_balance(self):
        return self.__amount

    # Getter method to access the account number
    def get_account_number(self):
        return self.__account_number

    # Getter method to access the bank name
    def get_bank_name(self):
        return self.__bank_name
