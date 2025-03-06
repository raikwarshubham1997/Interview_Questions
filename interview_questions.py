'''
"""
Move zeros to end of list
"""
lst = [1,2,0,0,3,6,0,5,9,0,0,0]
temp = []
zeros = []

for i in range(len(lst)):
    if lst[i] != 0:
        temp.append(lst[i])          #[1,2,3,6,5,9]
    else:
        zeros.append(lst[i])         #[0,0,0,0,0,0]

print(temp)
print(zeros)
print(temp+zeros)
# ----------------------------------------
# or using pre-defne function
lst.sort(reverse=True)
print(lst)
#-----------------------------------------
# or using extend method 
result = [n for n in lst if n != 0]
result.extend([0] * lst.count(0))
print(result)
# =====================================================
'''


pl = "abcbglshytukik"

def is_palindrome(s):
    return s == s[::-1]

def find_palindrome(s):
    palindromes = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            print(substring)
            if is_palindrome(substring) and len(substring) > 1:
                palindromes.append(substring)
    return palindromes

palindromes = find_palindrome(pl)
print("Palindrome substrings:", palindromes)



# 3
inp = [
    {"india": 40, "code": "1001"},
    {"pakistan": 20, "code": "1001"},
    {"china": 40, "code": "1001"},
    {"india": 56, "code": "1002"},
    {"pakistan": 14, "code": "1002"},
    {"china": 30, "code": "1002"}
]

'''
output
[
    {"india": 40, "pakistan": 20, "china": 40, "code": "1001"},
    {"india": 56, "pakistan": 14, "china": 30, "code": "1002"}
]
'''
grouped = {}

for item in inp:
    code = item["code"]
    # print("code", code)
    if code not in grouped:
        grouped[code] = {"code":code}
    for key, value in item.items():
        # print(">>>>>>>>>>>",key)
        if key != "code":
            grouped[code][key] = value

out = list(grouped.values())
print(out)


#===========================rev=======================================
#Write a python program to count the frequency of words appearing in a string
inp="Sheena loves eating apple and mango .Her sister also loves eating apple and mango"

splstr = inp.split()
print(splstr)
mydict = {}

for st in splstr:
    if st in mydict:
        mydict[st] += 1
    else:
        mydict[st] = 1
print(mydict)

#==================================================================
#find count of geeks
a="geeks for geeks"
#o/p:- 2
spl = a.split()
mydc = {}

for st in spl:
    if st == 'geeks':
        if st in mydc:
            mydc[st] += 1
        else:
            mydc[st] = 1

print(mydc)

#==================================================================
# create decorator python add two numbers
def add_two_numbers_decorator(func):
    def wrapper(a, b):
        result = a + b
        return func(result)
    return wrapper

@add_two_numbers_decorator
def display_result(result):
    print(f"The result is: {result}")

display_result(3,7)

print("===============================================")
vow = ["a","e","i","o","u"]
# o/p res = {'a': 3, 'e': 1, 'i': 1, 'o': 1}
mydict = {}
mystr = "My name is Johnathan"

for i in vow:    
    if i in mystr:
        # count = i.count()
        mydict.update({i:mystr.count(i)})
        
print(mydict)
print("==============================================")
# Write a function that takes a list of integers and returns the sum of all unique elements in the list. Unique elements are those that appear exactly once in the list.
nums = [1, 2, 3, 2, 4, 5, 5]
summ = 0
for i in nums:
    if nums.count(i) == 1:
        # print(i)
        summ+=i
print(summ)
        
# using dictinary
lst = [1,2,3,2,4,5,5]

dd = {}
for i in lst:
    if i in dd:
        #getting if key is existing
        dd[i] += 1
    else:
        dd[i]=1

print(dd)

calcu = 0
for key, value in dd.items():     #items returns tuple
    if dd[value] == 1:
        calcu+= key

print(calcu)

"""d = {}
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
unq=[]
add = 0
for j, k in d.items():
    if d[k] == 1:
        # print(j)
        unq.append(j)
        add+=j

print("Unique value :", unq)
print("Sum of unique value :", add)"""
print("==============================================")
   
words = ['how', 'much', 'is[br]to[br]', 'the', 'fish[br]', 'no', 'really']
#find [br] and replace it with <br/>
l=[]
for k in words:
    if 'br' in k:
        x= k.replace('[br]', '<br/>')
        l.append(x)
    else:
        l.append(k)
        
print(l)

# using list comprhension
# words = [w.replace('[br]', '<br />') for w in words]
# print("List Comprhension",words)


# solve without replace function
l2=[]

for wrd in words:
    modified_word = ''
    i = 0
    while i < len(wrd):
        if wrd[i:i+4] == '[br]':      # Checking for [br] manually
            modified_word += '<br/>'
            i +=4       # Skipping '[br]'

        else:
            modified_word += wrd[i]
            print(modified_word)
            i+=1

    l2.append(modified_word)
    print(l2)
    
print("Manually find and replace: ",l2)

print('much'[0:0+4])
print("==============================================")

# check whether number is prime or not 
'''
generally each number can divisible by 1 or itself then number is prime otherwise number can divisible more then two number then it's not a prime 
'''
var_n = 7
count = 0

for num in range(1, var_n+1):
    if var_n % num == 0:
        count += 1

if count == 2:
    print("Given number is Prime!")
else:
    print("Number not Prime!")
    

c = 0
i=1
while var_n >= i:
    if var_n % i == 0:
        c += 1

    i = i+1
if c == 2:
    print("Given number Prime!!!!")
else:
    print("Number not Prime!")
