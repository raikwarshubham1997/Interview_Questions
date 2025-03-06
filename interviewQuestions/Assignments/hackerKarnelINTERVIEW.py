
#what is decoretor write an example
def NewDecorator(func):
    def wrapper():
        print("before calling function")
        func()
        print("After calling function")
    return wrapper
    
@NewDecorator
def myfunc():
    print("This Decoratore")
    
result = myfunc()


# o/p {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}.

mystr =  "hello world"
mydict = {}
for i in mystr:
    mydict[i] = mystr.count(i)
    
print(mydict)

num = 23      # 99, 11, 7, 23
count = 0
i=1
while i<=num:
    if num % i==0:
        count += 1
    i=i+1
if count == 2:
    print(f"The number {num} is Prime")
    
else:
    print(f"The number {num} is Not Prime")





# id user_id amount dispatched
# 1   1       10000 1
# 2   2       5000  0
# id user_id amount dispatched
# 1 1 10000 1
# 2 2 5000  0
# user names, email addresses, order amounts, and dispatch statuses
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1

rows = 4
cols = 8

for i in range(rows):
    for j in range(cols):
        # Print 1 if the sum of indices is even, else print 0
        print((i + j) % 2, end=" ")
    print()
    

"""


#what is CORS ?


Users:

user_id name email mobile
1` User 1 user1@gmail.com 1122434567
2  User 2 user2@gmail.com 1231231234
3  User 3 user3@gmail.com 9988776655

Orders:

id user_id amount dispatched
1 1 10000 1
2 2 5000  0
user names, email addresses, order amounts, and dispatch statuses


dic = [{'id': 1, 'user_id':1, 'amount':10000, 'dispatched': 1},{'id': 2, 'user_id':2, 'amount':5000, 'dispatched': 0}]

d =[]
for i in dic:
    # print(i)
    if i['amount'] > 5000 and i['dispatched'] == 1:
        d.append(i)
        
print(d)

user = User.objects.get(user_id=id)
getobj = orders.objects.filter(amount>5000 and dispatched = 1)

select from order where amount>5000 and dispatched = 1 and user_id;


getnotdisp = orders.objects.filter(dispatched=0)

for get in getnotdisp:
    user = User.objects.get(id = get.user_id)
    

select from orders, user where dispatched=0;


ELECT * FROM users WHERE status = 'active' AND (name LIKE %user% OR email LIKE %user%)

getUser =  Users.objects.filter(status = 'active')

for i in getUser:
    if status = 'active' and name="Shubham"  or email="shubham@gmail.com":
        print(i.name, i.email)


SELECT full name, email, mobile number, username, and password.
full name, email, mobile number, username, and password.



1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1



for i in range(0, 4):
    for j in range(0, 8):
        if i >= 1:
            print(0, end=" ")
        if i == 0:
            print(1, end=" ")
    print()


Input: "hello world"
Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


mystr =  "hello world"
mydict = {}
for i in mystr:
    mydict[i] = mystr.count(i)
    
print(mydict)

# check given number is prime or not     # when the number is divisible by 1 or itself called prime like 13 divide by 1 or only 13 it means 13 is prime
num = 4
count = 0
i=1
while i<=num:
    if num % i==0:
        count += 1
    i=i+1
if count == 2:
    print(f"The number {num} is Prime")
    
else:
    print(f"The number {num} is Not Prime")

"""
