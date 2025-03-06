'''
# cunting vowels in a given word
vowels = ['a', 'e', 'i', 'o', 'u']
word ="programming"
count = 0

for vow in vowels:
    if vow in word:
        count+=1
    

if count != 0:
    print("Number of vowels in given word is: ",count)
else:
    print("There have no vowels in given word the counting is: ", count)
print("----------=============================------------")

# counting consonants in a given word
consonants = 0
for wr in word:    
    if wr not in vowels:
        consonants+=1
    else:
        print("There have no consonants in given word the counting is:", consonants)


print("counting of consonants: ", consonants)
print("----------=============================------------")

# Counting the Number of Occurrences of a Character in a String

word = input("Enter a Word: ")
occurence = input("Enter a Occurrences of a Character in a String : ")
count = 0

for wo in word:
    if wo == occurence:
        count+=1
    
if count!=0:
    print(f"Successfully! run Given Character {occurence} present in word :", count)
else:
    print(f"Given Character {occurence} not present in word :", count)

print("----------=============================------------")

# Writing Fibonacci Series
fib =[0,1]
# Range starts from 0 by default
for i in range(5):  
    fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))
print("----------=============================------------")
'''

# 16. Finding the Maximum Number in a List
numberList = [15, 85, 35, 89, 125]
let_max = numberList[0]

for num in numberList:
    if num >= let_max:
        let_max=num
    
print("the Maximum Number in a List : ",let_max)

#17. Finding the Minimum Number in a List
numberList2 = [15, 85, 35, 89, 125, 2]
let_min = numberList[0]

for num in numberList2:
    if num <let_min:
        let_min=num

print("the Minimum Number in a List : ", let_min)
print("----------=============================------------")

# 18. Finding the Middle Element in a List
numList = [1, 2, 3, 4, 5]
midElement = int((len(numList)/2)) 

print(numList[midElement])

print("----------=============================------------")

# 19. Converting a List into a String
lst = ["P", "Y", "T", "H", "O", "N"]
st=""
for i in lst:
    if i != "":
        st+=i

print(st)
print("----------=============================------------")

# 20. Adding Two List Elements Together
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
sumofElement = []
for l1 in range(0,len(lst1)):
    sumofElement.append(lst1[l1]+lst2[l1])

print(sumofElement)
print("----------=============================------------")

# 20. multiply Two List Elements Together
mul1 = [1, 2, 3]
mul2 = [4, 5, 6]
multiply = []
for i in range(0, len(mul1)):
    multiply.append(mul1[i]*mul2[i])

print("multiply : ",multiply)

print("----------=============================------------")

# 20. squer Two List Elements Together

squ1 = [1, 2, 3]
squ2 = [4, 5, 6]
square =[]

for digit in range(0, len(squ1)):
    square.append(squ1[digit]**squ2[digit])

print("Square : ", square)

print("----------=============================------------")

# 20. Subtract Two List Elements Together

sub1 = [1, 2, 3]
sub2 = [4, 5, 6]
subtraction =[]

for digit in range(0, len(sub1)):
    subtraction.append(sub1[digit]-sub2[digit])

print("Subtraction : ", subtraction)
print("----------=============================------------")

# 21. Comparing Two Strings for Anagrams
str1 = "Listen"
str2 = "Silent"

word_len1 = len(str1)
word_len2 = len(str2)
print(word_len1, word_len2)
count = 0
for i in str1:
    if i.lower() in str2 or i.upper() in str2:
        count+=1
    # else:
    #     count

print(count)
if count == word_len1 and count == word_len2:
    print("Given string Anagrams")
else:
    print("Given string not Anagrams")
print("----------=============================------------")

# 22. Checking for Palindrome Using Extended Slicing Technique
str1 = "Kayak".lower()
str2 = "Kayak".lower()
# using slicing
if str1 == str2[::-1]:
    print("Given string palindrome", True)
else:
    print("Not palindrome", False)

print("----------=============================------------")

# 23. Counting the White Spaces in a String
string = "P r ogramm in g "
whiteSpace = 0
for spc in string:
    if spc == ' ':
        whiteSpace+=1
    
print("Numbere of white space in a String: ",whiteSpace)
# or 
print(string.count(' '))
print("----------=============================------------")

# 24. Counting Digits, Letters, and Spaces in a String

name = 'Python is 1'

Digits = 0
Letters = 0
spaces = 0
for data in name:
    print(data)
    if data.isdigit():
        Digits+=1
    if data.isalpha():
        Letters+=1
    if data == ' ':
        spaces+=1


print("Digits : ",Digits, "and", "Letters : ",Letters, "and", "Speces : ", spaces)

# or we can use regex using import re module
import re

digitCount = re.sub("[^0-9]", "",name) 
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall("[ \n]", name)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))

print("----------=============================------------")

# 25. Counting Special Characters in a String
spChar = "!@#$%^&*()"

countSpecial = 0
for spl in spChar:
    if spl != spl.isdigit() and spl != spl.isalpha() and spl != ' ':
        countSpecial += 1

