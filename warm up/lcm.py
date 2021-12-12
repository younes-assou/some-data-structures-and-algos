def gcd(a, b):
    while True:
        r=a%b
        if r==0:return b
        a,b = b,r

def lcm_naive(a, b):
    x=gcd(a,b)
    if x==1:return a*b
    else:return a*b//x

a, b = map(int, input().split())
print(lcm_naive(a, b))

