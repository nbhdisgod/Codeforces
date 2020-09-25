#inputCopy
#5
#10 12 13 15 10
#outputCopy
#5 1
#inputCopy
#4
#10 20 30 40
#outputCopy
#1 2

from math import *
def fun(arr):
    misa=[]
    req=[]
    for i in range(0,len(arr)):
        misa.append(abs(arr[(i+1)%len(arr)]-arr[(i)%len(arr)]))
    req.append((misa.index(min(misa)))%len(misa)+1)
    req.append((misa.index(min(misa))+1)%len(misa)+1)
    return req

n=int(input())
l=list(map(int,input().split()))
print(*fun(l))


