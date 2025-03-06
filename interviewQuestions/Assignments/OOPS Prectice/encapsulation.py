"""
Encapsulation :- Binding data into a single unit is known as encapsulation.
                 Attributs and methods are bonded together into a class. A
                 class is an encapsulation. several classes together create packages.
                 A package is an encapsulation.

                 Ex:-
                 One man is a single encapsulation, all men and women together belong to class call 'Human', Human is an encapsulation.

                 class ------->[method | attribute(variable)]

                 The data hiding user not have no idea about the inner implementation of the class and even user.

"""

# What is encapsulation in Python? How do you achieve it using private and protected attributes?

'''
Public (name) – Accessible anywhere.
Protected (_name) – Accessible in child classes.
Private (__name) – Only accessible within the class
'''
class BankAccounts:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # public
        self._balance = balance     # protected
        self.__pin = 1234       #  private


    def get_pin(self):
        return self.__pin


acc =  BankAccounts(100023223, 5000)
print(acc.account_number)
print(acc._balance)
print(acc.get_pin())
print("==================================================")
# 1. A private variable (__a) is name-mangled in Python to prevent accidental access outside the class.
# 2. It cannot be accessed directly from outside the class but can still be accessed using name mangling (_ClassName__variable).
class Base:
    def __init__(self):
        self.__a = 2

class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        # Trying to access private variable from parent class
        # print("Accessing Private member of Base class: ", self.__a)  # ❌ This will cause an AttributeError

        # Accessing private variable using name mangling (Not recommended)
        print("Accessing Private member using name mangling: ", self._Base__a)
# Creating objects
obj1 = Derived()
obj2 = Base()

# Trying to access private variable directly
# print("Accessing Private member of obj1: ", obj1.__a)  # ❌ AttributeError

# Accessing private variable using name mangling (Bypassing encapsulation)
print("Accessing Private member of obj2 using name mangling: ", obj2._Base__a)  # ✅ Works but should be avoided


print("==================================================")
#  Private Methods (__method)
class Example:
    def __init__(self):
        self.__private_method()

    def __private_method(self):
        print("This is a private method")

ex = Example()
ex._Example__private_method()
print("==================================================")

# Protected Methods (_method)
class Parent:
    def _protected_method(self):
        print("This is a protected method")

    def Hello(self):
        print("Hiii")

class Child(Parent):
    def access_protected(self):
        self._protected_method()
        self.Hello()


obj = Child()
obj.access_protected()
obj._protected_method()
print("==================================================")

# Encapsulation in a Real-World Project: Banking System Example 🚀
class BankAccount:
    def __init__(self, balance):
        self.balance = balance      # Public attribute (not encapsulated

account = BankAccount(1000)
print(account.balance)  # 1000 (Accessible directly)

account.balance = -500  # ❌ Incorrect! Negative balance shouldn't be allowed
print(account.balance)  # -500 (This should not be possible)


print("========================Piggy Bank==========================")

'''
Example: Piggy Bank (Gullak) Using Encapsulation
In this example, we will create a Piggy Bank that stores money securely. No one can directly change the money inside; they have to use the right method to add or withdraw money.
'''

class PiggyBank:
    def __init__(self):
        #The __money variable is private, meaning no one can directly access it from outside the class.
        self.__money = 0


    def deposit(self, amount):
        # add money
        if amount > 0:
            self.__money += amount
            print(f"Rs.{amount} added to the piggy bank.")

        else:
            print("Invalid amount! Please add a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__money:
            self.__money -= amount
            print(f"Rs.{amount} withdraw successfull")

    def check_balance(self):
        print(f"Current balance: Rs {self.__money}")



my_piggy = PiggyBank()
my_piggy.deposit(1000)
my_piggy.check_balance()
my_piggy.withdraw(300)
my_piggy.check_balance()   

# print(my_piggy.__money)        #Trying to access __money directly will give an error ❌ → Not allowed!
'''
Encapsulated Methods (deposit, withdraw, check_balance)

You can only modify money using these safe methods.
Wrong methods (like directly changing money) are blocked.
Trying to access __money directly will give an error

print(my_piggy.__money) ❌ → Not allowed!



💡 Real-Life Connection
This is just like a piggy bank (गुल्लक):
✅ You can add money (deposit method)
✅ You can take out money (withdraw method)
❌ But you CANNOT open and change money directly without breaking the piggy bank!

Encapsulation keeps your data safe just like a piggy bank keeps your money safe. 😊
'''

print("========================School Student==========================")

#Example 2:
'''
1️⃣ Example: School Report Card (Hiding Student Marks)
In a school, a student's marks should be private, and only teachers should be able to update them. Students can only view their marks.
'''

class School:
    def __init__(self, name):
        self.name = name
        self.__marks = 0        #  Private variable (Encapsulation)

    def setmarks(self, marks):       
        """Only teachers can update marks""" 
        if 0 < marks <= 100:
            self.__marks += marks
        else:
            print("Invalid marks! Must be between 0 and 100.")


    def get_marks(self):
        """Students can only view their marks"""
        print(f"{self.name} your marks is {self.__marks}")



# Creating a student object
stu1 = School("Ved")
stu1.setmarks(98)
stu1.get_marks()
# Trying to access marks directly (This will not work)
# print(student1.__marks)  # ❌ Error: AttributeError


print("========================Bank Account==========================")

# Example 3
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance         # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs{amount} deposit successfully in Your A/c")
        else:
            print("Invalid deposit amount.")


    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully!")

        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current Balance: Rs {self.__balance}")


user = BankAccount("0951000100342834", 3000)
user.deposit(200)
user.check_balance()
user.withdraw(3000)
user.check_balance()

# Trying to access balance directly (This will not work)
# print(my_account.__balance)  # ❌ Error: AttributeErro





