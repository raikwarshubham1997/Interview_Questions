'''

str1 = "i.like.this.program.very.much"
# Output: str = “much.very.program.this.like.i” 

s = "i like this program very much"
words = s.split(' ')
string =[]
for word in words:
    print(word)
    string.insert(0, word)
 
print(string)
print("Reversed String:")
print(" ".join(string))

print("---------------======================------------------")
# Python program to find the longest common prefix
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
arr.sort()
print(arr)

first = arr[0]
last = arr[-1]

minLength = min(len(first), len(last))
print(minLength)

i = 0

while i < minLength and first[i] == last[i]:
    i += 1

print(first[:i])

print("---------------======================------------------")

# 1. Calculate string length.

str1 = "w3resource.com"
print(len(str1))
count = 0

for i in str1:
    count+=1

print("calculation: ", count)

# using function

def CalculateLength(st):
    count = 0
    for chr in st:
        count += 1

    return count

calcLen = CalculateLength(str1)
print(">>>>>", calcLen)

# using decorator

print("---------------======================------------------")
"""
2. Count character frequency in a string.

Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

staring2 =  "google.com"
wordCount = {}
for chr in staring2:
    wordCount[chr] = staring2.count(chr)

print("Here frequency of character : ", wordCount)

def FrequencyDecorator(func):
    def wrapper(mystr):
        frqun = {}
        for j in mystr:
            frqun[j] = mystr.count(j)
        print("Using Decorator: ",frqun)
        return func(frqun)
    return wrapper

@FrequencyDecorator
def MainFunction(frqun):
    print("This is main function.",frqun)

MainFunction(staring2)
print("---------------======================------------------")
"""
3. Get string of first and last 2 chars.

Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""
inpStr = "w3resource"               #input("Enter String : ")

if len(inpStr) >= 2:
    first_2_char = inpStr[:2]        # forword [start:stop]
    last_2_char = inpStr[-2:]           # reverse [start: stop]
    print(last_2_char)
    combination = first_2_char + last_2_char    
    print(combination)
else:
    print("Empty String")
print("---------------======================------------------")

"""
4. Replace first char occurrences with $.

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
st = "restart"
frst = st[0]
finalword = ''
for i in st[1:]:
    print(i)
    if i == frst:
        finalword+='$'
        # st.replace(i, '$')
    else:
        finalword+=i

print(frst + finalword)
print("================================")

print("---------------======================------------------")
"""
5. Swap first 2 chars of 2 strings.

Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

"""

mystrs = 'abc', 'xyz'

mystrs = mystrs[1][0:2]+'c'+ " " +mystrs[0][0:2]+'z'
print(type(mystrs))

print(mystrs)


# using function
def swapp(a, b):
    first = a[:2]
    second = b[:2]
    re = second+a[-1], first+b[-1]
    return re


reslt = swapp('abc', 'xyz')
print(reslt)
print("---------------======================------------------")

"""
6. Add ing or ly to a string.

Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
stt =  'abc'
print(stt[-3:])
if len(stt) >= 3 and stt[-3:] == 'ing':
    stt += 'ly'
if len(stt) >= 3 and stt[-3:] != 'ing':
    stt += 'ing'
print(stt)

def IncludeIngOrLyAtTheEnd(st):
    if len(st) >= 3:
        if st[-3:] == 'ing':
            st += 'ly'
        else:
            st += 'ing'
    
    return st

incld1 = IncludeIngOrLyAtTheEnd('abc')
incld2 = IncludeIngOrLyAtTheEnd('string')
incld3 = IncludeIngOrLyAtTheEnd('ab')
print(incld1)
print(incld2)
print(incld3)
print("---------------======================------------------")

"""
7. Replace 'not'...'poor' with 'good'.

Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""

sd = 'The lyrics is poor!'
if 'not' in sd: 
    ind = sd.index('not')
    print(ind)
    x =sd.replace(sd[ind:-1], "good")
    print("Final Output :",x)
else:
    print(sd)

# using function

def ReplaceNotToPoor(goo):
    if 'not' in goo:
        ind = goo.index('not')
        rep = goo.replace(goo[ind:-1], 'good')
        return rep
        
    return goo

obj1 = ReplaceNotToPoor('The lyrics is not that poor!')
print(obj1)
obj2 = ReplaceNotToPoor('The lyrics is poor!')
print(obj2)
print("---------------======================------------------")

# Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

print("---------------======================------------------")
"""
8. Find longest word in a list.

Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""


def find_longest_word(words_list):
    word_len = []

    for n in words_list:
        word_len.append((len(n), n))
    print(word_len)
    word_len.sort()

    return word_len[-1][0], word_len[-1][1]

result = find_longest_word(["PHP", "Exercises", "Backend"])

# Print the longest word and its length.
print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])
print("---------------======================------------------")

"""
9. Remove nth character from a string.

Write a  Python program to remove the nth index character from a nonempty string.
"""
# str2 = "Python"
# remove_char = input("Enter Character : ")
# if str2.lower() != "":
#     remv = str2.lower().replace(remove_char,"")
#     print(remv)
# else:
#     print("String Empty")


# using function 

# def RemoveNthCharacter(wooo, remv):
#     if wooo != "":
#         op = wooo.lower().replace(remv,"")
#         return op

#     else:
#         return f"String Empty"

# givenstr = "Python"
# remove_char2 = input("Enter Character to Remove string: ")
# finalObj =  RemoveNthCharacter(givenstr,remove_char2)
# print(finalObj)


print("---------------======================------------------")

"""
10. Swap first and last chars of a string.

Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
"""
swapp = "Python Programing"

if swapp != "":
    firstChar = swapp[0]
    lastChar = swapp[-1]
    final = lastChar+swapp[1:-2]+firstChar
    print(final)
else:
    print("Empty String")

# using Function

def SwappingFirstAndLast(str):
    if str != "":
        f = str[0]      #get first char of string
        l = str[-1]     #get last char of string
        swap = l+str[1:-2]+f
        return swap
    return f"Empty String"

a = 'Python Developer'
obj = SwappingFirstAndLast(a)
print(obj)

# Using Decorator 
def Swapping(fx):
    def wrapper(str):
        if str != "":
            f = str[0]
            l = str[-1]
            swp = l+str[1:-2]+f
            print(swp)
            return fx(str)       
        else:
            return "Empty string"
    return wrapper

@Swapping
def mainSwap(str):
    print("The original String : ", str)


swp = mainSwap(a)


print("---------------======================------------------")

"""
11. Remove odd index chars from a string.

Write a Python program to remove characters that have odd index values in a given string.
"""
inpStr = "Python Developer"
evenStr = ''
for i in range(len(inpStr)):
    if i%2 ==0:
        evenStr+=inpStr[i]
print(evenStr)
print("-------Using Function--------------")
# using function
def RemoveCharacters(orignal):
    even = ''
    for i in range(len(orignal)):
        if i%2 == 0:
            even+=orignal[i]
    return even
object1 = RemoveCharacters("Python Developer")
object2 = RemoveCharacters("Python Programming")
object3 = RemoveCharacters("Java Developer")
print(object1)
print(object2)
print(object3)   

print("-------Using Decorator--------------")
def RemoveCharactersDecorator(orignal):
    def wrapper(str):
        even = ''
        for i in range(len(str)):
            if i%2 == 0:
                even+=str[i]
        print("Remove odd Character : ", even)
        return orignal
    return wrapper

@RemoveCharactersDecorator
def OrignalFunc(str):
    print(f"Orignal String is {str}")

deffi1 = OrignalFunc("Python Developer")
deffi2 = OrignalFunc("Python Programming")
deffi3 = OrignalFunc("Java Developer")



print("---------------======================------------------")

"""
12. Count word occurrences in a sentence.

Write a Python program to count the occurrences of each word in a given sentence.
"""
words = "the quick brown fox jumps over the lazy dog.".lower()
wr = words.split()
dictt = {}
for wrd in wr:
    dictt[wrd] = words.count(wrd)

print(dictt)
print("-------Using Function--------------")
def Occurrences(str):
    dic ={}
    for wrd in str:
        dic[wrd] = str.count(wrd)
    return dic

occu1 = Occurrences(wr)
occu2 = Occurrences("using png image".split())
print(occu1)
print(occu2)

print("-------Using Decorator--------------")
def OccurrencesDecorator(occuran):
    def wrapper(str):
        dic ={}
        for wrd in str:
            dic[wrd] = str.count(wrd)
        print("Remove odd Character : ", dic)
        return occuran
    return wrapper

@OccurrencesDecorator
def OccurrencesFunc(str):
    print(f"Orignal String is {str}")

occ1 = OccurrencesFunc(wr)
occ2 = OccurrencesFunc("using png image".split())
occ3 = OccurrencesFunc("Java Developer".split())


print("---------------======================------------------")

"""
2. Count character frequency in a string.

Write a Python program to count the number of characters (character frequency) in a string.
Sample String : 'google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""
frequ = 'google.com'
d={}
for i in frequ:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

print("---------------======================------------------")
"""
13. Display input in upper and lower case.

Write a Python  script that takes input from the user and displays that input back in upper and lower cases.
"""
# inpCase = input("What is your favorite language? ")

# print("My favorite language is ", inpCase.upper())

# print("My favorite language is ", inpCase.lower())

print("---------------======================------------------")

"""
14. Sort distinct words in comma-separated input.

Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""
commasape = "red, white, black, red, green, black"
spl = commasape.split(",")
# or 
# words = [word for word in commasape.split(",")]
# print(words)

print(",".join(sorted(list(set(spl)))))



print("---------------======================------------------")
"""
15. Wrap word(s) in HTML tags.

Write a Python function to create an HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""

def add_tag(tag, word):
    return "<%s>%s<%s>" % (tag, word, tag)

firstTag = add_tag('i', 'Python')
secondTag = add_tag('b', 'Python Tutorial')
print(firstTag)
print(secondTag)

print("---------------======================------------------")
"""
16. Insert string into middle of another.

Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""
def insert_sting_middle(str, word):
    return str[:2]+word+str[-2:]

print(insert_sting_middle("[[]]",'Python'))
print(insert_sting_middle("<<>>",'Python'))
print(insert_sting_middle("{{}}",'Python'))

print("---------------======================------------------")
"""
17. Repeat last 2 chars of a string 4 times.

Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
"""
def insert_end(str):
    return str[-2:]*4

obj1 = insert_end("Python")
obj2 = insert_end("Exercises")
print(obj1)
print(obj2)

print("---------------======================------------------")
"""
18. Get first 3 chars of a string.

Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
"""
def first_three(threechar):
    if len(threechar)>=3:
        return threechar[:3]
    else:
        return "The length of the string is less than 3."
a1 = first_three("ipy")
a2 = first_three("Python")
print(a1)
print(a2)

print("---------------======================------------------")
"""
19. Get substring before a specific character.

Write a Python program to get the last part of a string before a specified character.
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
"""
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])
print("---------------======================------------------")

"""
20. Reverse string if length is a multiple of 4.

Write a Python function to reverse a string if its length is a multiple of 4.
"""
def ReverseIfLen4(str):
    if len(str)%4 == 0:
        return str[::-1]
    else:
        return "String length not multiple of 4 : ", str
lenChar = ReverseIfLen4("Ruby")
lenChar2 = ReverseIfLen4("Python")
print(lenChar)
print(lenChar2)
print("---------------======================------------------")

"""
21. Uppercase string if 2+ uppercase chars in first 4.
Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
"""

p ="PyThon"
x=0
for c in p[:4]:
    if c.upper() == c:
        # print("YES")
        x+=1
    # else:
        # print("NO")

if x >= 2:
    print(p.upper())
else:
    print("No Uppercase")
print("---------------======================------------------")

"""
23. Remove newline from a string.
Write a Python program to remove a newline in Python.
"""
x1 = 'Python Exercises\n'
print(x1)
# Use the rstrip() method to remove trailing whitespace characters, including the newline character.
# Then, print the modified 'str1' with trailing whitespace removed
print(x1.rstrip())
print("---------------======================------------------")
"""
24. Check if string starts with specified chars.
Write a Python program to check whether a string starts with specified characters.
"""
def CheckStringStart(st, char):
    print(char.lower() ,"and", st[0:len(char)])
    if char.lower() == st[0:len(char)].lower() or char.upper() == st[0:len(char)].upper():
        return True
    else:
        return False

d = CheckStringStart("w3resource.com", "w3r")
print(d)
print("---------------======================------------------")

"""
30. Print numbers with 2 decimal places.
Write a Python program to print the following numbers up to 2 decimal places.
"""
a = 3.1415926
b = 12.9999

print("original number: ", a)
print("Formatted Number: "+"{:.2f}".format(x))

print("Original Number: ", b)

# Format the value of 'b' to two decimal places and print it with a label.
print("Formatted Number: "+"{:.2f}".format(b))
print("---------------======================------------------")

"""
30. Print numbers with 2 decimal places.

Write a Python program to print the following numbers up to 2 decimal places.
"""
x = 3.1415926

# Define a variable 'y' and assign it the value -12.9999 (a negative floating-point number).
y = -12.9999

# Print an empty line for spacing.
print()

# Print the original value of 'x' with a label.
print("Original Number: ", x)

# Format the value of 'x' to two decimal places and include a sign (positive or negative) in the result.
print("Formatted Number with sign: "+"{:+.2f}".format(x))

# Print the original value of 'y' with a label.
print("Original Number: ", y)

# Format the value of 'y' to two decimal places and include a sign (positive or negative) in the result.
print("Formatted Number with sign: "+"{:+.2f}".format(y))

# Print an empty line for spacing.
print() 
print("---------------======================------------------")
"""
38. Count substring occurrences in string.
Write a Python program to count occurrences of a substring in a string.
"""
str1 = 'The quick brown fox jumps over the lazy dog.'
sp = str1.split(' ')
print(sp)
check = 'brown'
c = 0
for wrd in sp:
    if check == wrd:
        c+=1
    
print("Number of occurance : ", c)
'''
print("---------------======================------------------")
"""
39. Reverse a string.
Write a Python program to reverse a string.
"""

