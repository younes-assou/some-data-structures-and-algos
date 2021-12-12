def calc_fib(n):
    if n<=1:return n
    n0 = 0
    n1 = 1
    k = 1
    while k < n:
        n0, n1 = n1, n1 + n0
        k+=1
    return n1

n = int(input())
print(calc_fib(n))
