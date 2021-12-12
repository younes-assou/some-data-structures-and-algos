n=int(input())
nbrs=list(map(int, input().split()))

nbr1=max(nbrs)
idx = nbrs.index(nbr1)
nbrs[idx] = 0
nbr2=max(nbrs)

print(nbr1*nbr2)
