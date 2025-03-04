class BankAccount:
     def __init__(self, initial_balance=0):
         self.account_balance = initial_balance

         def deposit(self, amount):
              if amount > 0:
                   self.account_balance += amount
                   print(f"Deposted ${amount: 2f}")
              else:
                   print("Deposite amount must be posetive.")

         def withdraw(self, amount):
              if 0 < amount < self.account_balance:
                   self.account_balance -= amount
                   print(f"Withdrew ${amount: 2f}")
                   return True
              else:
                   print("Insufficient funds or invalid amount.")
                   return False
         def display_balance(self):
              print(f"Account balance: ${self.account_balance: 2f}")

