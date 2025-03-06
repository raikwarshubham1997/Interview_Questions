
# Get Largest Number in List
mylst = [1, 2, -8, 0]
maxx = mylst[0]
minn = mylst[0]
for i in mylst:
    if i > maxx:
        maxx = i
    

for low in mylst:
    if low < minn:
        minn = low

print("The largest number of list is: ", maxx)
print("The lowest number of list is: ", minn)




def find_maxno(myls):
    maxx = myls[0]
    for num in myls:
        if num > maxx:
            maxx = num
    return maxx

result = find_maxno([21, 32, 4, -3, 56])
print("Max number is : ", result)


def find_maxno_Userinp(myls):
    maxx = myls[0]
    for num in myls:
        if num > maxx:
            maxx = num
    return maxx

userinp =[]
len_of_no = int(input("Enter how many numbers you want in the list for the max number: "))
for i in range(0,len_of_no):
    mynum = int(input("Enter number : "))
    userinp.append(mynum)
print(userinp)
result = find_maxno_Userinp(userinp)
print("Max number is : ", result)





print("+=============================================================+")

def find_min(items):
    minn = items[0]
    for j in items:
        if j < minn:
            minn = j
    return minn

result = find_min([2,4,-6,-8,-3,6,5,0])
print("The minimum number of the list is: ", result)

# take user input
def find_minno_Userinp(items):
    minn = items[0]
    for j in items:
        if j < minn:
            minn = j
    return minn

userls = []
howmanynum = int(input("Enter how many numbers you want in the list for the min number : "))
for i in range(0,howmanynum):
    usrinp =int(input(" Enter number which you want compair : "))
    userls.append(usrinp)
print(userls)

result = find_minno_Userinp(userls)
print(result)