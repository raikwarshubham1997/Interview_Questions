"""Remove Duplicates from List

Write a  Python program to remove duplicates from a list."""


a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
unique =[]

for num in a:
    if num not in unique:
        unique.append(num)

print(unique)


# using function
def RemoveDuploicate(items):
    unique = []
    for num in items:
        if num not in unique:
            unique.append(num)
    return unique

result = RemoveDuploicate(a)
print("Here is the list without duplicate number: ", result)



# using decorator
def RemoveDuploicateDecorator(func):
    def wrapper(items):
        unique = []
        for num in items:
            if num not in unique:
                unique.append(num)
        return unique
    return wrapper

def duplicate(items):
    print("******Remove all duplicate******")

result = duplicate(a)
print("Here is the list without duplicate number: ", result)


