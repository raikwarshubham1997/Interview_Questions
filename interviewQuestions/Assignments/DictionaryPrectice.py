'''

"""
# Sort (ascending and descending) a dictionary by value
Write a  Python program to sort (ascending and descending) a dictionary by value.
o/p  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
"""

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(d.items())
covtTuple =  d.items()     # convert dict to tuple for the itration

value = []   # saprated values of dict
key = []     # saprated keys of dict

for i in covtTuple:      # items() return dictionary item from tuple
    print(i[1])
    value.append(i[1])    # append all the values of dict in value variable
    key.append(i[0])      # append all the keys of dict in key variable
print(value, key)        # [2, 4, 3, 1, 0] [1, 3, 4, 2, 0]

# conver decending
value.sort(reverse=True)    # reverse=True use for sort list ascending to descending
print(value)
# [4, 3, 2, 1, 0] o/p

mynewList =[]      # storing sorted descending order tuple 
for i in value:      #[4, 3, 2, 1, 0]
    for j in covtTuple:    #[(1, 2), (3, 4), (4, 3), (2, 1), (0, 0)]
        print(">>>>>",j)
        if i == j[1]:
            mynewList.append(j)

print(mynewList)
print(dict(mynewList))
print("-------------------------------Dictionary---------------------------------")

"""
2. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""

mydict = {0: 10, 1: 20}

# mydict[2] = 30      # short solution is this
# print("Solution 1: ",mydict)


# mydict.update({2:30})
# print("Solution 2: ",mydict)

# using logic 

convtTup = list(mydict.items())

print(convtTup[-1])      # [(0, 10), (1, 20)]

dd = convtTup[-1]

ddd = dd[0] +1 
print(ddd)
mydict[ddd] = dd[1]+10

print("Solution 3: ",mydict)

print("-------------------------------Dictionary---------------------------------")

"""
3. Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""    
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {}

for val in (dic1, dic2, dic3):
    print(val)
    dic4.update(val)

print(dic4)

# this is also good way
convDic1 = list(dic1.items())
convDic2 = list(dic2.items())
convDic3 = list(dic3.items())

temp = convDic1 + convDic2 + convDic3
print(dict(temp))

print("-------------------------------Dictionary---------------------------------")

"""
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


existKey = []
for i in d:
    existKey.append(i)

print(existKey)

newKey = int(input("Enter new key: "))

if newKey not in existKey:
    newVal= newKey*10
    d.update({newKey:newVal})
    print("New Key add successfully : ", d)
else:
    print(f"Entered key {newKey} already exist enter different key : {d}")

# Create with function
def FindKeyExistOrNot(dic, key):
    newKey = int(input("Enter new key: "))

    existKey = []      # storing all keys
    for i in d:
        existKey.append(i)
    return f"List of Existing key : ", existKey
    
"""
print("-------------------------------Dictionary---------------------------------")

# 5. Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30} 
for key, value in d.items():
    print(key, "->", value )
print("-------------------------------Dictionary---------------------------------")

"""
6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
n = 5
empty ={}
for dic in range(1,n+1):
    # empty[dic] = dic*dic    #currect 
    empty.update({dic:dic*dic})    #currect

print(empty)
print("-------------------------------Dictionary---------------------------------")
"""
7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""
no = 15
mydict = {}
for i in range(1, no+1):
    mydict.update({i:i**2})
    # mydict[i] = i**2

print(mydict)


# create by function

def CreateDictOfSquares(num):
    newDict = {}
    for i in range(1,num+1):
        newDict.update({i:i**2})
    return newDict

number = 15
result = CreateDictOfSquares(number)
print(result)

# create by decorator
def CreateDictOfSquaresByDecorator(takefunc):
    def wrapper(num):
        dic = {}
        for key in range(1, num+1):
            dic.update({key:key**2})

        print("Using Decorator : ",dic)
        return takefunc(num)
    return wrapper

@CreateDictOfSquaresByDecorator
def TakeArgument(num):
    print("This is the aditional Function.", num)

no = 15

result = TakeArgument(no)

print("-------------------------------Dictionary---------------------------------")

# 8. Write a Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200}

d2 = {'x': 300, 'y': 200}

d1.update(d2)

print(d1)
print("-------------------------------Dictionary---------------------------------")

# 10. Write a Python program to sum all the items in a dictionary.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
sumOfItem = 0

for val in my_dict.values():
    sumOfItem += val

print("The Sum of Dictionary items : ", sumOfItem)

print("-------------------------------Dictionary---------------------------------")

# 11. Write a Python program to multiply all the items in a dictionary.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

result = 1

for i in my_dict.values():
    result = result*i

print("The multiply all the items in a dictionary : ", result)
print("-------------------------------Dictionary---------------------------------")

# 12. Write a Python program to remove a key from a dictionary.
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}


my_dict.pop('data2')

print(my_dict)
print("-------------------------------Dictionary---------------------------------")

# 13. Write a Python program to map two lists into a dictionary.
key = ['red', 'green', 'blue']
value = ['#FF0000', '#008000', '#0000FF']
# o/p {"res":"#FF0000","green":"#008000","blue":"#0000FF"}

my_dict = {}
for i in range(len(key)):
    my_dict.update({key[i]:value[i]})

print("Maped two list into a dictionary : ",my_dict)
print("-------------------------------Dictionary---------------------------------")

# 14. Write a Python program to sort a given dictionary by key.

color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}

for key in sorted(color_dict):
    # Print each key-value pair where '%s' is a placeholder for the key and its associated color code.
    print("%s: %s" % (key, color_dict[key]))
print("-------------------------------Dictionary---------------------------------")

# 15. Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'x': 500, 'y': 5874, 'z': 560}
d = []
for i in my_dict.values():
    d.append(i)

print(d)
letMax = d[0]
letMin = d[0]

for num in d:
    if num > letMax:
        letMax = num
for num in d:
    if num < letMin:
        letMin = num

print(f"The maximum {letMax} and minimum {letMin} values of a dictionary")

print("-------------------------------Dictionary---------------------------------")

# 16. Write a Python program to get a dictionary from an object's fields.
class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'green'
        self.z = 'blue'

    def do_nothing(self):
        pass

test = dictObj()
print(test.__dict__)

print("-------------------------------Dictionary---------------------------------")
# Write a  Python program to remove duplicates from the dictionary.
student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

result = {}
for key, value in student_data.items():
    if value not in result.values():
        result.update({key:value})

print(result)
print("-------------------------------Dictionary---------------------------------")

# 18. Write a Python program to check if a dictionary is empty or not.
my_dict = {}

if my_dict == {}:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

# or
if not bool(my_dict):
    print("Dictionary is empty")

print("-------------------------------Dictionary---------------------------------")
"""
19. Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

"""
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

result = {}
for key, value in d1.items():
    print(key, value)
    for k, v in d2.items():
        if key == k:
            result[key]=value+v
        if key not in d2:
            result[key]=value
        if k not in d1:
            result[k]=v
            

print("Result is: ", result)


print("-------------------------------Dictionary---------------------------------")

"""
20. Write a  Python program to print all distinct values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
commonData = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

uniqueContent = []
for i in commonData:      # {"V":"S001"} one by one comming dict
    for j in i.values():         # each value of dict
        if j not in uniqueContent:
            uniqueContent.append(j)

print(set(uniqueContent))



print("-------------------------------Dictionary---------------------------------")
"""
21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd
"""
dictData = {'1':['a','b'], '2':['c','d']}
getDictVal = []

# getting all the values of dictionary and append in getDictVal
for val in dictData.values():
    getDictVal.append(val)

print(getDictVal)

# final output 
for i in getDictVal[0]:     # ['a','b']  i='a', i='b'
    for j in getDictVal[1]:   # ['c','d'] j ='c', j='d'
        d = i+j
        print(d)


print("-------------------------------Dictionary---------------------------------")
# Write a  Python program to find the highest 3 values of corresponding keys in a dictionary.

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

convtTup = list(my_dict.items())
print(convtTup)

letMax = convtTup[0][-1]
print(letMax)
op = []
for i in convtTup:
    if i[-1] > letMax:
        op.append(i[0])
print(op)


# when more then 5 items in dict 
convtTup = list(my_dict.items())
print(convtTup)

letMax = convtTup[5][-1]
print(letMax)
op = []
for i in convtTup:
    if len(op) < 3:            # only first three values append
        if i[-1] > letMax:
            op.append(i[0])
print(op)
print("-------------------------------Dictionary---------------------------------")

"""
23. Write a Python program to combine values in a list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})
"""
# mylist = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]


# d = {}
# for i in mylist:
#     print(i)
#     for key, value in i.items():
#         if key in i:
#             d.update({key:value})

# print(d)
        


print("-------------------------------Dictionary---------------------------------")

"""
24. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
"""
newDict ={}
mystr = "w3resource"

for letter in mystr:
    newDict[letter] = mystr.count(letter)
    # newDict.update({letter:mystr.count(letter)})

print(newDict)

print("-------------------------------Dictionary---------------------------------")

"""
25. Write a Python program to print a dictionary in table format.
C1 C2 C3                                                                                                      
1 5 9                                                                                                         
2 6 10                                                                                                        
3 7 11
"""
my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    # Print each row of transposed data as space-separated values.
    print(*row)


print("-------------------------------Dictionary---------------------------------")

"""
26. Write a  Python program to count the values associated with a key in a dictionary.
"""
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0
d = 0
for dic in student:
    count += dic['id']
    if dic['success'] == True:
        d += 1

print("count", count)
print("d",d)
print("-------------------------------Dictionary---------------------------------")
"""
27. Write a Python program to convert a list into a nested dictionary of keys.
"""
num_list = [1, 2, 3, 4]

newDict = current ={}

for name in num_list:
    current[name] = {}
    print(current)
    current = current[name]
    print(">>>>",current)

print(newDict)
print("-------------------------------Dictionary---------------------------------")

vow = ["a","e","i","o","u"]
# o/p res = {'a': 3, 'e': 1, 'i': 1, 'o': 1}
mydict = {}
mystr = "My name is Johnathan"

for i in vow:    
    if i in mystr:
        # count = i.count()
        mydict.update({i:mystr.count(i)})
        
print(mydict)

# using function
def CountVowelsOccurance(str,vow):
    mydict = {}
    for i in vow:
        count=0
        for j in str:
            print(i,j)
            if j == i:
                count+=1
        mydict[i]=count
    return mydict
cx = CountVowelsOccurance(mystr, vow)
print("cx,",cx)
                



print("-------------------------------Dictionary---------------------------------")
# arrenge dictionary assending order according to age

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}, 
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}, 
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
        } 
        #Typecast age str to int

age_lst = []
newdc = {}
for i in people.items():
    # print(i[1]["age"])
    age_lst.append(i[1]["age"])
age_lst.sort()
print(age_lst)

# for getting oldest person
letmaxx = age_lst[0]

for k in age_lst:
    for key, val in people.items():
        if k == val["age"]:
            # print(key,val)
            newdc[key] = val

print(people)
print(newdc)


# Access a Specific Person's Details
# Write a Python program to access and print the details of a specific person given their ID.

def GetPersonDetails(uid, data):

    for id, detail in people.items():
        if userId == id:
            return f"Here the details of ID {userId} \n", detail

userId = int(input("Enter user ID : "))

objid = GetPersonDetails(userId, people)
print(objid)


# Find the Oldest Person in the Dictionary
# Write a Python program to determine who the oldest person is based on the age field.
def GetOldestPerson(dc):
    for id, detail in dc.items():
        if detail['age'] > letmaxx:
            letmaxx = detail['age']
    # if letmaxx in dc.values():
    #     return dc

print(">>>>>>>>>>>>>>>>>",letmaxx)     


# Add a New Person to the Dictionary
# Write a Python program to add a new person's details to the dictionary.
people[5] = {'name':'Yash','age':'23','sex':'Male'}
print(people)

# Update the Age of a Person
# Write a Python program to update the age of a specific person in the dictionary.
for data in people.items():
    if data[1]["name"] == "Yash":
        data[1]["age"] = '31'
print(people)



# Count the Number of Males and Females
# Write a Python program to count how many males and females are in the dictionary.


pdata = {1: {'name': 'John', 'age': '27', 'sex': 'Male'}, 
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}, 
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}, 
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
        } 
male = 0
female = 0
for k, j in pdata.items():
    if j['sex'] == "Male":
        male+=1
    elif j['sex'] == "Female":
        female+=1

print("Male : ", male)
print("Female : ", female)

# Remove a Person from the Dictionary
# Write a Python program to delete a person's record using their ID.
for data in pdata.keys():
    print(data)
    if data == 5:
        del pdata[data]
print(pdata)

print("-------------------------------Dictionary---------------------------------")

# 28. Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

for i, j in num.items():
    num[i]=sorted(j)

print(num)
print("-------------------------------Dictionary---------------------------------")

# 29. Write a Python program to remove spaces from dictionary keys.
student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

lg = {}
for kk, vv in student_list.items():
    d = kk.replace(' ','')
    lg[d] = vv
    print(d)
print(lg)
print("-------------------------------Dictionary---------------------------------")
test = {1:1, 2:1, 3:1, 4:1}
for key in test:
    test[key]+=1

print(test)


'''

