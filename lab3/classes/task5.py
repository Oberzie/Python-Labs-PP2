class Account:
 def __init__(self):
    self.owner = input("Enter Account name: ")
    self.balance = int(input("Initial balance: "))
 
 def deposit(self, amount):
      if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} completed. New balance: {self.balance}")
      else:
            print("Deposit amount must be greater than 0.")
            
 def withdraw(self, amount):  
     if amount > self.balance:
            print(f"Withdrawal of {amount} declined. Insufficient funds. Available balance: {self.balance}")
     elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
     else:
            self.balance -= amount
            print(f"Withdrawal of {amount} completed. New balance: {self.balance}")

 
 def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

       


account = Account()
print(account)
dep = int(input("What sum do you want to deposit? "))
account.deposit(dep)
wit = int(input("How much do you want to withdraw? "))
account.withdraw(wit)


print(account)