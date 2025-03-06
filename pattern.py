"""
print pattern program
1 2 3 4 5
1 2 3 4
1 2 3 
1 2
1

        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1

"""

n = 5

for row in range(n):
    # print(row)
    for col in range(n-row):
        print(col+1, end=" ")
    print()


for row in range(n):
    for space in range(n-row-1):
        print(" ",end=" ")
    for col in range(row+1):
        print(col+1, end=" ")
    print()


"""
print pattern program
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
"""
for row in range(n):
    for col in range(n-row):
        print(row+1, end=" ")
    print()


"""
print pattern program
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
for i in range(n):
    for j in range(n-i):
        print(n-i, end=" ")
    print()


"""
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""

num = 5

for i in range(1, num+1):

    for j in range(num-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        print(j, end=" ")

    for j in range(i-1, 0, -1):
        print(j, end=" ")

    print()

"""
*
***
*****
*******
*********
"""
num2 = 5
for star in range(1, num2+1):
    for j in range(1, star*2):
        print("*", end=" ")
    print()

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
num3 = 5
for i in range(0, num3):
    # Print leading spaces
    for j in range(0, num3 - i - 1):
        print(" ", end="")
    # Print stars with spaces
    for j in range(0, i + 1):
        print("* ", end="")
    # Move to the next line
    print()


# 35. Palindrom pattern
"""
_ _ _ _ _ _ 1 _ _ _ _ _ _
_ _ _ _ _ 1 2 1 _ _ _ _ _
_ _ _ _ 1 2 3 2 1 _ _ _ _
_ _ _ 1 2 3 4 3 2 1 _ _ _
_ _ 1 2 3 4 5 4 3 2 1 _ _
_ 1 2 3 4 5 6 5 4 3 2 1 _
"""
for i in range(0,6):
    for j in range(0, 6-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")

    print()