print("-------------------------------Dictionary---------------------------------")
"""
30. Write a Python program to get the top three items in a shop.
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
Expected Output:
item4 55
item1 45.5
item3 41.3
"""
sample = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
l = []
for k, v in sample.items():
    l.append(v)

l.sort()
print(l)
maxlist = []
letMax = l[0]
for h in l[-3:]:
    maxlist.append(h)
print("maxlist,", maxlist)
for i in l[-1:2:1]:
    print(i)
    for key, value in sample.items():
        if i in value:
            print(key, value)

print("-------------------------------Dictionary---------------------------------")
"""
31. Write a Python program to get the key, value and item in a dictionary.
"""
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key  value  count")
c = 1
for k,v in dict_num.items():
    
    print(k,'  ',v, '    ', c)
    c+=1
print("-------------------------------Dictionary---------------------------------")
"""
32. Write a Python program to print a dictionary line by line.
"""
students = {'Aex': {'class': 'V', 'roll_id': 2}, 'Puja': {'class': 'V', 'roll_id': 3}}

print(students['Aex'])
for data in students:
    print(data)
    for d in students[data]:
        print("....", d)
        print(d, ":", students[data][d])
print("-------------------------------Dictionary---------------------------------")
"""
33. Write a Python program to check if multiple keys exist in a dictionary.
"""
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

