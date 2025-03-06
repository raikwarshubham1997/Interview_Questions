# print odd number from 1 to 50

list_ofodd =[]
for num in range(1, 50):
    if num % 2 != 0:
        list_ofodd.append(num)
print(list_ofodd)


lst = []
i = 1
while i<=50:
    if i%2 !=0:
        lst.append(i)
    i=i+1
print(lst)