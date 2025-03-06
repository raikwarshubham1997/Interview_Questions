"""
Shallow Copy:
* A shallow copy creates a new object, but it only copies references to the elements inside the original object.
* If the original object has nested objects (like lists inside a list), the shallow copy still refers to those nested objects instead of copying them.
* Changes to the nested objects will affect both the original and the copy.
"""
import copy

original_list = [[1, 2, 3],[4, 5, 6]]
shallow_copy = original_list.copy()

print(shallow_copy)

shallow_copy[0][0] = 100      # modify both orignal and shallow

print("Shallow Copy: ",shallow_copy, "and ", "Id : ", id(shallow_copy))
print("Orignal Copy: ",original_list, "and ", "Id : ", id(original_list))

print("Original Nested List ID:", id(original_list[0]))  # नेस्टेड लिस्ट का ID
print("Shallow Nested List ID:", id(shallow_copy[0]))
'''
1. original_list एक नेस्टेड लिस्ट है, जिसमें अंदर की लिस्ट ([1, 2, 3] और [4, 5, 6]) अलग-अलग ऑब्जेक्ट्स हैं।
2. जब हमने copy.copy(original_list) किया, तो बाहरी लिस्ट की एक नई कॉपी बनी लेकिन अंदर की लिस्ट्स की रेफरेंस ही कॉपी हुई।
'''


"""
Deep Copy:
* A deep copy creates a new object and recursively copies everything inside it, including all nested objects.
* This means the copy is completely independent of the original.
* Changes to the nested objects in the copy will NOT affect the original.

"""

original_list = [[1, 2, 3],[4, 5, 6]]
deep_copy = copy.deepcopy(original_list)

deep_copy[0][0] = 100  # Modify nested object

print(deep_copy)
print(original_list) 



import gc
print(gc.get_stats())  # Check garbage collection stats