def ReverseStr(str):
    d = str[::-1]
    return d

o1 = ReverseStr("abcdef")
o2 = ReverseStr("Python Exercises.")
print(o1)
print(o2)
print("---------------======================------------------")
"""
40. Reverse words in a string.
Write a Python program to reverse words in a string.
"""
def ReverseWords(string):
    st = string.split(" ")
    # print(st)
    revs = st[::-1]
    t = " ".join(revs)
    return t
queck = "The quick brown fox"
ob1 = ReverseWords(queck)
print(ob1)


# using Decorator
def ReverseDecorator(func):
    def wrapper(string):
        res = func(string)
        print("From Argument function: ",res)
        convtStr = " ".join(res)
        return f"Here Reverse words in a string By Decorator: {convtStr}"
    return wrapper

@ReverseDecorator
def ReverseWordsFunc(string):
    print("Original String : ",string)
    st = string.split(" ")
    # print(st)
    revs = st[::-1]
    return revs
    # t = " ".join(revs)
    # return t
queck = "The quick brown fox"
ob1 = ReverseWordsFunc(queck)
print(ob1)

print("---------------======================------------------")
"""
41. Strip specific characters from string.
Write a Python program to strip a set of characters from a string.
"""
def StripSpecificChar(string, chars):
    st = string.split(" ")
    lst = []
    for chr in chars:
        # print(chr)
        for c in st:
            if chr in c:
                c = c.replace(chr, "")
                lst.append(c)
    finalStr = " ".join(lst)
    
    return finalStr

