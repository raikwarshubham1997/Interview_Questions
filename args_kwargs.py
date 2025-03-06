# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)

# *args for variable number of arguments
def myfun(*args):
    for arg in args:
        print(arg)

myfun('Hello!', 'My', 'Name', 'is', 'Python')



def myfun2(*args):
    dc = {}
    for arg in args:
        dc[arg] = args.count(arg)
    print('dc', dc)

myfun2(1,2,3,4,5,6,7,5,3,2,3,7)


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')




