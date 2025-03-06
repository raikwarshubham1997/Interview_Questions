# create decorator adding 2 numbers

def add_two_numbers_decorator(func):
    def two_numbers(a, b):
        result = a + b
        return func(result)
    return two_numbers

@add_two_numbers_decorator
def displayresult(result):
    print(f"The result is:", result)


displayresult(12,5)


#find count of geeks
a="geeks for geeks"
#o/p:- 2

def CountValue(funct):
    def value(st):
        cunt = {}
        spl = st.split()
        print(spl)
        for stv in spl:
            if stv == 'geeks':
                if stv in cunt:
                    cunt[stv] += 1
                else:
                    cunt[stv] = 1
        return funct(cunt)
    return value

@CountValue
def displayResult(cunt):
    print(f"The result is: ", cunt)

st = 'geeks for geeks'
displayResult(st)

print("===================================================")
# add two numbers
def Addition(func):
    def wrapper(a, b):
        result = a+b
        print(result)
        return func(a,b)
    return wrapper

@Addition
def TakeFunc(a,b):
    print(f"Value of {a} and {b} : ", a, b)

TakeFunc(5,6)


print("============================================")

def DecoratorFunction(func):
    def wrapper():
        print("Before Function call!")
        func()
        print("After function call!")

    return wrapper

@DecoratorFunction
def hello():
    print("Hello, World!")


hey = hello()

print("============================================")

