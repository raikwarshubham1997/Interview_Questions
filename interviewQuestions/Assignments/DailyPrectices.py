# prime number (number is divisible by 1 or itself call prime number)
take = int(input("Enter a number and Check prime or not : "))
count = 0

for i in range(1,take+1):
    if take % i == 0:
        count += 1

if count == 2:
    print("Given number is prime!")
else:
    print("Given number not a prime!")

# while loop

c = 0
i = 1
while i<=take:
    if take%i == 0:
        c+=1
    i=i+1

# print(c)
if c == 2:
    print("Given number is prime!")
else:
    print("Given number not a prime!")

print("================Armstrong Number================")
'''
ex =
153 get len(153)
1^3 + 5^3 + 3^3 the calculation is equal given 153 it means Armstrong
'''
number =  int(input("Enter Digit: "))
orignal = number
power = len(str(number))
total = 0

while number != 0:
    r = number%10    # 153%10 = 15.3 =(3) reminder
    total = total + (r**power)
    number = number//10   # 153//10 = 15, 15//10=1

if total == orignal:
    print("Number is Armstrong!")
else:
    print("Number is Not Armstrong!")

print("==================Recursion===============")
# create fibonacci serise function
# formula --> f(n) = f(n-1)+f(n-2)
def fibonacci(num):
    # Base condition
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

for i in range(10):
    print(fibonacci(i), end=" ")

print("===================================")
# without recursion
def fibonacci2(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

fibonacci2(10)

print("=====================Decorator Function=====================")
# Simple example
def WelcomeDecorator(Hello):
    def wrapper():
        print("Welcome to Python")
        Hello()
        print("This is first Decorator function")
    return wrapper

@WelcomeDecorator
def Hello():
    print("Hello! World")

obj = Hello()

#  with strong example
def SumofTwoNumberDecorator(Addition):
    def wrapper(a,b):
        Addition(a,b)
        c= a + b
        return c
    return wrapper
    

@SumofTwoNumberDecorator
def Addition(a,b):
    print("This function take two argumnets!")

sumofTwo = Addition(5,6)
print(sumofTwo)

print("===================Anagrams value=======================")
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = ["eat","tea","tan","ate","nat","bat"]

final = []
for wrd in strs:
    anag = []
    for j in strs:
        if wrd == j:
            anag.append(j)
        else:
            c = 0
            for k in wrd:
                if k in j:
                    c+=1
            if c==3:
                anag.append(j)
    if anag in final:
        pass
    else:
        final.append(anag)

print(final)
