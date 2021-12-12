def isgore(a,b):
    nbr1=int(a+b)
    nbr2=int(b+a)

    return nbr1>=nbr2

def largest_number(a):
    res = ""
    while len(a)!=0:
        mx=0
        for x in a:
            if isgore(str(x),str(mx)):
                mx=x
        res+=str(mx)
        a.remove(mx)
    return res


n = int(input())
a = list(map(int, input().split()))
print(largest_number(a))
    
