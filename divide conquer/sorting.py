import random

def partition3(a, l, r):
    #write your code here
    i = l
    m = l
    n = r
    pivot = a[l]
    while i<=n:
        if a[i]<pivot:
            a[i], a[m] = a[m], a[i]
            i+=1
            m+=1
        elif a[i]>pivot:
            a[i], a[n] = a[n], a[i]
            n-=1
        else :
            i+=1
    return m,n



def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m-1)
    randomized_quick_sort(a, n, r)

n = int(input())
a = list(map(int, input().split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
