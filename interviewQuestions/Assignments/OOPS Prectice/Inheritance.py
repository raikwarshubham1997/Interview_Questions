"""
Inheritance प्रोग्रामिंग में कैसे काम करता है?
इसी तरह, Python में Inheritance का मतलब होता है कि एक Class (Parent) अपनी properties और methods दूसरी Class (Child) को दे सकती है।

🔹 Parent Class → राजा अर्जुन (जिसके पास तलवार, घोड़ा, और बुद्धिमानी है)
🔹 Child Class → राजकुमार विक्रम (जिसे अपने पापा की चीज़ें मिलीं)

Python में इसे ऐसे लिखा जाता है:
"""
# Parent Class (राजा अर्जुन)
class King:
    def __init__(self):
        # attributes
        self.sword = "जादुई तलवार"
        self.horse = "तेज़ घोड़ा"

    # methods
    def wisdom(self):
        return "राजा की बुद्धिमानी"

# child class (राजकुमार विक्रम)
class Prince(King):
    def show_legacy(self):
        return f"मुझे अपने पिता से {self.sword} और {self.horse} मिली, और मैं भी {self.wisdom()} सीख रहा हूँ!"

vikram = Prince()
print(vikram.show_legacy())
print(vikram.sword)
print(vikram.horse)


"""
Example: Parent-Child Relationship in Python (Using Inheritance)
Imagine we have a Parent Class Animal and a Child Class Dog.
The Dog class will inherit properties and methods from the Animal class
"""
class Animal:
    # constructor
    def __init__(self, name):
        self.name = name   # Common property for all animals

    def make_sound(self):
        return "Some generic animal sound"


# Child Class (Inheriting from Animal)

class Dog(Animal):
    def make_sound(self):           # Overriding the parent class method
        parnt = super().make_sound()
        return parnt + "\nBark!, Bark!"

    def fetch_ball(self):
        return f"{self.name} is fetching the ball!"

    def Eating(self):
        return f"{self.name}, is Eating Pedigiry!"



dog = Dog("Buddy")
print(dog.make_sound())
print(dog.fetch_ball())
print(dog.Eating())

'''
Explanation:
The Animal class has a common property (name) and a method (make_sound).
The Dog class inherits from Animal, so it gets the name property.
The Dog class overrides make_sound() to provide its own implementation.
The Dog class also has an extra method fetch_ball(), which is not present in Animal.
When we create an object of Dog, it can use both inherited and new methods.

Why is Inheritance Useful?
✅ Code Reusability – We don’t have to write the name property again in Dog.
✅ Extensibility – We can add new behavior to the child class without modifying the parent.
✅ Organized Code – Helps in structuring code efficiently.


'''
print("==========================================")

'''
Example: Vehicle Inheritance
Imagine a Parent Class Vehicle and Child Classes Car and Truck.
Each child class inherits properties from Vehicle and has its own additional features.
'''

# Parent Class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def start_engine(self):
        return f"{self.brand} engine start"

# Child Class (Car) - Inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, fuel_type):
        super().__init__(brand, wheels=4)      # All cars have 4 wheels
        self.fuel_type = fuel_type

    def car_info(self):
        return f"{self.brand} car runs on {self.fuel_type} with {self.wheels} wheels."

    
class Truck(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand, wheels=6)  # All trucks have 6 wheels
        self.capacity = capacity  # Capacity in tons

    def truck_info(self):
        return f"{self.brand} truck can carry {self.capacity} tons with {self.wheels} wheels."



car = Car("Toyota", "Petrol")
truck = Truck("Mahendra", 100)


print(car.car_info())
print(truck.truck_info())

'''
How Inheritance Works Here?
Vehicle is the Parent Class → It has brand, wheels, and start_engine().
Car and Truck are Child Classes → They inherit from Vehicle.
Both child classes have additional features (fuel_type for Car, capacity for Truck).
Each child class uses the parent class methods (start_engine()) and also has its own unique methods (car_info(), truck_info()).

🔥 Why is This Useful?
✅ Reusability – No need to rewrite start_engine() in every class.
✅ Extensibility – We can add more vehicles like Bike, Bus, etc., without changing Vehicle.
✅ Organized Code – Keeps the code structured and easy to maintain.
'''
print("===========================================================")
# Example 3 : Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name}, is working!"

# Child Class (Manager) - Inherits from Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size  # Additional attribute for Manager

    def manage_team(self):
        return f"{self.name}, is managing a team of {self.team_size} people."


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def code(self):
        return f"{self.name} is coding in {self.programming_language}"

class Finance(Employee):
    def __init__(self, name, salary, members):
        super().__init__(name, salary)
        self.members = members

    def financer(self):
        return f"{self.name} is a manager of {self.members}."


mange = Manager("Rolf", 70000, 30)
deve = Developer("Alice", 800000, "Python Developer!")
fince =  Finance("Devid", 50000, 20)

print(mange.work())
print(mange.manage_team())
print(deve.code())
print(fince.financer())
print(fince.name)

all = [Manager("Rolf", 70000, 30), Developer("Alice", 800000, "Python Developer!"), Finance("Devid", 50000, 20)]

for each in all:
    print(each.name, each.salary)


"""
🔥 Why is This Useful?
✅ Reusability – No need to rewrite work() in every class.
✅ Extensibility – We can add more employee roles like Tester, HR, etc.
✅ Organized Code – Keeps the code structured and easy to maintain
"""



print("=====================Multiple Inheritance======================")
'''
Multiple inheritance: It invlves more than one parant class.
'''

# Example
class Parent:
    def play(self):
        return "Plaing Cricket!"

class Parent2:
    def play2(self):
        return "Plaing Football"

class Child(Parent, Parent2):
    def Both(self):
        return "Child Plaing Both games"

main = Child()

print(main.play())
print(main.play2())
print(main.Both())

print("=====================Multilevel Inheritance======================")

'''
Multilevel Inheritance:- The child class acts as a parent class for anothe child class
'''

class GrandParent:
    def func1(self):
        return "This is a Grand parent class!"

class Parent(GrandParent):
    def func2(self):
        return "THis is a Parent class"

class Child(Parent):
    def func3(self):
        return "THis is a Child class"


demo = Child()
print(demo.func1())
print(demo.func2())
print(demo.func3())