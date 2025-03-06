

"""
Python uses two strategies for memory allocation: 

Reference counting
Garbage collection

Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.
Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, the virtual machine has a garbage collector that automatically deletes that object from the heap memory


Reference counting works by counting the number of times an object is referenced by other objects in the system. 
When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated.

For example, Let’s suppose there are two or more variables that have the same value, so, what Python virtual machine does is, rather 
than creating another object of the same value in the private heap, it actually makes the second variable point to that originally 
existing value in the private heap. Therefore, in the case of classes, having a number of references may occupy a large amount of 
space in the memory, in such a case referencing counting is highly beneficial to preserve the memory to be available for other objects
"""


"""
When x = 10 is executed an integer object 10 is created in memory and its reference is assigned to variable x, this is because everything is object in Python.
"""

x = 10
y = x 
  
if id(x) == id(y): 
    print("x and y refer to the same object", id(x),id(y)) 

"""
In the above example, y = x will create another reference variable y which will refer to the same object because Python optimizes
 memory utilization by allocation the same object reference to a new variable if the object already exists with the same value.
"""
