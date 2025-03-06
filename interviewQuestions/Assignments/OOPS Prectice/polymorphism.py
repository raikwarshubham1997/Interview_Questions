"""
same function use each class but child class override parent class fuction.
POLYMORPHISM - polymorphism is taken from greek word poly (many) and morphism(forms). 
It means that the same function name can be used for diffrent types. this makes programming more easier.
    
    A child class inherit all the methods from the parent class. However, in Some situations, the method
    inherited from the parent class doesn't quite fit into the child class. In such cases, you will have to re-implement method in the child class.

''Polymorphism is just a concept this means ability to take various form (It can use for method overriding).''
    
"""




# Example 1

class Dog:
    def sound(self):
        return "Dog Barks: Woof Woof!"

class Cat:
    def sound(self):
        return "Car meows: Meow Meow!"

class Cow:
    def sound(self):
        return "Cow moos: Moo Moo!"


# Polymorphism in action
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.sound())

print("===================================================")
# Example: as a Me different role in diffrent relation
class Mammy:
    def shubham(self):
        return "Shubham is my Son!!"

class Sister:
    def shubham(self):
        return "Shubham is my Brothe!!!"


class Ved:
    def shubham(self):
        return "Shubham is my Mama!!!!"



humans = [Mammy(), Sister(), Ved()]
for human in humans:
    print(human.shubham())

print("===================================================")

# Polymorphism in Functions

def add(a, b, c=0):  # Default value देकर Overloading जैसा किया
    return a + b + c

print(add(2, 3))       # 2 arguments => Output: 5
print(add(2, 3, 4))    # 3 arguments => Output: 9

print("===================================================")

'''
# can python use overriding?
Method Overriding is a part of Polymorphism, where the child class (Subclass) can modify the method of its parent class (Superclass) according to its needs.
'''
# Example: Method Overriding

class Parent:
    def show(self):
        return "Parent class : I am a parent class!"

class Child(Parent):
    def show(self):            # Overriding Parent's method
        return "Child class: I am a Child class!"


parent_obj = Parent()
child_obj = Child()

print(parent_obj.show())     # Output: मैं पेरेंट क्लास से हूँ!
print(child_obj.show())      # Output: मैं चाइल्ड क्लास से हूँ!

print("===================================================")

# Sometime we need to execute parent class using super() inside the child or subclass 

class Parentsame:
    def show(self):
        return "Parent class : I am a parent class!"

class Childsame(Parentsame):
    def show(self):            # Overriding Parent's method
        # Super() का उपयोग करके पेरेंट की Method भी चलाना
        parent_message = super().show()
        return parent_message + "\nChild class: I am a Child class!"

childsame = Childsame()
print(childsame.show())

# super().show() से हमने पेरेंट क्लास की method को भी call किया।
'''
--> Python में Overriding का उपयोग कहाँ किया जाता है?

✔ OOP (Object-Oriented Programming) में Code को Modify करने के लिए।
✔ Parent Class में General Method रखकर Child Class में उसे Custom बनाना।
✔ Frameworks जैसे Django, Flask में अपने हिसाब से Functions बदलने के लिए।
'''

print("===================================================")

# एक Example बनाओ जिसमें एक Vehicle क्लास हो और Car और Bike क्लास उसे Override करें!
class Vehicle:
    def shitting(self):
        return "Sit mamber!"

class Car(Vehicle):
    def shitting(self):
        vehcl = super().shitting()
        return vehcl + "\nThere is Sitthing 4 to 5 member in a car!"

class Bick(Vehicle):
    def shitting(self):
        vehcl = super().shitting()
        return vehcl + "\nThere is sitting 1 to 2 member in a bick!"


poly = [Car(), Bick()]
for po in poly:
    print(po.shitting())


# Example play game polymorphism (method overriding)
class Game:
    def Play(self):
        return "Game name and Equipment!"

class Cricket(Game):
    def Play(self):
        gm = super().Play()      # call parent class method
        return gm + "\nplay Cricket Match need bat and ball!"

class BasketBall(Game):
    def Play(self):
        gm = super().Play()      # call parent class method
        return gm + "\nPlay Basketball need a ground, Basket and Ball!!!"


class Hockey(Game):
    def Play(self):
        gm = super().Play()      # call parent class method
        return "Play Hockey need a Ground, hockey stick, and Ball!!"

# create object
ob1 = Cricket()
print(ob1.Play())

# polymorphism in action
games = [Cricket(), BasketBall(), Hockey()]
for game in games:
    print(game.Play())


"""
Python Overloading को Directly Support नहीं करता!
Python में Method Overloading (Function Overloading) directly नहीं होती, लेकिन इसे *डिफ़ॉल्ट आर्गुमेंट्स (Default Arguments) या args & kwargs से achieve किया जा सकता है।

Method Overloading का Example (Default Arguments से)
"""

class Calculator:
    def add(self, a, b, c=0):  # Default value देकर Overloading जैसा किया
        return a + b + c

# Object बनाना
calc = Calculator()

# 2 Arguments (Overloading जैसा Behavior)
print(calc.add(2, 3))     # Output: 5

# 3 Arguments (Overloading जैसा Behavior)
print(calc.add(2, 3, 4))  # Output: 9




def add(a, b, c=0):
    return a + b + c

print(add(2, 3))       # Uses two parameters, output: 5
print(add(2, 3, 4))    # Uses three parameters, output: 9

# Using *args to allow any number of arguments
def add_all(*args):
    return sum(args)

print(add_all(1, 2))             # Output: 3
print(add_all(1, 2, 3, 4, 5))     # Output: 15