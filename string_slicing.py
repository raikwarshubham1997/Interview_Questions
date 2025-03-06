b = "Hello, World!"
print(b[0:6])

print(b[:8])
print(b[2:])

'''
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
dd = "World!"
print(dd[-5])
print(dd[-2])
print(dd[-5:-2])

# =======Remove Whitespace=======
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

print()