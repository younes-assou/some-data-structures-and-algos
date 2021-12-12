def lis(x):
    T = [[] for i in range(len(x))]
    for i in range(len(x)):
        T[i] = [x[i],*T[i]]
        for j in range(i):
            if x[j]<x[i] and len(T[i])<len(T[j])+1:
                T[i]=[x[j],*T[j]]
    return T

def lcs2(a, b, i, j):
    #write your code here
    if i==0 or j==0: return 0

    return min(len(a), len(b))


#n = input()
a = list(map(int, input().split()))
#m = input()
#b = list(map(int, input().split()))

#print(lcs2(a, b, len(a)-1, len(b)-1))
print(lis(a))