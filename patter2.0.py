"""   *
     * *
    * * *
   * * * *
  * * * * *
  """

for row in range(0, 5):
    for space in range(0, 5-row):
        print("", end=" ")
    for star in range(0, row+1):
        print("*", end=" ")
    print()    #for new line

# using function
print("============Pyramid using Function==========")
def PrintPyramid(rng):
    for row in range(0, rng):
        for space in range(0, rng-row):
            print("", end=" ")
        for star in range(0, row+1):
            print("*", end=" ")

        print()

row = PrintPyramid(5)

print("============Pyramid using Decorator==========")
def DecoratorPattern(star):
    def wrapper(num):
        for row in range(0,num):
            for space in range(0,num-1):
                print("", end="")
            for strr in range(0,row+1):
                print("*", end=" ")
            print()
        return star
    return wrapper

@DecoratorPattern
def star(num):
    print(f"Pattern range is {num}")

obj = star(5)

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

for i in range(0, 5):
    for j in range(0, 5-i):
        print(" ", end="")
    for k in range(0, i+1):
        print("*", end="")
    print()

for l in range(1,5):
    for n in range(0, l+1):
        print(" ", end="")
    for m in range(0, 5-l):
        print("*", end="")
    print()

"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
 * * * * * * * *
    * * * * * 
      * * * 
        *
"""

for row in range(0, 5):
    for space in range(0, 6-row):
        print(" ", end=" ")
    for star in range(1, row*2):
        print("*", end=" ")
    print()

for row in range(0, 5):
    for space in range(0, row+1):
        print(" ", end=" ")
    for star in range(1, (5-row)*2):
        print("*", end=" ")

    print()


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

for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end="")
    print()

for x in range(1,5):
    for y in range(0,5-x):
        print("*", end="")
    print()