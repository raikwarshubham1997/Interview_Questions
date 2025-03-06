"""
7. What is the difference between staticmethod and classmethod in Python?
@staticmethod – No self, used for utility functions.
@classmethod – Uses cls and modifies class-level attributes
"""

# example

class Demo:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def greet():
        return "Hello! World."

Demo.increment()
print(Demo.count)
print(Demo.greet())
