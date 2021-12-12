# Uses python3
import numpy as np
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    #write your code here
    n = (len(dataset)-1)//2 +1
    T = np.zeros((n,n),np.int64)
    for i in range(0,n):
        T[i,i]=int(dataset[2*i])

    def minmax(i,j,T=T):
        mn = math.inf
        mx = -math.inf
        for k in range(i,j):
            a = evalt(T[i,k],T[k+1,j],dataset[2*k+1])
            b = evalt(T[i,k],T[j,k+1],dataset[2*k+1])
            c = evalt(T[k,i],T[k+1,j],dataset[2*k+1])
            d = evalt(T[k,i],T[j,k+1],dataset[2*k+1])
            mn = min(mn,a,b,c,d)
            mx = max(mx,a,b,c,d)
        return (mn,mx)

    for s in range(1,n):
        for i in range(n - s):
            j = i+s
            T[i,j],T[j,i] = minmax(i,j)

    return T[n-1,0]

print(get_maximum_value(input()))
