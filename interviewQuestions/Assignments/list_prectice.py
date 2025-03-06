'''
# 1. Sum all the items in a list
lst = [10, 12, 20, 22]
sum_is = 0
for i in lst:
    sum_is += i
print(sum_is)


# Define a function called sum_list that takes a list 'items' as input
print("=================using function===================")

def sum_list(items):
    sum_num = 0

    for item in items:
        sum_num += item
    
    return sum_num

ls = [10, 12, 20, 22]
result = sum_list(ls)
print(result)

print("===============solve using decorator==================")
def sum_decorator(func):
    def wrapper(items):
        sum_num = 0
        for itm in items:
            sum_num += itm
        return sum_num
    return wrapper

@sum_decorator
def MainFunc(items):
    print("This is main function")

ls = [10, 12, 20, 22]
result = MainFunc(ls)
print(result)

print("==============================================")
# 2.  Multiply Items in List
ml = [2,4,5,8]
final = 1
for m in ml:
    final = final*m

print(final)

print("=================using function===================")
def multiply(items):
    mul = 1
    for i in items:
        mul = mul*i
    return f"Multiplication of the list items is : {mul}"

ml = [2,4,5,8]
result =  multiply(ml)
print(result)

print("=================using Decorator===================")

def multi_decorator(func):
    def wrapper(items):
        mul = 1
        for m in ml:
            mul = mul*m
        original_func_call = func(items)
        return f"{original_func_call} | {mul}"
    return wrapper

@multi_decorator
def main_func2(items):
    #pass    # over all handled by above function
    return f"This is Main function"

mll = [2,4,5,8]
res = main_func2(mll)
print(res)
    

# Get Largest Number in List
mylst = [1, 2, -8, 0]
maxx = mylst[0]
minn = mylst[0]
for i in mylst:
    if i > maxx:
        maxx = i
    

for low in mylst:
    if low < minn:
        minn = low

print("The largest number of list is: ", maxx)
print("The lowest number of list is: ", minn)




def find_maxno(myls):
    letMax = myls[0]
    for i in myls:
        if i > letMax:
            letMax = i
    return f"The maximum element of list: ",letMax

mlst = [1, 2, -8, 0]
mx =  find_maxno(mlst)
print(mx)

def find_minno(myls):
    letMin = myls[0]
    for i in myls:
        if i < letMin:
            letMin = i
    return f"The minimum element of list: ",letMin

mlst = [1, 2, -8, 0]
mi =  find_minno(mlst)
print(mi)

print("==============================================")
"""
5. Count Strings with Same Start and End

Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
givenlst = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in givenlst:
    if i[0] == i[-1]:
        print(i)
        count+=1

print(count)


print("==============================================")
"""
6. Sort Tuples by Last Element

Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
sortBylastelement = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lastelement = []
for i in sortBylastelement:
    lastelement.append(i[1])
lastelement.sort()
print("ss",lastelement)

finalSorted =[]
for k in lastelement:
    print(">>>>>", k)
    for j in sortBylastelement:
        print(j[1], j)
        if k == j[1]:
            print(bool(True))
            finalSorted.append(j)

print(finalSorted)

print("==============================================")

"""
7. Remove Duplicates from List

Write a Python program to remove duplicates from a list.
"""
comm = [1,2,4,7,5,2,1,6,4,9,8,21,3,5]

# first approach
remvDup = []
for i in comm:
    if comm.count(i)==1:
        remvDup.append(i)
    
print(remvDup)

# secound approach
f = {}
noduplicate =[]
for j in comm:
    if j in f:
        f[j] += 1
    else:
        f[j] = 1
print(f)

for key, val in f.items():
    if val == 1:
        noduplicate.append(key)
print(noduplicate)


print("==============================================")
"""
8. Check if List is Empty
Write a Python program to check if a list is empty or not.
"""
def CheckListEmpty(mylist):
    if len(mylist) == 0:
        return "List have No data ",mylist
    else:
        return "List is not empty", mylist

l1 = CheckListEmpty([])
l2 = CheckListEmpty([1,2,3])
print(l1)
print(l2)
print("==============================================")
"""
9. Clone or Copy a List
Write a Python program to clone or copy a list.
"""
orignalls = [1,2,3,4,5]
copyls = orignalls.copy()

print(orignalls)
print(copyls)
print("==============================================")

"""
10. Find Words Longer Than n
Write a Python program to find the list of words that are longer than n from a given list of words.
"""
stri = "The quick brown fox jumps over the lazy dog"
x = stri.split(" ")
print(x)
n = int(input("Enter number to find word which is length is greater then n: "))
longer = []
for wrd in x:
    if len(wrd)>n:
        longer.append(wrd)

print(longer)
print("==============================================")

"""
11. Check Common Member Between Two Lists
Write a Python function that takes two lists and returns True if they have at least one common member.
"""
def find_at_leastOne_common(s1,s2):
    bool = False
    count = 0
    for i in s1:
        for j in s2:
            if j == i:
                bool = True
                count+=1
    return f"There have {count} common member in both list: ",bool
lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 6, 7, 8, 9]

finalResult = find_at_leastOne_common(lst1, lst2)
print(finalResult)

print("Using decorator")

print("==============================================")
def find_at_leastOne_commonDecorator(func):
    def wrapper(ls1,ls2):
        bool = False
        count = 0
        for i in ls1:
            for j in ls2:
                if j == i:
                    bool = True
                    count+=1
        print(f"There have {count} common member in both list: ",bool)
        return func(ls1,ls2)
    return wrapper

@find_at_leastOne_commonDecorator
def anyCommon(lst1, lst2):
    print(f"The two list is {lst1}, {lst2}")
lst01 = [1, 2, 3, 4, 5]
lst02 = [5, 6, 7, 8, 9, 4]
commonobj1 = anyCommon(lst01,lst02)


print("==============================================")
"""
12. Remove Specific Elements from List
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

removeData = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
remv = [0,4,5]
fin ={}
finaloutput = []
print(">>>>", len(removeData))

# convert list to dictionary
for rem in range(0,len(removeData)):
    fin[rem] = removeData[rem]
print(fin)

# compair index and delete match case in a dictionary
for i in remv:
    if i in fin:
        # print(True, i)
        del fin[i]

# all values append in a list
for k in fin.values():
    finaloutput.append(k)

print(fin)
print(finaloutput)

"""
Solve using function
"""

def RemoveByIndex(lst, ind):
    fin ={}
    finaloutput = []

    # convert list to dictionary
    for rem in range(0,len(lst)):
        fin[rem] = lst[rem]
    print(fin)

    # compair index and delete match case in a dictionary
    for i in remv:
        if i in fin:
            # print(True, i)
            del fin[i]

    # all values append in a list
    for k in fin.values():
        finaloutput.append(k)

    # print(fin)
    # print(finaloutput)
    return finaloutput



resultInx = RemoveByIndex(removeData, remv)

print(resultInx) 
            
    
print("==============================================")

"""
13. Generate 3D Array

Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""
# Create a 3D array using list comprehensions, with 3 rows, 4 columns, and each element initialized as '*'
array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]

# Print the resulting 3D array
print(array)
print("==============================================")

"""
14. Remove Even Numbers from List
Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""
mixedList = [1,2,3,4,5,6,7,8,9,10]

def MixedOddEven(lst):
    l=[]
    for num  in mixedList:
        if num % 2 == 0:
            del num
        else:
            l.append(num)

    return l

ob = MixedOddEven(mixedList)
print(ob)
print("================================================")



# using while loop 
num = 11
count = 0
i = 1
while i <= num:
    if num % i == 0:
        count+=1
    i = i+1

if count == 2:
    print("Number is Prime!")
else:
    print("Not prime")



# using four loop
n=11
c=0

for j in range(1,n+1):
    if n%j==0:
        c+=1
if c == 2:
    print("Number is prime")

else:
    print("Not a prime")

print("================================================")

"""
15. Shuffle List
Write a Python program to shuffle and print a specified list.
"""
from random import shuffle
ll = ['Red','Black','White','Blue']
shuffle(ll)
print(ll)
print("================================================")

"""
16. Generate Square Numbers in Range
Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
"""
def printValues():
    # Create an empty list 'l'
    l = list()
    # Loop from 1 to 20 (inclusive)
    for i in range(1, 21):
        # Calculate the square of 'i' and append it to the list 'l'
        l.append(i**2)
    # Print the first 5 elements of the list 'l'
    print(l[:5])
    # Print the last 5 elements of the list 'l'
    print(l[-5:])

# Call the printValues function to execute it
printValues()
print("================================================")
"""
17. Check If All Numbers Are Prime

Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False
"""

def is_prime(n):
    print("n", n)
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_primes(lst):
    print(lst)
    return all(is_prime(num) for num in lst)

# Sample test cases
print(all_primes([0, 3, 4, 7, 9]))  # False
print(all_primes([3, 5, 7, 13]))    # True
print(all_primes([1, 5, 3])) 

print("================================================")
"""
18. Calculate Difference Between Lists
Write a  Python program to calculate the difference between the two lists.
"""
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]

# set use bcoz list doesn't allow subtraction

print("set(list1)", set(list1))
print("set(list2)",set(list2))
diff_list1_list2 = list(set(list1) - set(list2))
print(diff_list1_list2)

diff_list2_list1 = list(set(list2) - set(list1))
print(diff_list2_list1)

total_diff = diff_list1_list2 + diff_list2_list1

print(total_diff)

print("================================================")
"""
Find Common Elements Between Two Lists
Write a Python program to find the common elements between two lists.
"""

list01 = [1, 2, 3, 4, 5]
list02 = [3, 4, 5, 6, 7]

commomEle = []

for i in list01:
    if i in list02:
        commomEle.append(i)

print("Common Elements: ", commomEle)

# without using predefind function
for i in list01:
    for j in list02:
        if i == j:
            if i not in commomEle:
                commomEle.append(i)
print(commomEle)

print("================================================")
"""
20. Access List Indices
Write a Python program to access the index of a list.
"""

def AccessIndex(lss,ind):
    for ele in range(len(lss)):
        if ind == ele:
            return f"The value of index {ele}",lss[ele]
        # else:
        #     return "list outoff index"
    return "list outoff index"
mylist = [11,23,12,34,45,65,44]
com = int(input("Enter Index number and get the value : ",))
sd = AccessIndex(mylist, com)
print(sd)

print("================================================")
"""
21. Convert List to String
Write a Python program to convert a list of characters into a string.
"""



chr1 = ["P","Y","T","H","O","N"]
dxo = "".join(chr1)
print(dxo)


# using function
def ConvertListToStr(ch):
    gh = "".join(ch)
    return gh

chr2 = ["w","3","r","e","s","o","u","r","c","e"]
objst1 = ConvertListToStr(chr1)   
objst2 = ConvertListToStr(chr2) 
print(objst1)
print(objst2)
print("================================================")

"""
22. Find Index of List Item
Write a Python program to find the index of an item in a specified list.
"""
def FindIndexOfItem(lst,item):
    for i in range(len(lst)):
        if lst[i] == item:
            return f"Index of Item : {i}"
indx = int(input("Enter element of list and get index of its: "))
checkInd = [10, 30, 29, 38, 45,-21]

inx = FindIndexOfItem(checkInd, indx)
print(inx)


print("================================================")
"""
24. Append One List to Another
Write a Python program to append a list to the second list.
"""
def AppendAListToSecond(ls1, ls2):
    append_ls1_ls2 = ls1 + ls2
    return append_ls1_ls2

ad = AppendAListToSecond([1,2,3,4],["Red","Green","Blue"])
print(ad)

print("================================================")

"""
25. Select Random Item from List
Write a Python program to select an item randomly from a list.
"""
import random
# Define a list 'color_list' containing various colors
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']

print(random.choice(color_list))

#using function
from random import choice

# Define a function named 'random_element' that takes a list 'lst' as a parameter
def random_element(lst):
    return choice(lst)

print(random_element([2, 3, 4, 7, 9, 11, 15]))
print("================================================")

words = ['how', 'much', 'is[br]', 'the', 'fish[br]', 'no', 'really']
#find [br] and replace it with <br/>

new_list = []
for word in words:
    modified_word = ''
    i=0
    while i < len(word):
        if word[i:i+4] == '[br]':
            modified_word += '<br/>'
            i+=4
        else:
            modified_word += word[i]
            i+=1
    new_list.append(modified_word)

print(new_list)

        

'''
print("================================================")
lst=[1,2,0,0,4,6,7,8,0,0,0]
l = []
for num in lst:
    if num > 0:
        print(num)
        l.insert(0, num)
    else:
        print(num)
        l.append(num)
