"""
Abstraction - hide unnecessary implimentation details and show only relavent features.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    #abstractmethod decorator: Ensures that any subclass must implement the abstract method.
    @abstractmethod
    def speak(self):
        pass

"""
Inheritance - Create new classes from existing ones to reuse code.(Same method name, different behaviors)
"""
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "meow!"

"""
Polymorphism - objects can take multiple forms, allowing for method ovrriding and overloading.
(We can treat different objects (Dog, Cat) as the same type (Animal) and call the same method speak().)
"""

animals = [Dog(), Cat()]      # → Creating a list of objects.
for animal in animals:        # → Iterating over the objects.
    print(animal.speak())     # → Calls speak() for each object:

"""
Encapsulation - Ristrict direct access to data by using private/protected variable.
"""
class Person:
    def __init__(self, name, age):
        self.name = name    # public variable (accessible anywhere)
        self.__age = age    # private variable (cannot be accessed directly outside the class) _a its a protected variable

    # In Python, variables prefixed with __ (double underscore) are "private" and should not be accessed directly.

    # Create gatter method for accessing private variable
    def get_age(self):
        return self.__age

    # get_age() is a gatter method used to retrieve the private variable __age.

