def gridTraveler(m,n, memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    elif (n,m) in memo:
        return memo[(n,m)]

    if m==1 and n==1: return 1
    if m==0 or n==0: return 0

    memo[(m,n)] = gridTraveler(m-1,n, memo)+gridTraveler(m,n-1, memo)

    return memo[(m,n)]

m,n = map(int, input().split())
print(gridTraveler(m,n))