print(l)

print("================================================")
"""
26. Check Circularly Identical Lists
Write a Python program to check whether two lists are circularly identical.
"""

# Define three lists: list1, list2, and list3, each containing a sequence of numbers
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

# Compare list1 and list2
print('Compare list1 and list2')

# Check if the string representation of list2 is present in the string representation of list1 repeated twice
# The result will be True if list2 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))

# Compare list1 and list3
print('Compare list1 and list3')

# Check if the string representation of list3 is present in the string representation of list1 repeated twice
# The result will be True if list3 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))) 
print("================================================")
"""
27. Find Second Smallest Number in List
Write a Python program to find the second smallest number in a list.
"""
# using simple function 
def Second_Smallest(numbers):
    # Check if the length of the 'numbers' list is less than 2; return None in this case
    if len(numbers) < 2:
        return

    # Check if there are only two elements in the 'numbers' list, and they are the same; return None in this case
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return

    # Create an empty set 'dup_items' to store duplicate items and an empty list 'uniq_items' to store unique items
    dup_items = set()
    uniq_items = []

    # Iterate through the elements in the 'numbers' list
    for x in numbers:
        # Check if 'x' is not in 'dup_items'; if not, add it to 'uniq_items' and 'dup_items'
        if x not in dup_items:
            uniq_items.append(x)       # list method "append" for add item in a list
            dup_items.add(x)           # set method "add" method to add item in a set
                     
    # Sort the 'uniq_items' list in ascending order
    # print("unique items: ", uniq_items)
    uniq_items.sort()
    # print(uniq_items)

    # Return the second smallest item from the sorted 'uniq_items' list, which is at index 1
    return uniq_items[1]