strip = "aeiou"
qik = "The quick brown fox"

op = StripSpecificChar(qik, strip)
print(op)
print("---------------======================------------------")
"""
42. Count repeated characters in string.
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
"""
def CountRepetedCharInString(mystr):
    dxn = {}  # dictionary is a unorderd collection that's why output 
    i = 1
    for chars in mystr:
        if chars not in dxn:
            dxn.update({chars:i})
        else:
            dxn[chars] += 1

    for word, count in dxn.items():
        if count > 1:
            print(word, count)
    # return dxn

sampleStr = "thequickbrownfoxjumpsoverthelazydog"
ssobj = CountRepetedCharInString(sampleStr)

"""
# we have used dictionary is a unorderd collection that's why output
t 2
h 2
e 3
u 2
r 2
o 4
"""

print("---------------======================------------------")
"""
44. Find character indices in string.
Write a Python program to print the index of a character in a string.
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9
"""
def FindCharecterIndex(string):
    for indx in range(len(string)):
        print(f"Current character {string[indx]} position at: {indx}")
# word = "w3resource"

wobj = FindCharecterIndex("w3resource")
print("--------------------------------------------")
wobj2 = FindCharecterIndex("Python Programming.")

print("---------------======================------------------")
"""
45. Check if string has all alphabet letters.
Write a Python program to check whether a string contains all letters of the alphabet.
"""
import string

