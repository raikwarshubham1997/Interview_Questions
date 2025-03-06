#1. Group Anagrams

# Input: strs = ["listen", "silent", "enlist", "rat", "tar", "art"]
# Output: [['listen', 'silent', 'enlist'], ['rat', 'tar', 'art']]
strs = ["listen", "silent", "enlist", "rat", "tar", "art"]

mainlist = []
for st in strs:
    # print(st)
    sublist = []
    # print("=======================")
    for j in strs:
        # print(j)
        if j == st:
            sublist.append(j)
        else:
            c = 0
            for k in st:   # each word itrate listen l,i,s,t,e,n and match j value
                if k in j:
                    c += 1
                if c == len(st):
                    sublist.append(j)
    print(sublist)
    if sublist in mainlist:
        pass
    else:
        mainlist.append(sublist)

print("Group Anagrams : ", mainlist)
print("================================================================")
"""
Group Strings by First Letter

Input: strs = ["apple", "banana", "cherry", "apricot", "blueberry", "carrot"]
Output: [['apple', 'apricot'], ['banana', 'blueberry'], ['cherry', 'carrot']]
(Explanation: Strings are grouped by their first letter.)
"""
strs = ["apple", "banana", "cherry", "apricot", "blueberry", "carrot"]

mainGrouped = []
for st in strs:
    firstLatterMatch = []
    for j in strs:
        if j[0]== st[0]:
            firstLatterMatch.append(j)
    if firstLatterMatch in mainGrouped:
        pass
    else:
        mainGrouped.append(firstLatterMatch)

print("First Latter Match Grouped : ", mainGrouped)

print("================================================================")

"""
3. Group Numbers by Parity (Even/Odd)

Input: nums = [1, 2, 3, 4, 5, 6]
Output: [[2, 4, 6], [1, 3, 5]]
(Explanation: Numbers are grouped into even and odd numbers.)
"""
nums = [1, 2, 3, 4, 5, 6]

finalList = []
odd = []
even = []

for i in nums:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
finalList.append(even)
finalList.append(odd)
print(finalList)

"""
4. Group Strings by Length

Input: strs = ["a", "abc", "de", "f", "gh", "xyz"]
Output: [['a', 'f'], ['de', 'gh'], ['abc', 'xyz']]
(Explanation: Strings are grouped based on their lengths.)
"""
strs2 = ["a", "abc", "de", "f", "gh", "xyz"]
finalOp =[]
for i in strs2:
    print(len(i))
    sublst = []
    for j in strs2:
        if len(j) == len(i):
            print(j)
            sublst.append(j)
    if sublst in finalOp:
        pass
    else:
        finalOp.append(sublst)

print("Final List: ", finalOp)

print("================================================================")
"""
Group Palindromes

Input: strs = ["madam", "level", "hello", "world", "civic", "deified"]
Output: [['madam', 'level', 'civic', 'deified'], ['hello', 'world']]
(Explanation: Palindromes and non-palindromes are grouped separately.)
"""
strs3 = ["madam", "level", "hello", "world", "civic", "deified"]

Palidroms =[]
palindromList =[]
nonPalindrom = []
for char in strs3:
    
    print(char)
    print(char, "==", char[::-1])
    if char == char[::-1]:
        palindromList.append(char)
    else:
        nonPalindrom.append(char)

Palidroms.append(palindromList)
Palidroms.append(nonPalindrom)
print(Palidroms)
print("==========================List============================")

"""
Group Numbers by Remainder When Divided by 3

Input: nums = [3, 6, 7, 9, 10, 15, 17]
Output: [[3, 6, 9, 15], [7, 10], [17]]
(Explanation: Numbers are grouped based on their remainder when divided by 3.)
"""
nums = [3, 6, 7, 9, 10, 15, 17]
finalRemainder = []

for i in len(nums):
        if j%3==0:
            tempp.append(j)


