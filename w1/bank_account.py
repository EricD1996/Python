class BankAccount:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.balance * self.interest)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(9000, .05)
    
    def display_info(self):
        print(self.name)
        print(self.email)
        self.account.display_account_info()
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)

    def make_deposit(self, amount):
    	self.account.deposit(amount)


        
person1 = User('Eric', 'asdasd@gmail.com')
person1.make_deposit(500)
person1.make_withdraw(500)
person1.display_info()