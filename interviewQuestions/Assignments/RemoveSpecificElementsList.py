"""
12. Remove Specific Elements from List

Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

my = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def RemoveSpecific(lst):
    newlst = []
    removeItem = [0, 4, 5]

    for i in range(len(lst)):
        if i not in removeItem:
            newlst.append(lst[i])
    return newlst
        

result = RemoveSpecific(my)
print(result)