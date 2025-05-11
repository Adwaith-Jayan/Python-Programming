from functools import reduce
def fact(n):
    nums=[x for x in range(1,n+1)]
    print(reduce(lambda x,y:x*y,nums,1))

fact(int(input("Number")))