# Create a set 'alphabet' containing all lowercase letters using 'string.ascii_lowercase'.
alphabet = set(string.ascii_lowercase)

# Define an input string.
input_string = 'The quick brown fox jumps over the lazy dog'

# Check if the set of lowercase characters in the input string contains all the letters of the alphabet.
# Print the result (True or False).
print(set(input_string.lower()) >= alphabet)

# Update the input string.
input_string = 'The quick brown fox jumps over the lazy cat'

# Check if the set of lowercase characters in the updated input string contains all the letters of the alphabet.
# Print the result (True or False).
print(set(input_string.lower()) >= alphabet) 

print("---------------======================------------------")
"""
46. Convert string to list of words.
Write a  Python program to convert a given string into a list of words.
Sample Output:
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
"""
def ConvertStrToList(str):
    convt_lst = str.split(" ")

    return convt_lst

convtob1 = ConvertStrToList("This is a test string")
convtob2 = ConvertStrToList("The quick brown fox jumps over the lazy dog.")   

print(convtob1)
print(convtob2)

# Use Decorator
def ConvertStrToListByDecorator(functionx):
    def wrapper(str):
        res =  functionx(str)
        print(res)
        print("---------By Decorator-------------")
        newStr = "The-quick-brown-fox-jumps-over-the-lazy-dog." 
        nwe = newStr.split("-")
        return nwe
    return wrapper

