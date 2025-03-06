'''
5. Count Strings with Same Start and End

Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

strls = ['abc', 'xyz', 'aba', '1221']

count = 0 
match = []
for st in strls:
    print(st, st[0], "and", st[-1])
    if st[0] == st[-1]:
        match.append(st)
        count+=1
    else:
        count

print("Expected Result : ", count, "and the match words is : ",match)

print("=================Function====================")

def count_start_end_same(lst):
    counts = 0
    for st in lst:
        if st[0] == st[-1]:
            counts += 1
        else:
            counts
    return counts

str_lst = ['abc', 'xyz', 'aba', '1221']
result = count_start_end_same(str_lst)
print("The Count Strings with Same Start and End is using function : ", result)


def count_start_end_same_decorator(myfunc):   # decorater can take a function as an argument
    def wrapper(items):
        counts = 0
        word =[]
        for st in items:
            if st[0] == st[-1]:
                word.append(st)
                counts += 1
            else:
                counts
        orignal_func = myfunc(items)
        return counts, "and", orignal_func, word
    return wrapper

@count_start_end_same_decorator
def mainfun(items):
    print("The word which is match :")
    

strlst = ['abc', 'xyz', 'aba', '1221']
result = mainfun(strlst)
print("The Count Strings with Same Start and End is Using Decorator : ",result)
