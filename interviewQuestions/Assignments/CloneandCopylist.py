"""
Clone or Copy a List

Write a  Python program to clone or copy a list.
"""

l = [12, 32, 22, 34, 56]

new_list = list(l)

final = l.copy()
print("Copy list : ", final)

print(new_list)
print(l)