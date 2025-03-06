# Write a program to calculate square of a given no?

inp = int(input("Enter a number to get square : "))

sqr = inp**2
print(f"The Square of {inp} is: ", sqr)

# without argument 
def square():
    inp = int(input("Enter a number to get square : "))
    sqr = inp**2
    print(f"The Square of {inp} is: ", sqr)

square()

# with argument

def square(num):    
    sqr = num**2
    return f"The Square of {inp} is: ", sqr

inp = int(input("Enter a number to get square : "))
result = square(inp)
print(result)

# using decorator 
def my_square(func):
    def wrapper():
        num = int(input("Enter a number to get square : "))
        sqr = num**2
        print(f"The Square of {num} is: ", sqr)
        func()
    return wrapper

@my_square
def the_input():
    print("This is the orignal function")


the_input()
        

