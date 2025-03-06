# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = ["eat","tea","tan","ate","nat","bat"]

finaloutput = []

for i in strs:
    anagsublist = []
    for j in strs:
        if j == i:
            anagsublist.append(j)
        else:
            count = 0
            for k in i:
                if k in j:
                    count+=1
                if count == 3:
                    anagsublist.append(j)

    if anagsublist in finaloutput:
        pass
    else:
        finaloutput.append(anagsublist)

print("Anagrams list: ", finaloutput)
print("=======================================================")
"""
Group Anagrams
Input: strs = ["listen", "silent", "enlist", "rat", "tar", "art"]
Output: [['listen', 'silent', 'enlist'], ['rat', 'tar', 'art']]
"""
lst = ["listen", "silent", "enlist", "rat", "tar", "art"]
anagramsList = []

for word in lst:
    sublst =[]
    for j in lst:
        if j == word:
            sublst.append(j)
        else:
            count = 0
            for k in word:
                if k in j:
                    count+=1
                if count == len(word):
                    sublst.append(j)
    if sublst in anagramsList:
        pass
    else:
        anagramsList.append(sublst)

print("Group Anagrams:", anagramsList)
print("============================================================")
# solve above function using Decorator
def DecoratorForAnagrams(anag):
    def wrapper(strs):
        finalop = []
        for wrd in strs:
            l = []
            for w in strs:
                if w == wrd:
                    l.append(w)
                else:
                    c=0
                    for k in wrd:
                        if k in w:
                            c+=1
                        if c==3:
                            l.append(w)

            if l in finalop:
                pass
            else:
                finalop.append(l)
        print("Here Group of anagram Using Decorator: ",finalop)
        return anag(f"tesss,{strs}")
        
    return wrapper

@DecoratorForAnagrams
def anag(strs):
    print("Here is Given list :", strs)

strs = ["listen", "silent", "enlist", "rat", "tar", "art"]
d = anag(strs)
print("================================================")

# find given number is prime or not

def CheckPrime(num):
    """
    if the give number divisible 1 or itself then number is prime othewise it's not a prime
    """
    count = 0
    i=1
    while i<=num:
        if num%i==0:
            count+=1
        i=i+1
    if count == 2:
        return f"Given number {num} is a prime!"
    else:
        return f"Given number {num} not a prime!"


result1 = CheckPrime(11)
result2 = CheckPrime(4)
result3 = CheckPrime(99)
result4 = CheckPrime(7)

print(result1)
print(result2)
print(result3)
print(result4)

no = 99
cno = 0
for i in range(1,no+1):
    if no % i == 0:
        cno += 1
if cno == 2:
    print("Given no is a prime!")
else:
    print("given no not a prime!")


print("================================================")
# reverse number 123 =>321

num = 123
rev = 0
while num > 0:
    rev = (rev*10) + num%10
    num = num//10
print("Reverse number: ",rev)







