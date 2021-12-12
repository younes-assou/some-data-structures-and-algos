def fib(n):
    if n<=1:return n
    n0 = 0
    n1 = 1
    k = 1
    while k < n:
        n0, n1 = n1, n1 + n0
        k+=1
    return n1

def pisanoPeriod(m):
    previous, current = 0, 1
    i=0
    while True:
        previous, current = current, (previous + current) % m
        i+=1
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i

def get_fibonacci_huge_naive(n, m):
    n = n%pisanoPeriod(m)
    return fib(n)%m

n, m = map(int, input().split())
print(get_fibonacci_huge_naive(n, m))