s1 = Second_Smallest([1, 2, -8, -2, 0, -2])
s2 = Second_Smallest([1, 1, 0, 0, 2, -2, -2])
s3 = Second_Smallest([1, 1, 1, 0, 0, 0, 2, -2, -2])
s4 = Second_Smallest([2, 2])
s5 = Second_Smallest([2])

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print("--------------------Output from Decorator----------------------")
#using Decorator
def SecondSmallestNumByDecorator(func):
    def wrapper(numbers):
        result = func(numbers)  # Call the original function
        if result is not None:
            print("From Decorator:", result)
        return f"The second Smallest Number in the list is {result}"  # Return the result
    return wrapper



@SecondSmallestNumByDecorator
def Second_Smallest(numbers):
    # Check if the length of the 'numbers' list is less than 2; return None in this case
    if len(numbers) < 2:
        return

    # Check if there are only two elements in the 'numbers' list, and they are the same; return None in this case
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return

    # Create an empty set 'dup_items' to store duplicate items and an empty list 'uniq_items' to store unique items
    dup_items = set()
    uniq_items = []

    # Iterate through the elements in the 'numbers' list
    for x in numbers:
        # Check if 'x' is not in 'dup_items'; if not, add it to 'uniq_items' and 'dup_items'
        if x not in dup_items:
            uniq_items.append(x)       # list method "append" for add item in a list
            dup_items.add(x)           # set method "add" method to add item in a set
                     
    # Sort the 'uniq_items' list in ascending order
    # print("unique items: ", uniq_items)
    uniq_items.sort()
    # print(uniq_items)

    # Return the second smallest item from the sorted 'uniq_items' list, which is at index 1
    return uniq_items[1]



