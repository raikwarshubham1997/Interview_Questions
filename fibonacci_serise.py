"""
फिबोनाची श्रृंखला एक ऐसी संख्याओं की श्रृंखला होती है, जहाँ हर अगली संख्या पिछली दो संख्याओं के योग के बराबर होती है।
यह श्रृंखला इस प्रकार होती है:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …

संख्याओं का नियम:
F(n)=F(n−1)+F(n−2)

जहाँ,

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)  (जब n≥2)
"""

def fibonacci(num):
    a , b = 0, 1
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

print("\n============== Fibonacci Serise Using Recursion ==============")

# f(n) = f(n-1)+f(n-2)
def FibonacciSerise(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return FibonacciSerise(num-1) + FibonacciSerise(num-2)

for i in range(10):
    print(FibonacciSerise(i), end=" ")


print("\n=============Recursion Example==============")

# def infinite_recursion():
#     print("Calling...")
#     infinite_recursion()  # No base condition

# infinite_recursion()
# इससे Stack Overflow होगा क्योंकि यह कभी नहीं रुकेगा।