print("Special Characters in String : ", countSpecial)

# or using regex
import re
count = re.sub('[\w]+', '', spChar)
print(len(count))
print("----------=============================-----------")
    
# 26. Removing All Whitespace in a String
string = "C O D E"
removeWhitespace = ""

for i in string:
    if i != ' ':
        removeWhitespace+=i

print("Remove all Whitespace : ",removeWhitespace)

print("----------=============================-----------")

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

print("----------=============================-----------")

from random import shuffle
# 28. Randomizing the Items of a List in Python

lst = ['Python', 'is', 'Easy']

shuffle(lst)
print("Here is random item of a list : ", lst)
print("----------=============================-----------")

# 29. Find the Largest Element in a List

mylst = [1, 2, 3, 4, 5]
letMaxNumIs = mylst[0]
for i in mylst:
    if i > letMaxNumIs:
        letMaxNumIs = i

print("The larget Element in a list : ", letMaxNumIs)

# using predefine method
largestIs = max(mylst)
print("Larget Element: ", largestIs)
print("----------=============================-----------")

# 30. Remove Duplicates from a List
duplicateItem = [1, 2, 2, 3, 4, 4, 5]
removeDuplicate = []
for num in duplicateItem:
    if num not in removeDuplicate:
        removeDuplicate.append(num)

print("Removed Duplicates from a List: ", removeDuplicate)
print("----------=============================-----------")

# 31. Shift All zero at the end of list

I=[1,2,0,0,4,6,7,8,0,0,0]
l1 = []
l2 = []

for num in I:
    if num != 0:
        l1.append(num)
    if num == 0:
        l2.append(num)

finalList = l1+l2
print("All zeros shif at the end : ", finalList)
print("----------=============================-----------")

# O/p=[6,4,2] using slicing
Lst=[1,2,3,4,5,6]
print(Lst[1::2])    # pattern is [start:stop:step]   

# start=which index you want start 
# stop = where you want stop index and 
# step = how many steps left 1,2... 
print("----------=============================-----------")

# 32. Factorial of a Number
"""
it means 
num=5    
factorial is 1*2*3*4*5 and multiply all values 120
num=10
factorial is 1*2*3*4*5*6*7*8*9*10 and multiply all values 3628800
"""
# solve with while loop
num = int(input("Enter Number: "))
fact = 1   #factorial start wit 1  1*2.... 
i=1       # loop will start 1 index

while i<=num:
    fact = fact * i   # fact=1 and i=1 fact=1*1
    i = i+1     # i=1 i=1+1=2 loop execute when i is not greater then or equal to

print(f"The Factoria of : {num}, is {fact}.")

# using for loop
calcu = 1
for i in range(1, num):
    calcu = calcu * i

print("The factorial is : ",fact)
print("----------=============================-----------")

# 32. Merge Two Sorted Lists
lst1 =[1, 3, 5]
lst2 =[2, 4, 6]


merge = sorted(lst1+lst2)

print(merge)

print("----------=============================-----------")
list1 = [1,3,4,9,6,7]
list2 = [2,5,8,10]
# O/p  result = [1,2,3,4,5,6,7,8,9,10]

mergeList = sorted(list1+list2)
print(mergeList)
print("----------=============================-----------")

mylist = [1,4,5,6,8,9,10]
# o/p [6,8,9,10,1,4,5]
sliceList1 = []
sliceList2 = []

for i in range(0, len(mylist)-4):
    sliceList1.append(mylist[i])

for j in range(3, len(mylist)):
    sliceList2.append(mylist[j])

desierOP = sliceList2 + sliceList1

# print(sliceList1," ",sliceList2)
print("The Desier output is : ", desierOP)
print("----------=============================-----------")

# reverse number 123
num = 123
rev = 0

while num > 0:
    rev = (rev*10) + num%10
    num = num//10

print("The reverse number :", rev)


print("----------=============================-----------")
mynum = 54321

reverse = 0
while mynum > 0:
    reverse = (reverse * 10)+ mynum%10
    print(reverse)
    mynum = mynum//10

print("Number Reverse : ", reverse)
print("----------=============================-----------")

# 33. find items which is not present in list 
lst = [1,3,5,7,9]
# o/p [2,4,6,8,10]
ItemNotInList =[]

for i in range(1, 11):
    if i not in lst:
        ItemNotInList.append(i)

print("List of items which is not in default lis: ", ItemNotInList)
print("----------=============================-----------")

# 34. check palindrom string in this
string = "Madam like apple level eat"
spl = string.split(" ")
print(spl)

palindrom =[]
count = 0

for st in spl:
    print(st)
    if st.lower() == st[::-1].lower():
        count+=1
        palindrom.append(st)

print("Palindrom words in the staring : ", palindrom, "Count :", count)
print("----------=============================-----------")
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
print("----------=============================-----------")

# 36. Find the First Non-Repeating Character

def first_non_repeting_character(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None
result = first_non_repeting_character("swiss")
print("First non-repeting character is : ", result)