s1 = Second_Smallest([1, 2, -8, -2, 0, -2])
s2 = Second_Smallest([1, 1, 0, 0, 2, -2, -2])
s3 = Second_Smallest([1, 1, 1, 0, 0, 0, 2, -2, -2])
s4 = Second_Smallest([2, 2])
s5 = Second_Smallest([2])

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print("================================================")

"""
28. Find Second Largest Number in List

Write a Python program to find the second largest number in a list.
"""

# simple function
def Second_Larget(numbers):
    if len(numbers) < 2:   # if length
        return

    if len(numbers) == 2 and numbers[0]==numbers[1]:
        return
    

    dup_items = set()
    uniq_items = []

    # Iterate through the elements in the 'numbers' list
    for x in numbers:
        # Check if 'x' is not in 'dup_items'; if not, add it to 'uniq_items' and 'dup_items'
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    uniq_items.sort()
    # print(uniq_items)

    return f"Second Largest item is {uniq_items[-2]}"

a1 = Second_Larget([1,2,-8,-2,0,-2])
a2 = Second_Larget([-6, 7, -8, 12, 4])
a3 = Second_Larget([89, 0, -23, 63, 63])
a4 = Second_Larget([-27, 36, -36, -15, -2])
print(a1)
print(a2)
print(a3)
print(a4)

