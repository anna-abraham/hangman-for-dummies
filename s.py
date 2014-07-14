class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def print_name(self):
    print(self.first_name, self.last_name)

dave = Person("Dave", "Smith")
dave.print_name()
print(dave.first_name)

class BankAccount:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def deposit(self, money):
    self.balance += money

  def withdraw(self, money):
    self.balance -= money

  def get_balance(self):
    return self.balance

john = BankAccount("John", 200)

print("John has %s dollars." % john.get_balance())
john.withdraw(100)
print("John now has %s dollars." % john.get_balance())