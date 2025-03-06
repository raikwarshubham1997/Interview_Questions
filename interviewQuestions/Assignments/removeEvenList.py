"""
14. Remove Even Numbers from List

Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""
num = [7, 8, 120, 25, 44, 20, 27]
oddno = []
for i in num:
    if i % 2 != 0:
        oddno.append(i)

print(oddno)


def RemovEven(lst):
    oddno = []
    for i in num:
        if i % 2 != 0:
            oddno.append(i)
    return oddno

result = RemovEven(num)
print(result)