print(Second_Larget([1, 2, 3, 4, 4]))
print(Second_Larget([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(Second_Larget([2, 2]))  # Edge case with two identical elements, returns None
print(Second_Larget([1])) 

print("--------------------Output from Decorator----------------------")
# using decorator
def SecondLargetNumByDecorator(func):
    def wrapper(numbers):
        # there is modifing orignal function without change thier structure using decorator
        c = 0
        for i in numbers:
            c +=i
        print("The sum of all number : ",c)
        res = func(numbers)
        return f"By Decorator : {res}"
    return wrapper

@SecondLargetNumByDecorator
def Second_Larget(numbers):
    if len(numbers) < 2:   # if length
        return

    if len(numbers) == 2 and numbers[0]==numbers[1]:
        return
    

    dup_items = set()
    uniq_items = []

    # Iterate through the elements in the 'numbers' list
    for x in numbers:
        # Check if 'x' is not in 'dup_items'; if not, add it to 'uniq_items' and 'dup_items'
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    uniq_items.sort()
    # print(uniq_items)

    return f"Second Largest item is {uniq_items[-2]}"

a1 = Second_Larget([1,2,-8,-2,0,-2])
a2 = Second_Larget([-6, 7, -8, 12, 4])
a3 = Second_Larget([89, 0, -23, 63, 63])
a4 = Second_Larget([-27, 36, -36, -15, -2])
print(a1)
print(a2)
print(a3)
print(a4)

print(Second_Larget([1, 2, 3, 4, 4]))
print(Second_Larget([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(Second_Larget([2, 2]))  # Edge case with two identical elements, returns None
print(Second_Larget([1])) 


print("================================================")
"""
29. Get Unique Values from List
Write a Python program to get unique values from a list.
"""
my_list = [10, 20, 30, 40, 20, 50, 60, 40, 20]
print("Orignal List", my_list)
# this is using pre-defined function
get_uniq = set(my_list)
print("Unique list: ", get_uniq)

# doing more pythonic way

'''
use this method when repeted value want in a list
'''
lst1 = []
for i in my_list:
    if i not in lst1:
        lst1.append(i)
print(lst1)

'''
use this when excluded repeted values
'''
d = {}
final = []
c = 1
for key in my_list:
    if key not in d:
        d.update({key:c})
    else:
        d[key] += 1

print(d)

# for l in d.items():
#     if l[1] == 1:
#         print(l[0])

for j,k in d.items():     #return tuple
    
    if k ==1:
        final.append(j)

print("Unique Values: ", final)



# function base

def Find_UniqueElement(list1):
    l = []
    for x in list1:
        if x not in l:
            l.append(x)
            

    return f"Unique Element by Function, {l}"

obj = Find_UniqueElement(my_list)
print(obj)



# using Decorator
def Find_UniqueElementByDecorator(getlistFunc):
    def FindUnique(list1):
        orig = getlistFunc(list1)
        print(orig)
        d = {}
        v = []
        # c = 1
        for x in list1:
            if x not in d:
                d.update({x:1})
            else:
                d[x] += 1

        for j, k in d.items():
            if k == 1:
                v.append(j)

        return f"Unique values by Decorator, {v}"
    return FindUnique
                
                


@Find_UniqueElementByDecorator
def Find_UniqueElement(list1):
    l = []
    for x in list1:
        if x not in l:
            l.append(x)
            

    return f"Unique Element by Function, {l}"

obj = Find_UniqueElement(my_list)
print(obj)
print("================================================")
"""
30. Count Frequency of List Elements
Write a Python program to get the frequency of elements in a list.
"""
def CountFrequency(list2):
    dc = {}
    # c = 1
    for elemnt in list2:
        if elemnt not in dc:
            dc.update({elemnt:1})
        else:
            dc[elemnt]+= 1

    return dc

my_list12 = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

c1 = CountFrequency(my_list12)
print("Original List :",my_list12)
print("Frequency of the elements in the List :",c1)
# o/p {10:4, 20:4, 40:2, 50:2, 30:1}

print("================================================")
"""
Sift all the 0 at the end of list
o/p l = [7,6,8,2,1,0,0,0,0,0,0]
"""
givenls = [1, 2, 0, 0, 6, 7, 8, 0, 0, 0, 0]
flst = []
for dig in givenls:
    if dig > 0:
        flst.insert(0, dig)    # insert add given index add item
    else:
        flst.append(dig)     # append add item at the end

print("Sift all the 0 at the end of list : ",flst)


print("================================================")
"""
31. Count Elements in List Within Range
Write a Python program to count the number of elements in a list within a specified rang
"""
def CountElementListRange(mylist):
    count = 0
    dct = {}
    for element in range(40, 100):
        if element >= 40 and element in mylist:
            dct[element] = mylist.count(element)

    for value in dct.values():
        count += value
        
    return f"{count}, Elements in List Within Range."


cobj = CountElementListRange([10, 20, 30, 40, 40, 40, 70, 80, 99])
print(cobj)
print("================================================")
"""
32. Check if List Contains Sublist
Write a Python program to check whether a list contains a sublist.
"""

def is_Sublist(l, s):
    sub_set = False
    # Check if 's' is an empty list; in this case, 's' is a sublist of any list
    if s == []:
        sub_set = True

    # Check if 's' is equal to 'l'; if so, 's' is a sublist of 'l'
    elif s == l:
        sub_set = True

    elif len(s) > len(l):
        sub_set = False
    
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                # If 'n' equals the length of 's', 's' is a sublist of 'l
                if n == len(s):
                    sub_set = True

    return sub_set

a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]

objec1 = is_Sublist(a,b)
objec2 = is_Sublist(a,c)
print(objec1)
print(objec2)

print("================================================")
"""
35. Create List with Range Concatenation
Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""
ele = ['p', 'q']
n = 5
rang = []
for u in range(1,n+1):
    for e in ele:
        o = e + str(u)
        print(o)
        rang.append(o)
print(rang)
print("================================================")
def extended_lidt(lst):
    lst.extend([10])

b = [5,10,15,20]
extended_lidt(b)
print(len(b))
print("================================================")
"""
36. Get Variable ID or String
Write a Python program to get a variable with an identification number or string.
"""
def GetVariableIdOrString(variable):
    # Print the hexadecimal representation of the unique identifier (memory address) of 'variable'
    # 'id(x)' returns the memory address, and 'format(id(x), 'x')' formats it as a hexadecimal string
    return "Variable Id: ", format(id(variable), 'x')

var_int = GetVariableIdOrString(100)
var_str = GetVariableIdOrString("w3resource")

print(var_int)
print(var_str)

n2 = 100
print(id(n2))
print(format(id(n2), 'x'))


print("================================================")
"""
37. Find Common Items in Lists
Write a Python program to find common items in two lists.
"""
def FindCommonItems(list1, list2):
    mixed = []
    for color in list1:
        for colr in list2:
            if color == colr:
                mixed.append(color)
    return mixed

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]

num1 = [1, 12, 21, 34, 45, 99]
num2 = [12, 33, 65, 99, 45, 78]

common1 = FindCommonItems(color1,color2)
common2 = FindCommonItems(num1, num2)
print(common1)
print(common2)

# using list comprhension
comm = [i for i in color1 for j in color2 if i == j]
print(comm)
print("================================================")

"""
38. Swap Every n-th and (n+1)th Values
Write a Python program to change the position of every n-th value to the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
"""
def SwapEveryNth_and_Nplus(lst):

    for num in range(0, len(lst)-1, 2):
        print(num)
        lst[num], lst[num+1] = lst[num+1], lst[num]
        print(lst)
    return lst
        

myobj1 = SwapEveryNth_and_Nplus([0,1,2,3,4,5])
print(myobj1)
print("================================================")
"""
39. Convert Integers List to Single Integer
Write a Python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350
"""
def ConvertIntListToSingleInt(number):
    single = ""
    a = str(number)
    for i in number:
        single += str(i) 

    return int(single)

create = ConvertIntListToSingleInt([11, 33, 50])
print(create)

print("-------------One more Approach---------------")
# one more approach
# split values without split() method
a = [11,33,50]

x,y,z = a

print(str(x)+str(y)+str(z))
print(x)
print(y)
print(z)
print("================================================")
"""
40. Split List by First Character
Write a Python program to split a list based on the first character of a word.
"""
from itertools import groupby
from operator import itemgetter

# Define a list 'word_list' containing words
word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

# Use 'groupby' to group and sort the words in 'word_list' based on the first letter of each word
# Iterate through the groups and print the first letter and the words starting with that letter
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    # print(letter)
    for word in words:
        print(word)
print("================================================")
"""
41. Create Multiple Lists
Write a Python program to create multiple lists.
"""
dxnry = {}

for lst in range(1, 21):
    dxnry[str(lst)] = []

print(dxnry)

print("================================================")
"""
42. Find Missing and Additional Values in ListsQA  
Write a Python program to find missing and additional values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h
"""
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

common_elements = set(list1) & set(list2)  # Find common elements
print(common_elements) 

list1 = [x for x in list1 if x not in common_elements]
list2 = [y for y in list2 if y not in common_elements]

print(list1)
print(list2)

print("-------------econd approach--------------")
# second approach
li1 = ['a','b','c','d','e','f']
li2 = ['d','e','f','g','h']
common = []
for i in li1:
    for j in li2:
        if i == j:
            common.append(i)

print(common)

for k in common:
    if k in li1 and k in li2:
        li1.remove(k)
        li2.remove(k)

print(li1)
print(li2)
print("----------------One more Approach------------------")

l3 = ['a','b','c','d','e','f']
l4 = ['d','e','f','g','h']

for g in l3[:]:
    print(g)
    if g in l4:
        l3.remove(g)
        l4.remove(g)

print(l3)
print(l4)
print("================================================")
"""
43. Split List into Variables
Write a Python program to split a list into different variables.
"""
color = [
    ("Black", "#000000", "rgb(0, 0, 0)"),
    ("Red", "#FF0000", "rgb(255, 0, 0)"),
    ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
]

var1, var2, var3 = color

print(var1)
print(var2)
print(var3)


print("================================================")
"""
44. Generate Groups of Consecutive Numbers
Write a Python program to generate groups of five consecutive numbers in a list.
"""
l = [[5*i + j for j in range(1, 6)] for i in range(5)]
print(l)
print("================================================")

"""
6. Sort Tuples by Last Element
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
"""
t = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
final = []
get_last_elemrnt_each_tup = []

for lastEle in t:
    get_last_elemrnt_each_tup.append(lastEle[-1])

# getting last element of each tuple using list comphension=
# get_last_elemrnt_each_tup = [ele[-1] for ele in t]
# print("===============>>>>", get_last_elemrnt_each_tup)
get_last_elemrnt_each_tup.sort()
print(get_last_elemrnt_each_tup)

for num in get_last_elemrnt_each_tup:
    for small in t:
        if num == small[-1]:
            # print(small)
            final.append(small)
        
print(final)        
    


