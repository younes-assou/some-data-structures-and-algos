def gcd_naive(a, b):
    while True:
        r=a%b
        if r==0:return b
        a,b = b,r

a, b = map(int, input().split())
print(gcd_naive(a, b))
