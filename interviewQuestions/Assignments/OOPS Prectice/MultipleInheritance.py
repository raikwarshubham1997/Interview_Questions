"""
Multiple Inheritance: It involve more than one parant class.

Python resolves conflicts using Method Resolution Order (MRO) with the C3 Linearization Algorithm.
"""

class Parent1:
    def show(self):
        return "This is first parent class!"

class Parent2:
    def show(self):
        return "This is second parent class!"

class Child(Parent1, Parent2):
    pass
        


ch = Child()

print(ch.show())