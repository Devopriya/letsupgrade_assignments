# -*- coding: utf-8 -*-
"""Day5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fMVNE82M2DKnaAwhGSqI9P4kyusoAxv5

For this challenge, create a bank account class that has two attributes:

owner
    balance
    and two methods:
    deposit
    withdraw
    As an added requirement, withdrawals may not exceed the available balance.
    Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
  def __str__(self):
    return "Account owner: Pavan \nAccount balance: 100"
  def deposit(self, dep_amt):
    self.balance += dep_amt
    print("Deposit Accepted")
  def withdraw(self, wd_amt):
    try:
      if self.balance >= wd_amt:
        self.balance -= wd_amt
        print("Withdrwal accepted")
      else:
        print("Funds unavailable")
    except ValueError:
      print("value error for fund")

"""# 1. Instantiate the class"""

acc = Account('Pavan')

"""# 2. Print the object"""

print(acc)

"""# 3. Show the account owner attribute"""

print("The account owner's name is {}.".format(acc.owner))

"""# 4. Show the account balance attribute"""

print("The account owner's balance is ${}.".format(acc.balance))

"""# 5. Make a series of deposits and withdrawals"""

acc.deposit(500)

acc.balance

acc.deposit(100)

acc.balance

acc.withdraw(400)

acc.balance

acc.deposit(100)

acc.balance

"""# 6. Make a withdrawal that exceeds the available balance"""

acc.balance

acc.withdraw(350)