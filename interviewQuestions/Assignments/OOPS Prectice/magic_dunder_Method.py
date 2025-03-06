"""
9. What are magic (dunder) methods in Python? Explain __init__, __str__, and __repr__ with examples.
__init__: Constructor
__str__: Human-readable string representation
__repr__: Developer-friendly string representation
Example:
"""

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}!"

    def __repr__(self):
        return f"Developer: ({self.name})"


obj = Person("Rolf Smith")
print(obj.__str__())
print(obj.__repr__())

print(str(obj))
print(repr(obj))