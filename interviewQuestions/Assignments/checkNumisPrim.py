# write a program to check whether a given number is  prime or not

'''
What is prime number?
ans = > which have only 2 factors ( matlav jo sirf 2 numbers se divisible ho 1 or itself) like
n = 13

factor = 1 and 13 only that means this is a prime number

now we have to need to solve
count = 0      # this is for count how many factors of n number 
i = 1    # loop start from 1 to given number range






17. Check If All Numbers Are Prime

Write a  Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
Sample Data:
([0, 3, 4, 7, 9]) -> False
([3, 5, 7, 13]) -> True
([1, 5, 3]) -> False



'''


# for check prime number we have to need one is input N and one count variable for counting factors 

num = int(input("Enter a number to check it's prime number: "))

count = 0
for n in range(1,num+1):
    if num%n == 0:
        count += 1
if count == 2:
    print("Given number is Prime.")
else:
    print("Not a Prime Number!.")

print(count)



n = int(input("Enter Number: ")) 
count = 0
i = 1

while i<=n:
    if n%i==0:
        count += 1
    i = i+1

if count==2:
    print("Prime number")

else:
    print("Not Prime")

    



