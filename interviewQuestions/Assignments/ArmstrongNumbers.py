"""
Python program to check Armstrong Number

formula is xyz = x^n + y^n + z^n......

8891 = order 4   # x^4 + y^4 + z^4
389 = order 3    # x^3 + y^3 + z^3  (if the solution of this is equal to 389 means Armstrong number)

8891%10=1
889%10=9
88%10=8
8%10= 8
0

"""
# Armstrong no 153


n = int(input("Enter Number: "))
s = n
pwr = len(str(n))
num = 0
while n != 0:
    #get remainder and square of pwr
    r = n%10
    num = num+(r**pwr)
    n=n//10      #153//10 = 15, 15//10 = 1
if s == num:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")

