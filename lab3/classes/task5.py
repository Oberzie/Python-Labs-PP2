class Account:
 def __init__(self):
    self.owner = input()
    self.balance = int(input())
 
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

account.deposit(500)
account.deposit(-200)  # Invalid deposit

account.withdraw(300)
account.withdraw(1500)  # Overdraw attempt
account.withdraw(-100)  # Invalid withdrawal

print(account)