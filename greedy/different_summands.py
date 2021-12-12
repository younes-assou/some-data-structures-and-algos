def optimal_summands(n):
    sm = []
    t=n
    k=1
    while t-k>k:
        sm.append(k)
        t-=k
        k+=1   
    sm.append(t)
    return sm

n = int(input())
summands = optimal_summands(n)
print(len(summands))
print(*summands)
