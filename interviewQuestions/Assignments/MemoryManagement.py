"""
Types of memory 
1. Stack Memory  (all our references & methods and method calls store in stack memory)
2. Private Heap Memory (whereas when we store any value or an object then we use of private heap memory)
"""
x = 5 
# here x is referencing to an object (5). x stored in stack memory
# 5 is a object stored in private heap memory
'''
so x here is referring to an object 5.that is x will be treated as a reference which will 
be stored in stack memory. whereas 5 is a value/object which would be stored in a private heap memory.
'''
# x - reference Stack memory 
# 5 - value/object private heap memory

print(type(x))   # <class 'int'>
print(id(x))     # 139857646791088

'''
in the same way I can defined y=x
'''
y = x
print(type(y))  # <class 'int'>
print(id(y))    # 139857646791088
# both id will same bcoz x value is 5 and y referring x here y is reference

'''
the meaning of this is y is a reference which is referring the object refered by x. when we modified
the value of x its type will be int and id different.
'''
x = x + 1
print(type(x))   # <class 'int'>
print(id(x))     # 140618819590608
# in this case x referring is diffrent value 6. type is same but id is diffrent.

# x -> 6
# y -> 5

if id(x) != id(y):
    print("It's Diffrent!")

# both x and y are reffering to diffrent object.



