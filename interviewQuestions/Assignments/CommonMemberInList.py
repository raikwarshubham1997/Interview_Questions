"""
11. Check Common Member Between Two Lists

Write a Python function that takes two lists and returns True if they have at least one common member.
"""

l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 8, 9]

# for num in l1:
#     for no in l2:
#         if num == no:
#             print(True)
#         else:
#             print(False)

def FindCommonWord(lst1, lst2):
    result = False

    for num in lst1:
        for no in lst2:
            if no == num:
                result = True
                
                return result

output = FindCommonWord(l1, l2)
print(output)
        
