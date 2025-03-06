'''
6. Sort Tuples by Last Element

Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
mytup = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

my = []
final = []

for i in mytup:
    print(i)
    my.append(i[-1])

if my != []:
    print("yyyyy")
    my.sort()
    print(my)
    for i in my:
        for k in mytup:
            if i == k[-1]:
                final.append(k)


print(final)
