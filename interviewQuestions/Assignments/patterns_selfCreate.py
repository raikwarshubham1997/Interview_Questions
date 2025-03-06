# 27. Building a Pyramid in Python
n = 5
for i in range(0,n):
    for j in range(0,n-i):
        print(" ", end="")
    for j in range(0, i+1):    # first time i=0 thats why i+1
        print("* ", end="")

    print()

print("----------=============================-----------")

for i in range(0,n):
    for j in range(0,i+1):
        print("_", end="")
    for j in range(0, n-i):
        print("* ", end="")

    print()
print("----------=============================-----------")

for i in range(0,n):
    for j in range(0,n-i):
        print(" ", end="")
    for j in range(0, i+1):    # first time i=0 thats why i+1
        print("* ", end="")

    print()

for i in range(0,n):
    for j in range(0,i+1):
        print("_", end="")
    for j in range(0, n-i):
        print("* ", end="")

    print()

print("----------=============================-----------")

for i in range(0,n):
    for j in range(0,i+1):
        print("_", end="")
    for j in range(0, n-i):
        print("* ", end="")

    print()

for i in range(0,n):
    for j in range(0,n-i):
        print(" ", end="")
    for j in range(0, i+1):    # first time i=0 thats why i+1
        print("* ", end="")

    print()

print("----------=============================-----------")

"""
* 
** 
*** 
**** 
*****
****
***
**
*
"""
for i in range(0,n):        # this loop print row
    for j in range(0, i+1):   # this loop print start
        print("*", end=" ")
    print()

for i in range(1,n):
    for j in range(0,n-i):
        print("*", end=" ")
    print()

print("----------=============================-----------")
"""
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
"""

for i in range(0,n):
    for j in range(0,i+1):   # for space print
        print(" ", end="")
    for j in range(0, n-i):   #print star
        print("*", end=" ")
    print()    # for lin change

for i in range(1, n):
    for j in range(0, n-i):
        print(" ", end="")
    for j in range(0,i+1):
        print("*", end=" ")
    print()
print("----------=============================-----------")

"""
     *
    **
   ***
  ****
 *****
"""

for i in range(0, n):
    for j in range(0, n-i):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print()

"""
          *
        * *
      * * * 
    * * * *
  * * * * *
"""
for i in range(0, n):
    for j in range(0, n-i):
        print(" ", end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()

"""
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
"""

for i in range(0, n):
    for j in range(0, n-i):
        print(" ", end="")     # for pyramid shap end="" no space b/w ""
    for j in range(0, i+1):
        print("*", end=" ")
    print()

print("----------=============================-----------")

"""
*****
 ****
  ***
   **
    *
"""
for i in range(0, n):
    for j in range(0, i+1):
        print(" ", end="")
    for j in range(0, n-i):
        print("*", end="")

    print()
print("----------=============================-----------")
"""
1
12
123
1234
12345
"""
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1, end="")

    print()

print("----------=============================-----------")

"""
12345
1234
123
12
1
"""
for i in range(0,n):
    for j in range(0, n-i):
        # print("value of J : ",j)
        print(j+1, end="")
    print()

print("----------=============================-----------")

"""
2
2 4
2 4 6 
2 4 6 8
2 4 6 8 10
2 4 6 8 10 12
2 4 6 8 10 12 14
2 4 6 8 10 12 14 16
2 4 6 8 10 12 14 16 18
2 4 6 8 10 12 14 16 18 20
"""

for i in range(0, 10+1):    
    for j in range(1, i+1):
        print(j*2, end=" ")
    print()

print("----------=============================-----------")
"""
2 4 6 8 10 12 14 16 18 20
2 4 6 8 10 12 14 16 18
2 4 6 8 10 12 14 16
2 4 6 8 10 12 14
2 4 6 8 10 12
2 4 6 8 10
2 4 6 8
2 4 6
2 4
2
"""
for i in range(0, 10):
    for j in range(1, 11-i):
        # print(">>>> J", i)
        print(j*2, end=" ")
    print()