@ConvertStrToListByDecorator
def ConvertStrToList(str):
    convt_lst = str.split(" ")

    return convt_lst

convtob3 = ConvertStrToList("This is a test string")
convtob4 = ConvertStrToList("The quick brown fox jumps over the lazy dog.")   


print("---------------======================------------------")
"""
47. Lowercase first n characters of string.
Write a Python program to lowercase the first n characters in a string.
"""
def LowercaseFirstN_Char(str):
    n = 4    # means starting first 4 character should be lowercase
    if len(str) > n:
        # the length of given staring is greter than n
        st = str[:n].lower() + str[n:]
        return st
# str1 = 'W3RESOURCE.COM'

lowr1 = LowercaseFirstN_Char('W3RESOURCE.COM') 
lowr2 = LowercaseFirstN_Char('PYTHON IS HIGHLEVEL LANGUAGE')
print(lowr1)
print(lowr2)
print("---------------======================------------------")

"""
48. Swap commas and dots in a string.
Write a Python program to swap commas and dots in a string.
Sample string: "32.054,23"
Expected Output: "32,054.23"
"""
amount = "32.054,23"
maketrans = amount.maketrans

# Translate (replace) the characters ',' with '.', and '.' with ',' in the 'amount' string using the 'maketrans' variable.
amount = amount.translate(maketrans(',.', '.,'))

# Print the modified 'amount' string with the swapped decimal and comma characters.
print(amount)
print("---------------======================------------------")
"""
49. Count and display vowels in text.
Write a Python program to count and display vowels in text.
"""
def CountVowels_and_Display(text):
    count = 0
    vowelList = []
    vowels = ["a","e","i","o","u"]
    for vowel in vowels:
        for ex in text:
            if ex.lower() == vowel:
                count += 1
                if ex.lower() not in vowelList:
                    vowelList.append(ex)

    print(count)
    print("Vowels Display:", vowelList)

mkobj = CountVowels_and_Display("Welcome to w3resource.com")
print("---------------======================------------------")
"""
50. Split string on last delimiter occurrence.
Write a Python program to split a string on the last occurrence of the delimiter.
"""
str1 = "w,3,r,e,s,o,u,r,c,e"

# Split the string 'str1' into a list of substrings using the ',' separator, starting from the right.
# Split at most 1 time and print the result.
print(str1.rsplit(',', 1))

# Split the string 'str1' into a list of substrings using the ',' separator, starting from the right.
# Split at most 2 times and print the result.
print(str1.rsplit(',', 2))

# Split the string 'str1' into a list of substrings using the ',' separator, starting from the right.
# Split at most 5 times and print the result.
print(str1.rsplit(',', 5)) 
print("---------------======================------------------")
