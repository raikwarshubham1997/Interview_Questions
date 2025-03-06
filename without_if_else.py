l1 = [1,1,0,0,0,1,0,1,0,1]
count_1 = l1.count(1)
print(count_1)

count_ones = 0
for i in l1:
    count_ones += i
print(count_ones)

print("===================================")
l2 = [5, 5, 0, 0, 0, 5, 0, 5]

count_five = 0
for x in l2:
    count_five += (x==5)
print(count_five)

print("===================================")
l3 = [2,1,4,13,11,34,23,8,9,65]
let = l3[0]

for val in l3:
    print(let * (val <= let))
    max_value = let * (val <= let) + val * (val > let)
print("<<<<",max_value)

for vl in l3:
    min_value = let * (vl >= let) + vl * (vl < let)
print(">>>", min_value)
print("===================================")


# list comprhension

squares = []
for i in range(1,10):
    squares.append(i**2)

print(squares)


sqr = [a ** 2 for a in range(10)]
print(sqr)


even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)


print("==========================================")
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

print("==========================================")
n = 5
for i in range(1, n+1):
    print("*"*i)
print("==========================================")
for a in range(n, 0, -1):
    print("* "*a)
print("==========================================")
print("==========================================")