print(student.keys() >= {"class","name"})
# Check if the set of keys in 'student' contains the keys 'name' and 'Alex'.
# Note that 'Alex' is not a key, so this check will always be False.
print(student.keys() >= {"name", "Alex"})
print(student.keys() >= {"roll_id", "name"})
print("-------------------------------Dictionary---------------------------------")
"""
34. Write a Python program to count the number of items in a dictionary value that is a list.
"""
dictx =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count = 0
for val in dictx.values():
    count += len(val)

print("The Number of items : ", count)

# using function
def CountNumberOfItems(mydict):
    c = 0
    for item in mydict.values():
        c += len(item)

    return f"Count the number of items in a dictionary value : {c}"

ob = CountNumberOfItems(dictx)
print(ob)


#using Decorator
def CountNumberOfItemsByDecorator(countFunc):
    def wrapper(mydict):
        r = countFunc(mydict)
        print(mydict.keys())
        return f"from decorator, {r}"
    return wrapper

@CountNumberOfItemsByDecorator
def CountNumberOfItems2(mydict):
    c = 0
    for item in mydict.values():
        c += len(item)

    return f"Count the number of items in a dictionary value : {c}"

ob = CountNumberOfItems2(dictx)
print(ob)

print("-------------------------------Dictionary---------------------------------")
"""
35. Write a Python program to sort Counter by value.
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""
sampleData = {'Math':81, 'Physics':83, 'Chemistry':87}
final2 = []
temp = []
tup = list(sampleData.items())      # o/p [('Math', 81), ('Physics', 83), ('Chemistry', 87)]

for num in sampleData.values():
    temp.append(num)

temp.sort(reverse=True)
print(temp)

for i in temp:
    print(i)
    for data in tup:
        if data[-1] == i:
            print(">>>>",data[-1])
            final2.append(data)
print(final2)


# def SrotCounterByValue(mydict):
#     temp = []
#     # convert dictionary to list inside tuple
#     tup = list(mydict.items())
#     print(tup)

#     for i in mydict.values():
#         temp.append(i)
#     return temp
# cop = SrotCounterByValue({'Math':81, 'Physics':83, 'Chemistry':87})
# print(cop)
print("-------------------------------Dictionary---------------------------------")
"""
36. Write a Python program to create a dictionary from two lists without losing duplicate values.
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})
"""
list_val = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
dxx = {}


for key, value in zip(list_val,id_list):
    dxx.update({key:{value}})
print(dxx)
