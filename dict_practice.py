thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


"""
thisdict = [{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
},{
  "brand": "Jeep",
  "model": "campus",
  "year": 2010
},{
  "brand": "Mahendra",
  "model": "Thar",
  "year": 1999
},{
  "brand": "Maruti",
  "model": "Swift",
  "year": 1964
}]
"""

print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])

# Duplicates Not Allowed
# Duplicate values will overwrite existing values:
thisdict_2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2000
}
print(thisdict_2)

print(len(thisdict))

'''
Dictionary Items - Data Types
The values in dictionary items can be of any data type:

Example
String, int, boolean, and list data types:
'''
thisdict_3 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict_3)

# Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict_4 = dict(name="John", age=23, country="Norway")
print(thisdict_4)

thisdict_5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict_5["model"]
print(x)
x = thisdict_5.get("model")
print(x)

y = thisdict_5.keys()
print(y)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

t = car.keys()
print(t)

car["color"] = "Red"
print(car)
print(car.keys())


v = car.values()
print(v)

car["year"] = 2000
print(car)

car["color"] = "Red"
print(car.values())

"""
Get Items
The items() method will return each item in a dictionary, as tuples in a list.
"""
print(car.items())

dt = car.pop("model")
print(car)

dt2 = car.popitem()
print(car)

del car["year"]
print(car)

arrdict = [{
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
            },{
            "brand": "Jeep",
            "model": "campus",
            "year": 2010
            },{
            "brand": "Mahendra",
            "model": "Thar",
            "year": 1999
            },{
            "brand": "Maruti",
            "model": "Swift",
            "year": 1964
          }]

# get all brand names
lst=[]
dct = {}
for brnd in arrdict:
    print(brnd["brand"])
    lst.append(brnd["brand"])
car["brand"] = lst
print(lst)
print(">>>>>>>",car)

print("=====================================================")

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}, 
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}, 
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
        } 

